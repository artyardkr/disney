import re

file_path = '/Users/songhyowon/글로벌경영ppt/final_presentation.html'

with open(file_path, 'r') as f:
    content = f.read()

# Find the split point (start of Part 2)
split_marker = '<!-- ==================== A1: Porter\'s 5 Forces ==================== -->'
parts = content.split(split_marker)

if len(parts) != 2:
    print("Error: Could not find split marker")
    exit(1)

part1 = parts[0]
part2 = parts[1]

# Renumber slides in part 2
# Start checking what the last slide number in part 1 was?
# Rough heuristic: Part 1 ends at slide 13.
offset = 13

def replace_id(match):
    num = int(match.group(1))
    return f'id="slide{num + offset}"'

part2_fixed = re.sub(r'id="slide(\d+)"', replace_id, part2)

new_content = part1 + split_marker + part2_fixed

with open(file_path, 'w') as f:
    f.write(new_content)

print("Successfully renumbered slides in Part 2.")
