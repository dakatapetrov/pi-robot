from pi_robot.gpio_service import GpioService

class MovementService(object):
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def move_left(self):
        print 'moving left'
        self.left_motor.second_only()
        self.right_motor.first_only()

    def move_right(self):
        print 'moving right'
        self.left_motor.first_only()
        self.right_motor.second_only()

    def move_front(self):
        print 'moving front'
        self.left_motor.first_only()
        self.right_motor.first_only()

    def move_back(self):
        print 'moving back'
        self.left_motor.second_only()
        self.right_motor.second_only()

    def stop(self):
        print 'stop'
        self.left_motor.off()
        self.right_motor.off()
