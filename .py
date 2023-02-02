import pigpio
from time import sleep

def interrupt_handler(gpio, level, tick):
    print("Interrupt detected on GPIO", gpio)

pi = pigpio.pi()
pi.set_mode(17, pigpio.INPUT)
pi.set_pull_up_down(17, pigpio.PUD_UP)
cb = pi.callback(17, pigpio.FALLING_EDGE, interrupt_handler)

# The program will now run and wait for the interrupt
while True:
    print("While is Running   !!!!!!")
    
    pass
