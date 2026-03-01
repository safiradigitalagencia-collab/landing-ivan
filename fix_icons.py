import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the .feature-list-icon css block
css = re.sub(
    r'\.feature-list-icon\s*{[^}]*}\s*\.feature-list-icon\s*svg\s*{[^}]*}',
    """\.feature-list-icon {
    flex-shrink: 0;
    margin-top: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 60px;
    height: 60px;
    background: rgba(15, 24, 42, 0.08);
    border: 1px solid rgba(15, 24, 42, 0.12);
    border-radius: 18px;
    box-shadow: 0 4px 10px rgba(15, 24, 42, 0.05), 0 0 16px rgba(221, 244, 105, 0.12);
}

.feature-list-icon svg {
    width: 32px;
    height: 32px;
    filter: drop-shadow(0 2px 3px rgba(15, 24, 42, 0.15));
}""",
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

