import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace padding-top: 0px !important; with padding-top: 60px !important; for desktop and 40px for mobile ?
# Actually, if we just remove the specific overrides, it falls back to the .section-dark defaults: 90px desktop / 60px mobile

# Let's just restore padding-top to a normal value like 60px desktop / 40px mobile directly in the CSS
css = re.sub(
    r'\.problem\.section-dark\s*\{\s*padding-top:\s*0px\s*!important;\s*margin-top:\s*0px\s*!important;\s*\}',
    r'',
    css
)

css = re.sub(
    r'\.problem\.section-dark\s*\{\s*/\* Set padding-top back to normal as spacing is handled by hero padding bottom \*/\s*padding-top:\s*0px\s*!important;\s*\}',
    r'',
    css
)

css = re.sub(
    r'/\* Adjust problem section because of hero \*/\s*\.problem\.section-dark\s*\{\s*padding-top:\s*0px\s*!important;\s*\}',
    r'',
    css
)

css = re.sub(
    r'\.problem\.section-dark\s*\{\s*padding-top:\s*0px\s*!important;\s*\}',
    r'',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Then let me append a clean override if needed
clean_override = """
/* Fix padding of problem section */
.problem.section-dark {
    padding-top: 60px !important; 
}
@media (max-width: 768px) {
    .problem.section-dark {
        padding-top: 40px !important; 
    }
}
"""
with open('style.css', 'a', encoding='utf-8') as f:
    f.write(clean_override)

print("CSS cleaned.")
