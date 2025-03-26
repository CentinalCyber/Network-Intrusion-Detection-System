import RPi.GPIO as GPIO
import time
import subprocess

# GPIO Pin Definitions
LED_PIN = 17     # LED output
BUZZER_PIN = 27  # Buzzer output

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# Function to simulate attack detection using ping
def detect_attack():
    result = subprocess.run(["ping", "-c", "1", "10.0.0.97"], capture_output=True, text=True)
    print(f"Ping result:\n{result.stdout}")
    return "1 packets transmitted, 1 received" in result.stdout

# Blink LED function
def blink_led(duration=10, interval=0.5):
    end_time = time.time() + duration
    while time.time() < end_time:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(interval)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(interval)

# Beep buzzer briefly
def beep_buzzer(duration=0.2):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

# Main loop
attack_detected = False

try:
    while True:
        if detect_attack() and not attack_detected:
            print("⚠️ Attack detected! Activating alert...")
            attack_detected = True

            # Sound buzzer briefly
            beep_buzzer()

            # Turn LED ON for 3 seconds
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(LED_PIN, GPIO.LOW)

            # Blink LED
            blink_led(duration=10)

            # Reset alert state
            attack_detected = False

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
