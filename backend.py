from flask import Flask, request, jsonify
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

@app.route('/', methods=['GET'])
def led()
  status = request.args.get('ziemniak')
  if status == 'on':
    GPIO.output(18, GPIO.HIGH)
    return 'Led succesfully turned on'
  elif status == 'off':
    GPIO.output(18, GPIO.HIGH)
    return 'Led succesfully turned off'
   else:
    return 'Not a valid status'
