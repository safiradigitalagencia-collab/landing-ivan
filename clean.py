import re

def clean_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # We want to remove `style="..."` completely from these specific blocks where typography is messed up.
    # We will remove style attributes from h1, h2, h3, h4, h5, h6, p, ul, li
    content = re.sub(r'<(h[1-6]|p|ul|li)([^>]*) style="[^"]*"', r'<\1\2', content)

    # Some might be multiline or have spaces before style
    content = re.sub(r'<(h[1-6]|p|ul|li)\s+([^>]*?)\s*style="[^"]*"\s*([^>]*)>', r'<\1 \2 \3>', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

clean_html("index.html")
