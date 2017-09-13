# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET
import sys
import os

cnt = 0
while(cnt < 100):
    if (os.path.exists('C:\\Users\\WangChi\\Desktop\\hadoop数据集\\数据4-18\\config\\11\\000000\\job_1491833005747_'+str(cnt).rjust(4,'0')+'_conf.xml') == False):
        cnt = cnt+1
        continue

    tree = ET.parse('C:\\Users\\WangChi\\Desktop\\hadoop数据集\\数据4-18\\config\\11\\000000\\job_1491833005747_'+str(cnt).rjust(4,'0')+'_conf.xml')
    root = tree.getroot()

    sys.stdout = open('job_1491833005747_'+str(cnt).rjust(4,'0')+'_conf.out','w')
    cnt=cnt+1
    for child in root:
        for config in child:
            print(config.text,end=' ')