/** @odoo-module **/

import { registry } from "@web/core/registry";
import { session } from "@web/session";

function applyCustomColors() {
    const colors = session.colorlist_customizer;
    if (!colors) {
        console.log('[ColorlistCustomizer] No colors in session');
        return;
    }

    // Actualizar variables CSS
    const root = document.documentElement;
    for (let i = 0; i < 12; i++) {
        const color = colors[`colorlist_${i}`];
        if (color) {
            root.style.setProperty(`--colorlist-color-${i}`, color);
        }
    }

    // Crear/actualizar elemento style para compatibilidad
    let styleEl = document.getElementById('colorlist-customizer-styles');
    if (!styleEl) {
        styleEl = document.createElement('style');
        styleEl.id = 'colorlist-customizer-styles';
        document.head.appendChild(styleEl);
    }

    // Generar CSS con alta especificidad
    let css = '';
    for (let i = 0; i < 12; i++) {
        const color = colors[`colorlist_${i}`];
        if (color) {
            css += `.o_colorlist .o_colorlist_item_color_${i}, `;
            css += `.o_widget_colorlist .o_colorlist_item_color_${i}, `;
            css += `div.o_colorlist_item_color_${i}, `;
            css += `.o_field_widget .o_colorlist_item_color_${i} `;
            css += `{ background-color: ${color} !important; }\n`;
        }
    }
    styleEl.textContent = css;
    console.log('[ColorlistCustomizer] Colors applied:', colors);
}

// Aplicar inmediatamente si el DOM está listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyCustomColors);
} else {
    applyCustomColors();
}

// Observer para detectar nuevos elementos colorlist
const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
        if (mutation.type === 'childList') {
            for (const node of mutation.addedNodes) {
                if (node.nodeType === Node.ELEMENT_NODE) {
                    if (node.classList && (
                        node.classList.contains('o_colorlist') ||
                        node.classList.contains('o_widget_colorlist') ||
                        node.querySelector('.o_colorlist')
                    )) {
                        applyCustomColors();
                        break;
                    }
                }
            }
        }
    }
});

// Iniciar observer cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        observer.observe(document.body, { childList: true, subtree: true });
    });
} else {
    observer.observe(document.body, { childList: true, subtree: true });
}

registry.category("services").add("colorlist_customizer", {
    start() {
        applyCustomColors();
        return {};
    },
});
