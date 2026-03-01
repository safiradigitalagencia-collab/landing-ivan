import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Icon 1
icon1_old = """                                <svg viewBox="0 0 24 24" fill="url(#gradient-feature)" stroke="url(#gradient-feature)"
                                    stroke-width="1.5" stroke-linejoin="round">
                                    <!-- Icono de progresión / crecimiento -->
                                    <rect x="3" y="14" width="4" height="8" rx="1" />
                                    <rect x="10" y="8" width="4" height="14" rx="1" />
                                    <rect x="17" y="2" width="4" height="20" rx="1" />
                                </svg>"""
icon1_new = """                                <svg viewBox="0 0 24 24" fill="none" stroke="none" stroke-linejoin="round">
                                    <!-- Icono de progresión / crecimiento -->
                                    <rect x="3" y="14" width="4" height="8" rx="1" fill="#DDF469" />
                                    <rect x="10" y="8" width="4" height="14" rx="1" fill="#0F182A" />
                                    <rect x="17" y="2" width="4" height="20" rx="1" fill="#0F182A" />
                                </svg>"""
html = html.replace(icon1_old, icon1_new)

# Replace Icon 2
icon2_old = """                                <svg viewBox="0 0 24 24" fill="url(#gradient-feature)" stroke="url(#gradient-feature)"
                                    stroke-width="1" stroke-linejoin="round">
                                    <!-- Icono kettlebell minimalista -->
                                    <path
                                        d="M15 11H9c-2.21 0-4 1.79-4 4v1c0 2.76 2.24 5 5 5h4c2.76 0 5-2.24 5-5v-1c0-2.21-1.79-4-4-4z" />
                                    <path
                                        d="M14 11V6c0-1.1-.9-2-2-2s-2 .9-2 2v5H7V6c0-2.76 2.24-5 5-5s5 2.24 5 5v5h-3z" />
                                </svg>"""
icon2_new = """                                <svg viewBox="0 0 24 24" fill="none" stroke="none" stroke-linejoin="round">
                                    <!-- Icono kettlebell minimalista -->
                                    <path fill="#0F182A"
                                        d="M15 11H9c-2.21 0-4 1.79-4 4v1c0 2.76 2.24 5 5 5h4c2.76 0 5-2.24 5-5v-1c0-2.21-1.79-4-4-4z" />
                                    <path fill="#DDF469"
                                        d="M14 11V6c0-1.1-.9-2-2-2s-2 .9-2 2v5H7V6c0-2.76 2.24-5 5-5s5 2.24 5 5v5h-3z" />
                                </svg>"""
html = html.replace(icon2_old, icon2_new)

# Replace Icon 3
icon3_old = """                                <svg viewBox="0 0 24 24" fill="url(#gradient-feature)" stroke="url(#gradient-feature)"
                                    stroke-width="2" stroke-linejoin="round">
                                    <!-- Icono rayo (Rápido y eficiente) -->
                                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon>
                                </svg>"""
icon3_new = """                                <svg viewBox="0 0 24 24" fill="none" stroke="none" stroke-linejoin="round">
                                    <!-- Icono rayo (Rápido y eficiente) -->
                                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" fill="#0F182A"></polygon>
                                    <circle cx="19" cy="4" r="2.5" fill="#DDF469" />
                                </svg>"""
html = html.replace(icon3_old, icon3_new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
