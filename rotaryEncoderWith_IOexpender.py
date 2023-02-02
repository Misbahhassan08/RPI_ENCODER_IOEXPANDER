import pcf8574_io
import threading
import pigpio

class PCF8574(threading.Thread):
    p1 = pcf8574_io.PCF(0x20)
    def __init__(self):
        threading.Thread.__init__(self)
        self.encoderPinA = "p0"
        self.encoderPinB = "p1"
        self.encoderButton = "p2"
        self.inputmode = "INPUT"
        self.encoderValue = 0
        self.encoderButtonVal = 1    # encoder button value set high
        self.encoderPinALast = 0
        self.valPrecEncoderButton = 0
        self.change = False
        self.p1.pin_mode(self.encoderPinA,self.inputmode)
        self.p1.pin_mode(self.encoderPinB,self.inputmode)
        self.p1.pin_mode(self.encoderButton,self.inputmode)
        pass   # end of pcf8574 constructor
    def get(self):
        return self.encoderValue
    def loop(self):
        if self.change:
            print(f"ENCODER --> {self.encoderValue}")
            print(f" - BUTTON --> {self.encoderButtonVal}")
            self.change = False
        pass   # end of loop function
    def updateEncoder(self):
        n = self.p1.read(self.encoderPinA)
        if (self.encoderPinALast == 0) and (n==1):
            if self.p1.read(self.encoderPinB) == 0:
                self.encoderValue -= 1  
                self.change = True  # change the value
            else:
                self.encoderValue += 1
                self.change = True  # change the value
        self.encoderPinALast = n
        # Button managment
        self.encoderButtonVal = self.p1.read(self.encoderButton)
        if self.encoderButtonVal != self.valPrecEncoderButton:
            change = True   # change the value of button
            self.valPrecEncoderButton = self.encoderButtonVal
        pass   # end of updateEncoder function
    def run(self):
        while True:
            self.loop()
            self.updateEncoder()
        pass    # end of run function
    pass   # end of pcf8574 main class

if __name__ == "__main__":
    pcf = PCF8574()
    pcf.start()