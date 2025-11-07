from pyfirmata import Arduino
import numpy as np
import time

# Decimal to 8−bit string/array
def dectobyte(number):
    array = []
    for index in range(8):
        quotient = number % 2
        number = number // 2
        array.append(quotient)
    return np.flip(np.array(array))
 
class info_transfer:
    def __init__(self, port, number):
        self.number = number
        self.board = Arduino(port)
        self.period = 1.5
        
        self.led1 = self.board.digital[11]
        self.led2 = self.board.digital[12]
        
        self.array = dectobyte(self.number)

def run(self):
    self.value = 1
    self.led1.write(1)
    time.sleep(2)

    for element in self.array:
        self.led2.write(element)
        print(element)
        time.sleep(self.period)
    
    self.led1.write(0)
    self.led2.write(0)
    
    self.board.sp.close()