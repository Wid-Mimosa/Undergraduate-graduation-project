import matplotlib.pyplot as plt
import time



while (1):

    plt.figure(figsize=(12,7))
    plt.xlabel('Time')
    plt.ylabel('percent')
    fCpu = open('/home/ubuntu/PycharmProjects/untitled/untitled/cpu', 'r')

    cpuUsage = []
    cpuTime = []
    cpuName = []
    cpuNameValue = []
    cnt = 0

    for line in fCpu:
        cpuUsage.append(line.split()[1])
        cpuTime.append(cnt)
        if(cnt % 5 == 0):
            cpuName.append(line.split()[0])
            cpuNameValue.append(cnt)
        cnt += 1
    fCpu.close()

    plt.plot(cpuTime,cpuUsage,'b',label='CPU')
    plt.xticks(cpuNameValue,cpuName)


    fCpu = open('/home/ubuntu/PycharmProjects/untitled/untitled/memory', 'r')

    cpuUsage = []
    cpuTime = []
    cpuName = []
    cpuNameValue = []
    cnt = 0

    for line in fCpu:
        cpuUsage.append(float(line.split()[1]) * 100)
        cpuTime.append(cnt)
        if(cnt % 10 == 0):
            cpuName.append(line.split()[0])
            cpuNameValue.append(cnt)
        cnt += 1
    fCpu.close()

    plt.plot(cpuTime,cpuUsage,'r',label = 'Memory')
    plt.xticks(cpuNameValue,cpuName,)
    plt.xticks(rotation='45')
    plt.legend()

    plt.savefig('/home/ubuntu/PycharmProjects/untitled/Hadoopweb/static/img/cpu')
    plt.close()
    time.sleep(30)
