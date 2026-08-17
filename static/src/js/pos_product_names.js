// Customize POS - Nombres de productos y categorías en mayúsculas
(function() {
    'use strict';
    
    console.log('[CustomizePOS] Script loaded');
    
    var config = {
        productNamesUppercase: false,
        categoryNamesUppercase: false
    };
    
    function applyStyles() {
        console.log('[CustomizePOS] Applying styles:', config);
        
        var body = document.body;
        if (!body) {
            console.log('[CustomizePOS] No body found');
            return false;
        }
        
        if (config.productNamesUppercase === true) {
            body.classList.add('product-names-uppercase');
            console.log('[CustomizePOS] Product names: ADDED');
        } else {
            body.classList.remove('product-names-uppercase');
            console.log('[CustomizePOS] Product names: removed');
        }
        
        if (config.categoryNamesUppercase === true) {
            body.classList.add('category-names-uppercase');
            console.log('[CustomizePOS] Category names: ADDED');
        } else {
            body.classList.remove('category-names-uppercase');
            console.log('[CustomizePOS] Category names: removed');
        }
        
        return true;
    }
    
    function fetchConfig() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', '/customize_pos/config', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                try {
                    var data = JSON.parse(xhr.responseText);
                    config.productNamesUppercase = data.product_names_uppercase;
                    config.categoryNamesUppercase = data.category_names_uppercase;
                    console.log('[CustomizePOS] Config fetched:', data);
                    applyStyles();
                } catch(e) {
                    console.log('[CustomizePOS] Error parsing config:', e);
                }
            }
        };
        xhr.send();
    }
    
    function init() {
        console.log('[CustomizePOS] Initializing...');
        fetchConfig();
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
    
    setTimeout(function() {
        if (!document.body || !document.body.classList.contains('product-names-uppercase')) {
            console.log('[CustomizePOS] Retrying...');
            fetchConfig();
        }
    }, 3000);
    
    window.customizePosApply = function() {
        fetchConfig();
    };
})();
