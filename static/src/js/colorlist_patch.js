// Customize POS - Aplicar colores personalizados
(function() {
    'use strict';
    
    function applyCustomColors() {
        var session = window.odoo && window.odoo.session_info;
        var colors = session && session.customize_pos;
        
        if (!colors) {
            console.log('[CustomizePOS] No colors found in session');
            return;
        }

        var root = document.documentElement;
        for (var i = 0; i < 12; i++) {
            var color = colors['colorlist_' + i];
            if (color) {
                root.style.setProperty('--colorlist-color-' + i, color);
            }
        }

        console.log('[CustomizePOS] Colors applied');
    }

    function waitForOdoo(callback, attempts) {
        attempts = attempts || 0;
        if (attempts > 50) return;
        
        if (window.odoo && window.odoo.session_info) {
            callback();
        } else {
            setTimeout(function() {
                waitForOdoo(callback, attempts + 1);
            }, 100);
        }
    }

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

    setInterval(function() {
        if (document.querySelector('.pos')) {
            applyCustomColors();
        }
    }, 2000);
})();
