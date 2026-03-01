import os

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace light gray background color #F6F7F9 with #FFFFFF globally in the stylesheet
css = css.replace('#F6F7F9', '#FFFFFF')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Replaced all #F6F7F9 with #FFFFFF globally.")
