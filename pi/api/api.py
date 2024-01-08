from flask import Flask, request
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


@app.route("/led", methods=["GET", "POST"])
def ledRoute():
    led_status = "ON" if GPIO.input(led_pin) == GPIO.HIGH else "OFF"
    match request.method:
        case "GET":
            return {"status": led_status}, 200, {"ContentType": "application/json"}
        case "POST":
            if led_status == "ON":
                GPIO.output(led_pin, GPIO.LOW)
            else:
                GPIO.output(led_pin, GPIO.HIGH)

            led_status = "ON" if led_status == "OFF" else "OFF"

            return (
                {"status": led_status},
                200,
                {"Content-Type": "application/json"},
            )


@app.route(
    "/button",
    methods=[
        "GET",
    ],
)
def buttonRoute():
    button_status = "RELEASED" if GPIO.input(button_pin) == GPIO.HIGH else "PRESSED"
    return {"status": button_status}, 200, {"ContentType": "application/json"}


atexit.register(GPIO.cleanup)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
