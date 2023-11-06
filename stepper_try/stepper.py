import RPi.GPIO as GPIO
import time

def delayMicroseconds(delay_us) -> None:
    start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    # print("start:", start_time)
    while (end_time - start_time) < delay_us * 1000:
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    # print("end  :", end_time)
    # print("interval:", end_time - start_time)

class Stepper:
    # pulse_per_rev should be consistent of setting
    # assume pulse+direction, so SW11=off and SW12=off for MiSUMi driver
    # circuit: PUL+ to pulse pin, PUL- to GND, DIR+ to direction_pin, DIR- to GND
    def __init__(self, pulse_per_rev, pulse_pin, direction_pin, pulse_length_us = 50):
        
        # check if GPIO is initialized
        if GPIO.getmode() != 11:
            GPIO.setmode(GPIO.BCM)

        GPIO.setup(pulse_pin, GPIO.OUT);
        GPIO.setup(direction_pin, GPIO.OUT)

        self.pulse_pin = pulse_pin
        self.direction_pin = direction_pin
        self.pulse_per_rev = pulse_per_rev
        self.pulse_length = pulse_length_us

    def start_rotate(self, angular_speed_rev_min):
        
        # calculate the period between two pin
        us_between_pulse = 60*1000000 / (angular_speed_rev_min * self.pulse_per_rev)
        # print("us_between_pulse: ", us_between_pulse)
        if us_between_pulse > 0:
            GPIO.output(self.direction_pin, GPIO.HIGH)
        else:
            GPIO.output(self.direction_pin, GPIO.LOW)
            us_between_pulse = us_between_pulse * -1

        GPIO.output(self.pulse_pin, GPIO.HIGH)
        delayMicroseconds(self.pulse_length)
        GPIO.output(self.pulse_pin, GPIO.LOW)
        delayMicroseconds(us_between_pulse - self.pulse_length)

    def stop_rotate(self):
        GPIO.output(self.direction_pin, GPIO.LOW)
        GPIO.output(self.pulse_pin, GPIO.LOW)

def main():
    try:
        start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        stepperL = Stepper(400, 20, 21)
        # print("start:", start_time)
        print("CW")
        while (end_time - start_time) < 5000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            stepperL.start_rotate(-15)
        print("CCW")
        while (end_time - start_time) < 10000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            stepperL.start_rotate(15)
        # print("end  :", end_time)
        # print("interval:", end_time - start_time)

        

    except Exception as error:
        print("error!", error)
        GPIO.cleanup()
        exit(1)
    except KeyboardInterrupt:
        print("no error")
        GPIO.cleanup()
        exit(0)

    GPIO.cleanup()

if __name__ == "__main__":
    main()


