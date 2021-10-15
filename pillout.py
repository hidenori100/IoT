import RPi.GPIO as GPIO
import time

led = 17
buzzer = 18
trig = 20
echo = 21

print('start')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def pillout():
    try:
        GPIO.output(buzzer, False)
        GPIO.output(led, False)
        GPIO.output(trig, False)
        time.sleep(0.5)

        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)

        while GPIO.input(echo) == 0:
            pulse_start = time.time()

        while GPIO.input(echo) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print('Distance : ', distance, 'cm')

        if distance <= 10:
            GPIO.output(led, True)
            GPIO.output(buzzer, True)
            time.sleep(0.5)
            GPIO.output(buzzer, False)
            result="약 감지O"


        else:
            GPIO.output(buzzer, False)
            time.sleep(0.3)
            GPIO.output(led, False)
            result="약 감지X"

        return result

    except:
        GPIO.cleanup()


pillout()