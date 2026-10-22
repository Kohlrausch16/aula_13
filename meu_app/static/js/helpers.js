function toggleOrder() {
    const params = new URLSearchParams(window.location.search);
    const ordem = params.get('ordem');

    const crescente = document.querySelector('.icon-crescente');
    const decrescente = document.querySelector('.icon-decrescente');

    crescente.style.display = ordem === 'crescente' ? 'none' : 'inline';
    decrescente.style.display = ordem === 'crescente' ? 'inline' : 'none';
}

document.addEventListener('DOMContentLoaded', toggleOrder);
