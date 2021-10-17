# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-15 17:47:44
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-17 17:57:21
from multiprocessing import Process

from src_code import *
from src_code.bench import bench, stopWatch


# Define a function for the thread
def singleBench(processName):
    s0 = stopWatch(processName + " complete")
    s1 = stopWatch(processName + " creating")
    s2 = stopWatch(processName + " sorting")
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

# Create two processes
def main():
    p1 = Process(target=singleBench, args=('Process 1',))
    p1.start()    

    p2 = Process(target=singleBench, args=('Process 2',))
    p2.start()    

if __name__ == '__main__':
    main()


