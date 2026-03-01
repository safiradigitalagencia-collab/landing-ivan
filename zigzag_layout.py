css_block = """
/* =========================================================
   LAYOUT ZIG-ZAG: PERSONAS REALES. RESULTADOS REALES.
   ========================================================= */

.transformation-container {
    padding-top: 40px;
}

.transformation-row {
    display: flex;
    align-items: center;
    gap: 80px;
    margin-bottom: 90px;
    text-align: left;
}

.transformation-row:last-child {
    margin-bottom: 0;
}

.transformation-row.reverse {
    flex-direction: row-reverse;
}

.transformation-image {
    flex: 1;
    max-width: 500px;
}

.transformation-image img {
    width: 100%;
    border-radius: 20px;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.08);
    display: block;
}

.transformation-text {
    flex: 1;
}

.transformation-text h3 {
    font-family: 'Oswald', sans-serif;
    font-size: clamp(1.8rem, 4vw, 2.25rem);
    line-height: 1.2;
    margin-bottom: 20px;
    color: var(--text-white);
}

.transformation-text p {
    font-size: 1.1rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin-bottom: 0;
}

@media (max-width: 768px) {
    .transformation-row, .transformation-row.reverse {
        flex-direction: column !important;
        gap: 24px;
        margin-bottom: 60px;
        text-align: center;
    }
    
    .transformation-image {
        max-width: 100%;
        order: 1; /* Garantir que a imagem venha primeiro no mobile */
    }
    
    .transformation-text {
        order: 2; /* Garantir que o texto venha depois no mobile */
    }

    .transformation-text h3 {
        margin-bottom: 12px;
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)
