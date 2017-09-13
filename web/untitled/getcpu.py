#    
# Copyright (c) 2014, Lambo Wang, All rights reserved.    
# Use of this source code is governed by a GNU v2 license that can be    
# found in the LICENSE file.    
#   
# Logs:  
# Transplant to NT system by Lambo Wang, 2012-11-28    
# Add function of get cpu state and get memory state by Lambo Wang,2012-11-29    
# first add to Git of OSChina,2014-10-24 by Lambo Wang   
"""  
Shows real-time NT system statistics.  
Author: Lambo Wang <lambo.wang@icloud.com>  
"""

import sys
import psutil
import datetime
import os

cnt = 0

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

while 1:

    if(cnt > 150):
        removeLine('/home/ubuntu/PycharmProjects/untitled/untitled/cpu',0)
        removeLine('/home/ubuntu/PycharmProjects/untitled/untitled/memory',0)


    cpu = str(psutil.cpu_percent(interval=10))
    f = open('/home/ubuntu/PycharmProjects/untitled/untitled/cpu', 'a')
    f.write(datetime.datetime.now().strftime('%H:%M:%S') + "  " + cpu + '\n')
    f.close()

    print (cnt)

    f1 = open('/home/ubuntu/PycharmProjects/untitled/untitled/memory', 'a')
    f1.write(datetime.datetime.now().strftime('%H:%M:%S')+ '  ')
    f1.write(str(1 - psutil.virtual_memory().available * 1.0 / psutil.virtual_memory().total) + '\n')
    f1.close()

    cnt += 1


