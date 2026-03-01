import os

css_path = '/Users/amandaloba/pagina de vendas ivan/style.css'

css_to_add = """

/* --- ATUALIZACAO HERO (PREMIUM & DEPTH) --- */
.hero, header.hero {
    background:
        /* Radial left cyan */
        radial-gradient(circle at 0% 30%, rgba(0, 230, 230, 0.15) 0%, transparent 50%),
        /* Radial right green */
        radial-gradient(circle at 100% 70%, rgba(221, 244, 105, 0.12) 0%, transparent 50%),
        /* Tileable subtle hexagon mesh */
        url("data:image/svg+xml,%3Csvg width='60' height='104' viewBox='0 0 60 104' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M30 0l30 17.3v34.6L30 69.2 0 51.9V17.3H30zm0 103.9l30-17.3V52l-30-17.3L0 52v34.6z' fill='none' stroke='rgba(255,255,255,0.025)' stroke-width='1'/%3E%3C/svg%3E"),
        /* Base Deep Blue Gradient */
        linear-gradient(to bottom, #0F182A 0%, #070B13 100%) !important;
    background-color: #0F182A !important;
    background-size: auto, auto, 60px 104px, auto !important;
}

/* Video Wrapper Premium Style */
.hero-video-wrapper {
    border: 1px solid rgba(0, 230, 230, 0.25) !important;
    box-shadow: 0 15px 50px rgba(0, 0, 0, 0.4), 0 0 30px rgba(0, 230, 230, 0.1), 0 0 30px rgba(221, 244, 105, 0.05) !important;
    border-radius: 12px !important;
}
"""

with open(css_path, 'a') as f:
    f.write(css_to_add)

print("Styles appended successfully.")
