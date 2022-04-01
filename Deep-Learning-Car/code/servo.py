#import RPi.GPIO as GPIO
import pigpio


class servo_motor ():
    def __init__(self):
        self.servo = 13
        self.pwm = pigpio.pi() 
        self.pwm.set_mode(self.servo, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency( self.servo, 50 )

    def spin(self, val):
        value = (val*11.1111111) + 500
        self.pwm.set_servo_pulsewidth( self.servo, value)
        return None

    
