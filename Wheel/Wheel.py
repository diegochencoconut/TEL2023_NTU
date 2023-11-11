from nonblocking_delay import delayMicroseconds
import lgpio
import time

class Wheel:
    def __init__(self, left_frontwheel_RPWM,   left_frontwheel_LPWM,
                       right_frontwheel_RPWM,  right_frontwheel_LPWM,
                       left_backwheel_RPWM,    left_backwheel_LPWM,
                       right_backwheel_RPWM,   right_backwheel_LPWM,
                       PWM_period = 5000, PWM_full = 100, PWM_zero = 0, PWM_factor = 1):

        self.PWM_period = PWM_period
        self.PWM_full = PWM_full
        self.PWM_zero = PWM_zero
        self.PWM_factor = PWM_factor

        self.left_frontwheel_forward_pin = left_frontwheel_LPWM
        self.left_frontwheel_backward_pin = left_frontwheel_RPWM

        self.right_frontwheel_forward_pin = right_frontwheel_RPWM
        self.right_frontwheel_backward_pin = right_frontwheel_LPWM
    
        self.left_backwheel_forward_pin = left_backwheel_LPWM
        self.left_backwheel_backward_pin = left_backwheel_RPWM
    
        self.right_backwheel_forward_pin = right_backwheel_RPWM
        self.right_backwheel_backward_pin = right_backwheel_LPWM

        self.pins = [self.left_frontwheel_forward_pin,
                     self.left_frontwheel_backward_pin,
                     self.right_frontwheel_forward_pin,
                     self.right_frontwheel_backward_pin,
                     self.left_backwheel_forward_pin,
                     self.left_backwheel_backward_pin,
                     self.right_backwheel_forward_pin,
                     self.right_backwheel_backward_pin]

        self.handle = lgpio.gpiochip_open(0)
        lgpio.group_claim_output(self.handle, self.pins)
        self.group_leader = self.left_frontwheel_forward_pin
       
    def __del__(self):
        lgpio.group_free(self.handle, self.group_leader)

    def PWMoutput(self, speed, PWMdata):
        PWM_holdup = self.PWM_period * (speed - self.PWM_zero) / (self.PWM_full - self.PWM_zero)
        PWM_holdup = PWM_holdup * self.PWM_factor
        lgpio.group_write(self.handle, self.group_leader, PWMdata)
        delayMicroseconds(PWM_holdup)
        lgpio.group_write(self.handle, self.group_leader, 0)
        delayMicroseconds(self.PWM_period - PWM_holdup)

    def stop(self):
        lgpio.group_write(self.handle, self.group_leader, 0)

    def forward(self, speed):
        levels = 0b10101010
        self.PWMoutput(speed, levels)
 
    def backward(self, speed):
        levels = 0b01010101
        self.PWMoutput(speed, levels)

    def leftside(self, speed):
        levels = 0b01101001
        self.PWMoutput(speed, levels)

    def rightside(self, speed):
        levels = 0b10010110
        self.PWMoutput(speed, levels)     


def main():
    test = Wheel(5, 6, 12, 16, 13, 19, 20, 21)
    try:
        start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
    
        while (end_time - start_time) < 6000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            test.forward(50)
        
        start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        while (end_time - start_time) < 6000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            test.backward(50)
        
        start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        while (end_time - start_time) < 6000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            test.forward(50)
        
        start_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
        while (end_time - start_time) < 6000000000:
            end_time = time.clock_gettime_ns(time.CLOCK_BOOTTIME)
            test.backward(50)

    except Exception as e:
        test.stop()
        del test

    except KeyboardInterrupt:
        test.stop()
        del test

        
if __name__ == "__main__":
    main()
''' 
        self.forward_pin = [self.left_frontwheel_forward_pin,
                            self.left_backwheel_forward_pin,
                            self.right_frontwheel_forward_pin,
                            self.right_backwheel_forward_pin]

        self.backward_pin = [self.left_frontwheel_backward_pin,
                             self.left_backwheel_backward_pin,
                             self.right_frontwheel_backward_pin,
                             self.right_backwheel_backward_pin]

        self.left_forward_pin = [self.left_frontwheel_forward_pin,
                                 self.left_backwheel_forward_pin]

        self.left_backward_pin = [self.left_frontwheel_backward_pin,
                                  self.left_backwheel_backward_pin]

        self.right_forward_pin = [self.right_frontwheel_forward_pin,
                                  self.right_backwheel_forward_pin]
        
        self.right_backward_pin = [self.right_frontwheel_backward_pin,
                                   self.right_backwheel_backward_pin]

        self.frontwheel_forward_pin = [self.left_frontwheel_forward_pin,
                                       self.right_frontwheel_forward_pin]

        self.frontwheel_backward_pin = [self.left_frontwheel_backward_pin,
                                        self.right_frontwheel_backward_pin]

        self.backwheel_forward_pin = [self.left_backwheel_forward_pin,
                                      self.right_backwheel_forward_pin]

        self.backwheel_backward_pin = [self.left_backwheel_backward_pin,
                                       self.right_backwheel_backward_pin]
''' 
