import os

css_block = """
@media (max-width: 768px) {
    /* =========================================================
       PADRONIZAR ALTURA E ESPAÇAMENTOS DOS CARDS 1 E 3 (Mobile)
       ========================================================= */
       
    .plan-card--60dias,
    .plan-card--anual {
        min-height: 420px !important; 
        display: flex !important;
        flex-direction: column !important;
    }
    
    /* Topo do card para manter mesma quebra e linha visivel igual */
    .plan-card--60dias .pricing-header,
    .plan-card--anual .pricing-header {
        padding: 24px 20px 20px !important;
        min-height: 85px !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* Corpo do card para preencher espaço esticado */
    .plan-card--60dias .pricing-body,
    .plan-card--anual .pricing-body {
        padding: 28px 24px !important;
        display: flex !important;
        flex-direction: column !important;
        flex-grow: 1 !important;
    }

    /* Espaçamento dos textos e valores mantendo a mesma constancia */
    .plan-card--60dias .price-desc,
    .plan-card--anual .price-desc {
        margin-bottom: 8px !important;
        line-height: 1.4 !important;
    }
    
    /* O texto extra do 3º plano "por 12 meses..." forçava alturas diferentes */
    /* Ao forçar uma altura mínima para esses spans ou empurrar o botão, a caixa se equaliza */
    
    .plan-card--60dias .price,
    .plan-card--anual .price {
        margin-top: 12px !important;
        margin-bottom: 16px !important;
    }

    /* Força os botões para a margem base criando alinhamento de rodapé perfeito */
    .plan-card--60dias .btn-outline,
    .plan-card--anual .btn-outline {
        margin-top: auto !important; 
    }
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(css_block)
