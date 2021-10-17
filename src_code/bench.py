# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-15 17:47:44
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-17 17:46:27
import random
import time

class bench:

    def __init__(self):
        self.numbers = []    # creates a new empty list

    def __init__(self, count, start, stop):
        self.numbers = []    # creates a new empty list
        self.createRandoms(count,start,stop)

    def createRandoms(self, count, start, stop):
        
        for x in range(count):
            self.numbers.append(random.SystemRandom().uniform(start, stop))  # random.randrange(start, stop))
    # get fct:
    def getNumbers(self):
        return self.numbers

    def getSorted(self):
        return sorted(self.numbers)


class stopWatch:

    def __init__(self):
        self.startTime=0
        self.stopTime=0
        self.name = ""

    def __init__(self, name):
        self.startTime=0
        self.stopTime=0
        self.name = name    

    def start(self):
        self.startTime=time.time()
        return 0

    def stop(self):
        self.stopTime=time.time()
        return self.getRuntime()
        
    def getRuntime(self):
        return (self.stopTime-self.startTime)

    def print(self):
        print('Stop Watch: "%s" runs for %.2f seconds' %(self.name , self.getRuntime()))    


