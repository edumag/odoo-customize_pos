// Colorlist Customizer - Aplicar colores personalizados
// Este script se ejecuta en el contexto del POS sin usar imports

(function() {
    'use strict';
    
    function applyCustomColors() {
        // Obtener colores de la sesión (window.odoo define session_info)
        var session = window.odoo && window.odoo.session_info;
        var colors = session && session.colorlist_customizer;
        
        if (!colors) {
            console.log('[ColorlistCustomizer] No colors found in session');
            return;
        }

        // Actualizar variables CSS
        var root = document.documentElement;
        for (var i = 0; i < 12; i++) {
            var color = colors['colorlist_' + i];
            if (color) {
                root.style.setProperty('--colorlist-color-' + i, color);
            }
        }

        console.log('[ColorlistCustomizer] Colors applied:', colors);
    }

    // Función para esperar a que odoo esté disponible
    function waitForOdoo(callback) {
        if (window.odoo && window.odoo.session_info) {
            callback();
        } else {
            setTimeout(function() {
                waitForOdoo(callback);
            }, 100);
        }
    }

    // Aplicar cuando el DOM esté listo
    function init() {
        waitForOdoo(function() {
            applyCustomColors();
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Re-aplicar periódicamente por si el POS carga dinámicamente
    setInterval(function() {
        if (document.querySelector('.pos')) {
            applyCustomColors();
        }
    }, 2000);

})();
