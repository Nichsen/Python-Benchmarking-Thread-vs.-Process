# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-15 17:47:44
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-17 17:46:54
from src_code import *
from src_code.bench import bench, stopWatch

s0 = stopWatch("complete")
s1 = stopWatch("creating")
s2 = stopWatch("sorting")
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