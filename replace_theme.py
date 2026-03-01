import sys

def replace_colors(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace solid hex colors
    content = content.replace('#2563eb', '#22c55e')
    content = content.replace('#1d4ed8', '#16a34a')
    content = content.replace('#1e40af', '#15803d')

    # Replace rgb/rgba references
    content = content.replace('37, 99, 235', '34, 197, 94')

    # Make the target gradient on buttons
    # Since background was hardcoded to solid color `#22c55e` (after replacement) or `#16a34a`, we can swap it manually.
    content = content.replace('background: #22c55e;', 'background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);')
    content = content.replace('background: #16a34a;', 'background: linear-gradient(135deg, #16a34a 0%, #15803d 100%);')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

replace_colors('style.css')
