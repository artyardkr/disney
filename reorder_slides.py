
import re

file_path = '/Users/songhyowon/글로벌경영ppt/final_presentation.html'

def reorder_slides():
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Define blocks based on tool analysis (1-based index in comments, 0-based in code)
    # Preamble: Lines 1-253 (Indices 0-253)
    # Block A (Slides 1-6): Lines 254-615 (Indices 253-615)
    # Block B (Slides 7-13): Lines 616-1190 (Indices 615-1190)
    # Block C (Slides 14-39): Lines 1191-2542 (Indices 1190-2542)
    # Footer: Lines 2543-End (Indices 2542-End)

    preamble = lines[0:253]
    block_a = lines[253:615]
    block_b = lines[615:1190]
    block_c = lines[1190:2542]
    footer = lines[2542:]

    # Debug print to verify start/end of blocks
    print(f"Block A Start: {block_a[0].strip()}") # Should be slide 1
    print(f"Block B Start: {block_b[0].strip()}") # Should be slide 7
    print(f"Block C Start: {block_c[0].strip()}") # Should be slide 14
    print(f"Footer Start: {footer[0].strip()}")   # Should be empty or closing div

    # Construct new order: Preamble -> A -> C -> B -> Footer
    new_content_lines = preamble + block_a + block_c + block_b + footer
    full_content = "".join(new_content_lines)

    # Renumber slides from 1 to N
    # Regex to find id="slide\d+"
    # We need to reset the counter
    
    counter = 0
    def replace_id(match):
        nonlocal counter
        counter += 1
        return f'id="slide{counter}"'

    new_content_renumbered = re.sub(r'id="slide\d+"', replace_id, full_content)
    
    # Verify proper renumbering count
    count_slides = len(re.findall(r'id="slide\d+"', new_content_renumbered))
    print(f"Total slides renumbered: {count_slides}")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content_renumbered)

    print("Successfully reordered and renumbered slides.")

if __name__ == "__main__":
    reorder_slides()
