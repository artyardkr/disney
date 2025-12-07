
import re

file_path = '/Users/songhyowon/글로벌경영ppt/final_presentation.html'

def move_strategy_after_a8():
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Helper to find slide by content
    def find_slide_range(content, marker_text):
        # Find the slide div containing the marker
        # We search for <div class="slide" id="slide..."> that precedes the marker
        # and the next <div class="slide" ...> or end of container
        
        # Find index of marker
        marker_idx = content.find(marker_text)
        if marker_idx == -1:
            print(f"Error: Marker '{marker_text}' not found.")
            return None

        # Find the start of the slide containing this marker
        # Search backwards from marker_idx for '<div class="slide"'
        slide_start_idx = content.rfind('<div class="slide"', 0, marker_idx)
        if slide_start_idx == -1:
             print(f"Error: Could not find start of slide for marker '{marker_text}'.")
             return None
        
        # Find the end of this slide. 
        # It ends before the NEXT '<div class="slide"' or '</div><!-- slide-container -->' 
        # But simply looking for next slide tag is safer if we assume slides are sequential.
        # However, we want to find a BLOCK of slides.
        
        return slide_start_idx

    # 1. Locate Strategy Block
    # Start: Slide with "Orbit Diagram" (or "5대 글로벌 전략" comment if reliable, but content is safer)
    # The Orbit slide has class="orbit-container"
    strategy_start_marker = 'class="orbit-container'
    strategy_start_idx = find_slide_range(content, strategy_start_marker)
    
    # End: Slide with "The 5 Pillars of Success"
    strategy_end_marker = 'The 5 Pillars of Success'
    # We want the END of this slide.
    # So we find the start of the NEXT slide after this one.
    
    end_marker_idx = content.find(strategy_end_marker)
    if end_marker_idx == -1:
        print("Error: Strategy end marker not found")
        return

    # Find start of the 5 Pillars slide
    last_strategy_slide_start = content.rfind('<div class="slide"', 0, end_marker_idx)
    
    # Find start of the next slide (which should be the start of A1?? No, A1 is before. 
    # Wait, the Strategy block is currently at the END of the HTML (after Cases? or before?)
    # Based on previous file view, Strategy (Slide 29-34) was AFTER A1-A8 but Where?
    # Actually, in reordered file: Intro -> Analysis(A1-A8...Cases...) -> Strategy?
    # Let's check if Strategy is indeed at the end.
    
    # We need to find the end of the 5 Pillars slide.
    # Look for the next '<div class="slide"' after last_strategy_slide_start + 1
    next_slide_idx = content.find('<div class="slide"', last_strategy_slide_start + 1)
    
    if next_slide_idx == -1:
        # It might be the last slide. Find end of slide-container or </div>
        # But we also have References slide? 
        # In my reorder script: Preamble + A + C + B + Footer.
        # B was Strategy. C was Expansion (14-39).
        # So Strategy (B) is AFTER Expansion (C).
        # Expansion included A1-A8 AND Cases AND References.
        # So Strategy is at the very end (before Footer).
        # Wait, if B is at the end, then References (part of C) is BEFORE Strategy.
        print("Strategy block seems to be at the end.")
        strategy_block_end = content.rfind('</div>', 0, content.rfind('<div class="controls"'))
        # This acts as a fallback, but let's be more precise.
        # If next_slide_idx is -1, it means no more slides.
        # The closing </div> for the last slide is needed.
        # The structure is <div class="slide"> ... </div>
        pass
    else:
        strategy_block_end = next_slide_idx

    # If Strategy is the last block, we need to capture up to before the closing </div> of container
    # Let's use string slicing carefully.
    
    if next_slide_idx == -1:
        # Find </div> that closes the slide.
        # Since slides have nested divs, counting might be tricky.
        # But we know the file ends with </div></div>...
        # A safe bet is looking for <!-- ==================== A1: Porter's 5 Forces --> which was usually next?
        # No, A1 is now before.
        
        # Let's assume Strategy block is everything from strategy_start_idx to the end of slides.
        # Look for <div class="controls">
        controls_idx = content.find('<div class="controls">')
        # Backtrack to find the closing </div> of slide-container
        container_end = content.rfind('</div>', 0, controls_idx)
        strategy_block_end = container_end 

    strategy_text = content[strategy_start_idx:strategy_block_end]
    
    # Remove Strategy block from content
    content_without_strategy = content[:strategy_start_idx] + content[strategy_block_end:]
    
    # 2. Locate Insertion Point (After A8)
    a8_marker = '2026 Strategic Roadmap (2)'
    a8_idx = content_without_strategy.find(a8_marker)
    if a8_idx == -1:
        print("Error: A8 marker not found")
        return

    # Find start of A8 slide
    a8_slide_start = content_without_strategy.rfind('<div class="slide"', 0, a8_idx)
    
    # Find end of A8 slide (Start of next slide)
    next_after_a8 = content_without_strategy.find('<div class="slide"', a8_slide_start + 1)
    if next_after_a8 == -1:
        print("Error: Could not find slide after A8")
        return
        
    insertion_point = next_after_a8

    # 3. Insert Strategy Block
    final_content = content_without_strategy[:insertion_point] + strategy_text + content_without_strategy[insertion_point:]

    # 4. Renumber Slides
    counter = 0
    def replace_id(match):
        nonlocal counter
        counter += 1
        return f'id="slide{counter}"'

    final_content_renumbered = re.sub(r'id="slide\d+"', replace_id, final_content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content_renumbered)
    
    print(f"Moved Strategy block (length {len(strategy_text)}) to after A8.")
    print(f"Total slides: {counter}")

if __name__ == "__main__":
    move_strategy_after_a8()
