# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-15 17:47:44
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-17 17:49:50
import threading

from src_code import *
from src_code.bench import bench, stopWatch


# Define a function for the thread
def singleBench(threadName):
    s0 = stopWatch(threadName + " complete")
    s1 = stopWatch(threadName + " creating")
    s2 = stopWatch(threadName + " sorting")
    s0.start()
    s1.start()
    b = bench(1000000,0,1000)
    s1.stop()
    s2.start()
    #print(b.getNumbers())
    b.getSorted()
    s2.stop()
    s0.stop()
    s0.print()
    s1.print()
    s2.print()

# Create two threads
try:
    x1 = threading.Thread(target=singleBench, args=("Thread 1",))
    x2 = threading.Thread(target=singleBench, args=("Thread 2",))
    x1.start()    
    x2.start()
except:
   print ("Error: unable to start thread")
