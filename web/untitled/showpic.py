import shutil
import matplotlib.pyplot as plt
import time
import os

def show(mapTime,mapCount,reduceTime,reduceCount,filename):
    plt.figure()
    st = 0
    cnt = 0
    mapTime = float(mapTime)
    mapCount = float(mapCount)
    reduceTime = float(reduceTime)
    reduceCount = float(reduceCount)
    for i in range(0,int(mapCount)):
        tmpx = [st,st + mapTime]
        tmpy = [cnt,cnt]
        plt.plot(tmpx,tmpy,'b')
        cnt += 1
        if(cnt > 70):
            cnt = 0
            st += mapTime + 1
    if(cnt != 0):
        st += mapTime
    mapEndTime = st
    st += 6
    cnt = 0
    reduceStartTime = st
    for i in range(0,int(reduceCount)):
        tmpx = [st, st + reduceTime]
        tmpy = [cnt, cnt]
        plt.plot(tmpx, tmpy, 'r')
        cnt += 2
        if (cnt > 71):
            cnt = 0
            st += reduceTime + 1
    if (cnt != 0):
        st += reduceTime
    yValue = ['sist02', 'sist03', 'sist05', 'sist17', 'sist19', 'sist20', 'sist21', 'sist22', 'sist23']
    xValue = [4, 12, 20, 28, 36, 44, 52, 60, 68]

    plt.yticks(xValue, yValue)
    #plt.legend()
    plt.savefig('/home/ubuntu/PycharmProjects/untitled/Hadoopweb/static/img/'+filename+'.png')
    plt.close()

    reduceEndTime = st

def removeLine(filename, lineno):
    fro = open(filename, "r")

    current_line = 0
    while current_line < lineno:
        fro.readline()
        current_line += 1

    seekpoint = fro.tell()
    frw = open(filename, "r+")
    frw.seek(seekpoint, 0)

    # read the line we want to discard
    fro.readline()

    # now move the rest of the lines in the file
    # one line back
    chars = fro.readline()
    while chars:
        frw.writelines(chars)
        chars = fro.readline()

    fro.close()
    frw.truncate()
    frw.close()

while (1):

    f = open('/home/ubuntu/PycharmProjects/untitled/untitled/showpic','r');
    str = f.readline()
    print str.__len__()
    if(str.__len__()):
        show(str.split()[0],str.split()[1],str.split()[2],str.split()[3],str.split()[4])
        f.close()
        removeLine('/home/ubuntu/PycharmProjects/untitled/untitled/showpic',0)

    time.sleep(5)
