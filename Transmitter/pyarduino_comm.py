# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 14:10:35 2023

@author: Marc Arvie
"""

from pyfirmata import Arduino
import numpy as np
import time

 # Decimal to 8-bit string/array
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
    # for element in data:
        
    # while True:
        # Sample for blinking LED
        # value_ = str(value)
        # value_ = value_.encode('ascii')
        # # time_b = time.perf_counter() - time_anew
        # ser.write(value_)
        # time_b = time.perf_counter() - start
            self.led2.write(element)
            print(element)
            # ser.readline()
            time.sleep(self.period)
        
        self.led1.write(0)
        self.led2.write(0)
    
    
    # pin_7.write(1)
    # pin_13.write(1)
    # tot = time.perf_counter() - start
    # board.digital[12].write(1)
    # board.digital[4].write(1)
    
    
    
    
    
    
        self.board.sp.close()
# print(tot)