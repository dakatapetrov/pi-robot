import RPi.GPIO as GPIO

class GpioService(object):
    GPIO.setmode(GPIO.BOARD)

    def __init__(self, pin1, pin2):
        self.pin1 = pin1
        self.pin2 = pin2

    def init(self):
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        self.pin1_state = False
        self.pin2_state = False

    def first_on(self):
        GPIO.output(self.pin1, True)
        self.pin1_state = True

    def first_off(self):
        GPIO.output(self.pin1, False)
        self.pin1_state = False

    def first_switch(self):
        self.pin1_state = not self.pin1_state
        GPIO.output(self.pin1, self.pin1_state)

    def second_on(self):
        GPIO.output(self.pin2, True)
        self.pin2_state = True

    def second_off(self):
        GPIO.output(self.pin2, False)
        self.pin2_state = False

    def second_switch(self):
        self.pin1_state = not self.pin1_state
        GPIO.output(self.pin1, self.pin1_state)

    def first_only(self):
        self.first_on()
        self.second_off()

    def second_only(self):
        self.first_off()
        self.second_on()

    def on(self):
        self.first_on()
        self.second_on()

    def off(self):
        self.first_off()
        self.second_off()

    def switch(self):
        self.first_switch()
        self.second_switch()
