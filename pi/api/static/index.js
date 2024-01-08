async function checkButtonStatus() {
    const response = await fetch("/button");
    const button_status = await response.json();
    document.querySelector("#button_status").innerHTML = button_status.status
}

async function toggleLed() {
    const response = await fetch("/led", { method: "POST" });
    const led_status = await response.json();
    document.querySelector("#led_status").innerHTML = led_status.status;
}

setInterval(checkButtonStatus, 100);