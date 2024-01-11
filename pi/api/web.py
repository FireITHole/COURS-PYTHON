from flask import Flask, render_template, request
from flask_cors import CORS
import RPi.GPIO as GPIO
import atexit


app = Flask(__name__)
CORS(app)

led_pin = 23
button_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led_pin, GPIO.LOW)


def getLedStatus() -> str:
    return "ON" if GPIO.input(led_pin) == GPIO.HIGH else "OFF"


def getButtonStatus() -> str:
    return "PRESSED" if GPIO.input(button_pin) == GPIO.LOW else "RELEASED"


def toggleLed() -> None:
    if getLedStatus() == "ON":
        GPIO.output(led_pin, GPIO.LOW)
    else:
        GPIO.output(led_pin, GPIO.HIGH)


@app.route("/", methods=["GET", "POST"])
def indexRoute():
    match request.method:
        case "GET":
            return render_template(
                "index.html", led_status=getLedStatus(), button_status=getButtonStatus()
            )
        case "POST":
            toggleLed()
            return render_template(
                "index.html", led_status=getLedStatus(), button_status=getButtonStatus()
            )


@app.route("/button")
def buttonRoute():
    return (
        {"status": getButtonStatus()},
        200,
        {"Content-Type": "application/json"},
    )


@app.route("/led", methods=["GET", "POST"])
def ledRoute():
    match request.method:
        case "GET":
            return (
                {"status": getLedStatus()},
                200,
                {"Content-Type": "application/json"},
            )
        case "POST":
            toggleLed()
            return (
                {"status": getLedStatus()},
                200,
                {"Content-Type": "application/json"},
            )


atexit.register(GPIO.cleanup)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
