// Fonction récupérant l'état actuel du bouton
async function checkButtonStatus() {
    const response = await fetch("/button");
    const button_status = await response.json();
    document.querySelector("#button_status").innerHTML = button_status.status
}

// Fonction changeant l'état de la LED
async function toggleLed() {
    const response = await fetch("/led", { method: "POST" });
    const led_status = await response.json();
    document.querySelector("#led_status").innerHTML = led_status.status;
}

// On appelle la fonction une fois toutes les 100 millisecondes
setInterval(checkButtonStatus, 100);

// Permet de ne pas soumettre une nouvelle fois la form lors d'une actualisation de page
if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}