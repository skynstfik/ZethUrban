// Carrito de compras
async function agregarAlCarrito(productoId) {
    try {
        const res = await fetch('/agregar_carrito', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: productoId })
        });
        const data = await res.json();
        if (data.success) {
            document.getElementById('cart-count').textContent = data.total_items;
            mostrarToast('¡Producto agregado al carrito!');
        }
    } catch (e) {
        console.error('Error al agregar:', e);
    }
}

async function eliminarItem(productoId) {
    try {
        const res = await fetch('/eliminar_carrito', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: productoId })
        });
        const data = await res.json();
        if (data.success) {
            const el = document.getElementById(`item-${productoId}`);
            if (el) el.remove();
            document.getElementById('cart-count').textContent = data.total_items;
            const totalEl = document.getElementById('total-precio');
            const totalFinalEl = document.getElementById('total-final');
            if (totalEl) totalEl.textContent = `$${data.total.toLocaleString('es-CL')}`;
            if (totalFinalEl) totalFinalEl.textContent = `$${data.total.toLocaleString('es-CL')}`;
            if (data.total_items === 0) location.reload();
        }
    } catch (e) {
        console.error('Error al eliminar:', e);
    }
}

// Toast notification
function mostrarToast(mensaje) {
    let toast = document.querySelector('.toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.textContent = mensaje;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
}

// Menú mobile
function toggleMenu() {
    const menu = document.getElementById('mobile-menu');
    menu.classList.toggle('open');
}

// Inicializar contador del carrito
async function initCart() {
    try {
        const res = await fetch('/carrito');
        // El conteo viene del HTML directo del servidor
    } catch(e) {}
}
