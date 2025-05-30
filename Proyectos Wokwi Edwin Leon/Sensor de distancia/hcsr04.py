
from machine import time_pulse_us
from machine import Pin
import time

class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=30000):
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)
        self.echo_timeout_us = echo_timeout_us

    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:  # ETIMEDOUT
                raise OSError('Out of range')
            raise ex

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return round(cms, 2)

    def distance_mm(self):
        pulse_time = self._send_pulse_and_wait()
        mms = (pulse_time / 2) / 2.91
        return round(mms, 1)
