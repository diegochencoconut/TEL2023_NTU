import RPi.GPIO as GPIO

def pinMode(pin, status):
    if GPIO.getmode() != 11: GPIO.setmode(GPIO.BCM)

    if status=="OUTPUT":    
        GPIO.setup(pin, GPIO.OUT)
        return
    if status=="INPUT":     
        GPIO.setup(pin, GPIO.IN)
        return

def delayMicroseconds(delay_us) -> None:
    start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    
    while (end_time - start_time) < time_interval * 1000:
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)

def digitalWrite(
def setup() -> None:
    pinMode(5, "OUTPUT")

def loop() -> None:
    mode = GPIO.getmode()
    print(mode)

setup()
ITER_LIMIT = 10
i = 0
while (i < ITER_LIMIT):
    loop()
    i = i + 1
GPIO.cleanup()
