with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
html = re.sub(
    r'<div class="container hero-content text-center" style="margin: 0 auto;">',
    r'<div class="container hero-content text-center" style="margin: 0 auto; padding-top: 30px;">',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
