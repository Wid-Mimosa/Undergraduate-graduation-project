import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import xlrd
import random

def functionreduce1():
    data = xlrd.open_workbook('E:\\python\\实验数据及\\wordcountreduce.xlsx')
    #data = xlrd.open_workbook('E:\\python\\实验数据及\\terasortreduce.xlsx')

    table = data.sheet_by_index(0)
    Y = table.col_values(ord('T') - ord('A'))
    #Y = table.col_values(29)

    YInput = np.array(Y[0:41:2])
    #YInput = np.array(Y[0:30])

    #按照reduce个数对输入进行修改
    X = []
    for i in range(ord('K') - ord('A'), ord('P') - ord('A')):
    #for i in range(ord('U') - ord('A'),ord('Z') - ord('A')):
        #print(i)
        tmp = []
        for j in range(0, 84, 4):
        #for j in range(0,120,4):
            #print(j)
            tmp.append(table.col_values(i)[j])
        X.append(tmp)

    #print(X)
    #计算参数配置 K 次幂
    print(X)
    K = 3
    for k in range(2,K+1):
        for i in range(0,5):
            tmp = []
            for each in X[i]:
                tmp.append(pow(each,k))
            X.append(tmp)

    Xtrain = np.transpose(np.array(X))

    #print(Xtrain)



    linreg = LinearRegression()

    print(Xtrain.shape)
    print(YInput.shape)

    model=linreg.fit(Xtrain, YInput)
    print (model)
    print (linreg.intercept_)
    print (linreg.coef_)

    Y_predict = linreg.predict(Xtrain)
    #evaluate(YInput,Y_predict)

    plt.figure()
    #print(Y_predict)
    #plt.figure().patch.set_facecolor('blue')
    plt.plot(range(len(Y_predict)),Y_predict,'b',linestyle=':',label='predict K')
    plt.plot(range(len(Y_predict)),YInput,'r',label='real K')
    plt.legend()
    plt.xlabel('The Number Of Trial')
    plt.ylabel('The Value Of K In Linear Regression')
    plt.show()
    return linreg

def functionreduce2():
    data = xlrd.open_workbook('E:\\python\\实验数据及\\wordcountreduce.xlsx')
    #data = xlrd.open_workbook('E:\\python\\实验数据及\\terasortreduce.xlsx')

    table = data.sheet_by_index(0)
    Y = table.col_values(ord('U') - ord('A'))
    #Y = table.col_values(30)

    YInput = np.array(Y[0:41:2])
    #YInput = np.array(Y[0:30])

    #按照reduce个数对输入进行修改
    X = []
    for i in range(ord('K') - ord('A'), ord('P') - ord('A')):
    #for i in range(ord('U') - ord('A'),ord('Z') - ord('A')):
        #print(i)
        tmp = []
        for j in range(0, 84, 4):
        #for j in range(0,120,4):
            #print(j)
            tmp.append(table.col_values(i)[j])
        X.append(tmp)

    #print(X)
    #计算参数配置 K 次幂

    K = 3
    for k in range(2,K+1):
        for i in range(0,5):
            tmp = []
            for each in X[i]:
                tmp.append(pow(each,k))
            X.append(tmp)

    Xtrain = np.transpose(np.array(X))

    #print(Xtrain)



    linreg = LinearRegression()

    #print(Xtrain.shape)
    #print(YInput.shape)

    model=linreg.fit(Xtrain, YInput)
    print (model)
    print (linreg.intercept_)
    print (linreg.coef_)


    #print(Xtrain[0])
    Y_predict = linreg.predict(Xtrain)

    evaluate(YInput,Y_predict)

    plt.figure()
    plt.plot(range(len(Y_predict)),Y_predict,'b',linestyle=':',label='predict C')
    plt.plot(range(len(Y_predict)),YInput,'r',label='real C')
    plt.legend()
    plt.xlabel('The Number Of Trial')
    plt.ylabel('The Value Of C In Linear Regression')
    plt.show()
    return linreg

def functionReduceSlope():
    data = xlrd.open_workbook('E:\\python\\实验数据及\\terasortreduce.xlsx')
    table = data.sheet_by_index(0)

    X = table.col_values(26)
    Y = table.col_values(ord('T') - ord('A'))

    plt.figure()

    for i in range(0,120,4):
        XInput = []
        YInput = []
        for j in range(0,4):
            XInput.append(X[i+j])
            YInput.append(Y[i+j])

        cof = np.polyfit(XInput,YInput,1)
        p1 = np.poly1d(cof)
        print(p1)
        plt.plot(XInput,p1(XInput))

    plt.xlabel('The Input File Size of Reduce')
    plt.ylabel('Time')
    plt.show()

def evaluate(Y,Y_predict):
    max = np.max(Y);
    print(max)
    SSE = 0.0
    #print(SSE)
    for i in range(0,len(Y)):
        SSE += pow((Y[i] - Y_predict[i]),2)
        #print(SSE)
    SSE /= pow(max,2)

    print('SSE')
    print(SSE)

    MAPE = 0.0
    for i in range(0,len(Y)):
        MAPE += pow((Y[i] - Y_predict[i]),2) / Y[i]
    MAPE /= len(Y)

    print(MAPE)

    RMSE = pow(MAPE,0.5)

    print(RMSE)

    R2 = 0.0
    a = 0.0
    for i in range(0,len(Y)):
        a += pow((Y[i] - Y_predict[i]),2)
    sum = 0;
    for i in range(0,len(Y)):
        sum += Y[i] / len(Y)
    b = 0.0
    for i in range(0,len(Y)):
        b += Y_predict[i] - sum
    R2 = 1 - a / b
    print(a,sum,b)
    print(R2)

def functionmap():
    data = xlrd.open_workbook('E:\\python\\实验数据及\\wordcountmap.xlsx')

    table = data.sheet_by_index(0)
    Y = table.col_values(4)

    YInput = np.array(Y)

    # 按照个数对输入进行修改
    X = []
    for i in range(0,3):
        X.append(table.col_values(i))

    #print(X)
    K = 5
    for k in range(2, K + 1):
        for i in range(0, 3):
            tmp = []
            for each in X[i]:
                tmp.append(pow(each, k))
            X.append(tmp)

    Xtrain = np.transpose(np.array(X))

    # print(Xtrain)



    linreg = LinearRegression()

    #print(Xtrain.shape)
    #print(YInput.shape)

    model = linreg.fit(Xtrain, YInput)
    #print(model)
    #print(linreg.intercept_)
    #print(linreg.coef_)

    Y_predict = linreg.predict(Xtrain)

    Y_percent =[]

    for i in range(0,YInput.__len__()):
        Y_percent.append(1 - abs(Y_predict[i] - YInput[i]) / YInput[i])

    plt.figure()
    plt.plot(range(len(Y_predict)), Y_predict, 'b',linestyle=':',label='Predict Map Time')
    plt.plot(range(len(Y_predict)), YInput, 'r', label='Real Map Time')
    #plt.plot(range(len(Y_predict)), Y_percent, 'r', label='Accuracy percent')
    plt.legend()
    plt.xlabel('The Number Of Trial')
    plt.ylabel('Time Of Map Process')
    #plt.show()

    return linreg

def predict(map,reduce):

#次数最高K
    K = 5

    len = map.__len__()
    for i in range(2,K+1):
        for j in range(0,len):
            map.append(pow(map[j],i))

    len = reduce.__len__()
    for i in range(2, K + 1):
        for j in range(0, len):
            reduce.append(pow(reduce[j], i))

    mapModel = functionmap()
    reduceModel1 = functionreduce1()
    reduceModel2 = functionreduce2()

    mapinput = np.array(map).reshape(1,-1)
    reduceinput = np.array(reduce).reshape(1,-1)

    mapTime = mapModel.predict(mapinput)
    reduceTime1 = reduceModel1.predict(reduceinput)
    reduceTime2 = reduceModel2.predict(reduceinput)

    time = [mapTime,reduceTime1,reduceTime2]
    print(mapTime,reduceTime1,reduceTime2)

    return time

def work():

    #参数添加
    map = []
    reduce = []

    #iosort
    map.append(random.randrange(0,601) / 600)
    #sortpercent
    map.append(random.random())
    #iofactor
    map.append(random.randrange(0,71) / 70)

    #para
    reduce.append(random.randrange(0,20) / 20)
    #iofactor
    reduce.append(random.randrange(0,91) / 90)
    #shufflebufer
    reduce.append(random.uniform(0.5,0.9))
    #shufflemerge
    reduce.append(random.uniform(0.5,0.9))
    #inputbuffer
    reduce.append(random.uniform(0,0.9))

    #reduce = [0.263157895,0.488888889,0.263155481,0.722194119,0.049734288]

    print(map)
    print(reduce)
    predictTime = predict(map,reduce)

    yValue = ['sist02', 'sist03', 'sist05', 'sist17', 'sist19', 'sist20', 'sist21', 'sist22', 'sist23']
    xValue = [4, 12, 20, 28, 36, 44, 52, 60, 68]


    print('please input num')
    mapNum = int(input())
    reduceNum = int(input())
    print(mapNum,reduceNum)
    plt.figure()
    st = 0
    cnt = 0
    for i in range(0,mapNum):
        tmpx = [st,st + predictTime[0]]
        tmpy = [cnt,cnt]
        plt.plot(tmpx,tmpy,'b')
        cnt += 1
        if(cnt > 71):
            cnt = 0
            st += predictTime[0] + 1
    st += 5
    if(mapNum % 71 != 0):
        st += predictTime[0]
    reduceSize = mapNum * 128 / reduceNum
    perReduceTime = reduceSize * predictTime[1] + predictTime[2]
    cnt = 0

    for i in range(0,reduceNum):
        tmpx = [st, st + perReduceTime]
        tmpy = [cnt,cnt]
        plt.plot(tmpx, tmpy, 'g')
        cnt += 2
        if (cnt > 71):
            cnt = 0
            st += perReduceTime + 1
    if(reduceNum % 31 != 0):
        st += perReduceTime
    print('final time is' + str(st))
    plt.yticks(xValue, yValue)
    plt.show()

work()