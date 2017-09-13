
import matplotlib.pyplot as plt
import xlrd
import numpy as np

#['sist02', 'sist03', 'sist05', 'sist17', 'sist19', 'sist20', 'sist21', 'sist22', 'sist23']
#Y name
yValue = ['sist02', 'sist03', 'sist05', 'sist17', 'sist19', 'sist20', 'sist21', 'sist22', 'sist23']
xValue = [4, 12, 20, 28, 36, 44, 52, 60, 68]

yValueCnt = {};

data = xlrd.open_workbook('E:\\python\\分段收集数据.xlsx')

table1 = data.sheet_by_index(0)
X0 = table1.col_values(10)
X1 = table1.col_values(16)
Y = table1.col_values(11)

st = X0[0] * 3600 * 24

plt.figure()
for each in range(0,X0.__len__()):
    x = []
    x.append(X0[each] * 24 * 3600 - st)
    x.append(X1[each] * 24 * 3600 - st)
    tmp = 'sist'+str(Y[each])
    if(tmp not in yValueCnt):
        yValueCnt[tmp] = yValue.index(tmp) * 8;
    y = [yValueCnt[tmp],yValueCnt[tmp]]
    yValueCnt[tmp] += 1
    if(yValueCnt[tmp] % 8 == 0):
        yValueCnt[tmp] -= 8
    plt.plot(x,y,'g')



cnt = 0
table2 = data.sheet_by_index(1)
X0 = table2.col_values(5)
X1 = table2.col_values(11)
print(X1)
print(X0.__len__())
cnt = 0
for each in range(0,X0.__len__()):
    x = []
    x.append(X0[each] * 24 * 3600 - st)
    x.append(X1[each] * 24 * 3600 - st)
    y = [cnt,cnt]
    cnt += 2;
    if(cnt > 71):
        cnt = 0
    plt.plot(x,y,'')

plt.yticks(xValue,yValue)
plt.show()

