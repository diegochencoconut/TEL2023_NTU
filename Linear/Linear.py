from nonblocking_delay import delayMicroseconds
import lgpio
import time

class Linear:
    def __init__(self, red_pin, black_pin):
        self.red_pin = red_pin
        self.black_pin = black_pin

        self.handle = lgpio.gpiochip_open(0)
        lgpio.group_claim_output(self.handle, [red_pin, black_pin])
        
    def __del__(self):
        lgpio.group_free(self.handle, self.red_pin)

    def pushup(self):
        lgpio.group_write(self.handle, self.red_pin, 1)

    def pulldown(self):
        lgpio.group_write(self.handle, self.red_pin, 2)

    def stop(self):
        lgpio.group_write(self.handle, self.red_pin, 0)


linear_motor = Linear(19, 26)

start = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
end = time.clock_gettime_ns(time.CLOCK_BOOTTIME)

while (end - start) < 4000000000:
    end = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    linear_motor.pushup()
start = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
end = time.clock_gettime_ns(time.CLOCK_BOOTTIME)

while (end - start) < 3000000000:
    end = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    linear_motor.pulldown()
linear_motor.stop()
del linear_motor
