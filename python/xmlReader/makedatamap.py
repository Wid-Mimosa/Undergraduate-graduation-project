import random
import os

f = open('E:\\python\\xmlReader\\textinput','w')

for i in range(0,100):
    f.write("-Dmapreduce.task.io.sort.mb=" + str(random.randrange(0, 601)) + ' ')
    # sortpercent
    f.write("-Dmapreduce.map.sort.spill.percent=" + str(random.random()) + ' ')
    # iofactor
    f.write("-Dmapreduce.task.io.sort.factor=" + str(random.randrange(0, 91)) + '\n')

