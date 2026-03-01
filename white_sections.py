css_block = """
/* =========================================================
   REMOVENDO DEGRADÊS E CORES DOS FUNDOS DAS SEÇÕES
   ========================================================= */

body,
.section-dark, 
.section-darker {
    background: #FFFFFF !important;
    background-color: #FFFFFF !important;
}

/* GARANTIR QUE HERO E OVERLAY FIQUEM CINZA CLARINHO (F6F7F9) COMO PEDIDO */
.hero, .hero-bg {
    background: transparent !important;
    background-color: transparent !important;
}

.overlay {
    background: #F6F7F9 !important;
    background-color: #F6F7F9 !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)
