# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.http import JsonResponse
import random
import os
import math
import shutil
import time

# Create your views here.
def index(request):
    return render(request,'dashboard.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def preWeb(request):
    return render(request,'preWeb.html')

def preHistory(request):
    return render(request,'preHis.html')

def jobHistory(request):
    return render(request,'jobHistory.html')

def modConfig(request):
    return render(request,'modConfig.html')

def getCpuPic(request):
    randomStr = str(random.randrange(999999999)).rjust(9,str(0))
    print (randomStr)
    shutil.copy('/home/ubuntu/PycharmProjects/untitled/Hadoopweb/static/img/cpu.png','/home/ubuntu/PycharmProjects/untitled/Hadoopweb/static/img/cpu' + randomStr + '.png')
    returnStr = '/static/img/cpu' + randomStr + '.png'
    return JsonResponse(returnStr,safe=False)

def show(mapTime,mapCount,reduceTime,reduceCount):
    f = open('/home/ubuntu/PycharmProjects/untitled/untitled/showpic', 'a')
    strRet = str(random.randrange(999999999)).rjust(9,str(0))
    f.write(str(mapTime) + ' ' + str(mapCount) + ' ' + str(reduceTime) + ' ' + str(reduceCount) + ' ' + strRet + '\n')
    f.close()
    while(os.path.exists('/home/ubuntu/PycharmProjects/untitled/Hadoopweb/static/img/'+strRet+'.png') != True):
        time.sleep(1)
    return strRet

def getPredictTerasort(request):
    mapConfig = []
    reduceConfig = []
    allConfig = []
    for i in range(0,3):
        strname = 'input' + str(i)
        allConfig.append(float(request.GET[strname]))
    for i in range(3,6):
        strname = 'input' + str(i)
        mapConfig.append(float(request.GET[strname]))
    for i in range(6,11):
        strname = 'input' + str(i)
        reduceConfig.append(float(request.GET[strname]))
    K = 5
    for k in range(2,K+1):
        for i in range(0,3):
            mapConfig.append(pow(mapConfig[i],k))
    K = 5
    for k in range(2,K+1):
        for i in range(0,5):
            reduceConfig.append(pow(reduceConfig[i],k))

    print reduceConfig
    pre1c = -0.122546188756
    pre1k = [-0.10186921,-0.12920555,-0.34136253,2.00281455,-0.25951392,
           0.58876442,   0.81739065,   1.07952984,  -7.13820832,   1.76534935,
          -1.22060576, -1.86570857,  -1.19465829,  11.84008983,  -4.89750593,
           1.03962983,   1.83872521,   0.24669356,  -9.3634219,    5.73338349,
          -0.30206354,  -0.6562141,    0.17179084,   2.86510883,  -2.38879589]

    pre2c = 13.7916267837
    pre2k = [   46.7764175,     10.35487709,   70.5924918,   -244.89688553,    51.33619384,
              -274.19937026,   -65.17923449,  -268.37976117,   911.40787858,  -332.08552107,
               645.38861468,   122.72199929,   399.98854891, -1536.50559002,   848.68193623,
              -651.44615741,  -100.62716739,  -242.77278343,  1218.21133135,  -924.40093382,
               234.45777796,    30.98308047,    46.946826,    -371.90667573,   363.9610519 ]
    reducetimek = reducetimec = 0
    for i in range(0,reduceConfig.__len__()):
        reducetimek += pre1k[i] * reduceConfig[i]
        reducetimec += pre2k[i] * reduceConfig[i]
    reducetimek += pre1c
    reducetimec += pre2c
    perReducetime = reducetimec + reducetimek * allConfig[1] / allConfig[2]
    mapNum = math.ceil(allConfig[1] / 128)
    #print show(40,mapNum,perReducetime,allConfig[2])
    return JsonResponse(show(40,mapNum,perReducetime,allConfig[2]),safe=False)

'''

[   46.7764175     10.35487709    70.5924918   -244.89688553    51.33619384
  -274.19937026   -65.17923449  -268.37976117   911.40787858  -332.08552107
   645.38861468   122.72199929   399.98854891 -1536.50559002   848.68193623
  -651.44615741  -100.62716739  -242.77278343  1218.21133135  -924.40093382
   234.45777796    30.98308047    46.946826    -371.90667573   363.9610519 ]
'''

#def getPredictTerasort(request)
'''
1.88418520772
[  0.42226364  -0.18115264  -0.6377934   -7.96744216  -1.21077218
  -1.68583709   2.34050607   1.76665227  10.26821352   4.1324498
   1.90518225  -2.78148766  -0.90570657   0.52957254  -5.13600101
   0.34232102  -0.48766809  -0.74933485  -7.69027809   1.3277363
  -0.9982329    1.22579479   0.3644565    3.24676499   0.7277919 ]
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
-460.328194431
[  -27.91817374    73.97812467   119.29993773  2019.26630644   294.59094953
   222.60029564  -747.05842934  -294.74692228 -2325.21690195  -940.79823389
  -328.268967     855.74788814   103.30802656  -341.96143034  1137.54126081
   -12.13669203   188.05815992    99.47141219  1561.65491895  -289.56014891
   153.98102759  -405.48110871    18.68503456  -479.13299993  -151.03399501]
'''