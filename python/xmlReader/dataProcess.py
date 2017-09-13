import os
import sys

def work(x):
    if(x == 'mapreduce.job.jar'):
        return False
    if(x == 'mapreduce.job.cache.files.timestamps'):
        return False
    if(x == 'mapreduce.input.fileinputformat.inputdir'):
        return False
    if(x == 'mapreduce.job.cache.files'):
        return False
    if(x == 'mapreduce.output.fileoutputformat.outputdir'):
        return False
    if(x == 'mapreduce.job.dir'):
        return False

    #手动删除数量
    if(x == 'mapreduce.input.fileinputformat.numinputfiles'):
        return False
    if(x == 'mapreduce.job.inputformat.class'):
        return False
    if(x == 'mapreduce.job.cache.files.filesizes'):
        return False
    if(x == 'io.sort.record.percent'):
        return False
    if(x == 'min.num.spill.for.combine'):
        return False
    if(x == 'mapreduce.terasort.num-rows'):
        return False
    if(x == 'mapreduce.reduce.java.opts'):
        return False
    if(x == 'mapreduce.map.java.opts'):
        return False

    if(x == 'mapreduce.reduce.input.buffer.percent'):
        return False

    #怀疑的参数
    if(x == 'mapred.child.java.opts'):
        return False
    return True


AllTestConfig = {}

cntFilename = 0;
cntFoldername = 0;
while(cntFoldername < 100):
    while(cntFilename < 100):
        if (os.path.exists('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\'+str(cntFilename).rjust(4,'0')+'_conf.out') == False):
            cntFilename += 1
            #print('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\job_1491833005747_'+str(cntFilename).rjust(4,'0')+'_conf.out')
            continue
        fp = open('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\'+str(cntFilename).rjust(4,'0')+'_conf.out','r')
        for eachline in fp:
            output = eachline.split()

            if(output[0] not in AllTestConfig):
                AllTestConfig[output[0]] = {}
                #print(AllTestConfig[output[0]])
            if(output[1] not in AllTestConfig[output[0]]):
                AllTestConfig[output[0]][output[1]] = 1
            else:
                AllTestConfig[output[0]][output[1]] += 1
        fp.close()
        #print(cntFilename)
        cntFilename += 1

    cntFoldername += 1
    cntFilename = 0
for key in AllTestConfig.keys():
    if(len(AllTestConfig[key]) > 1 and work(key)):
        print(key,AllTestConfig[key])


cntFilename = 0;
cntFoldername = 0;
cnt = 0
fpForW = open('E:\\python\\xmlReader\\InputData.csv','w')
while(cntFoldername < 100):
    while(cntFilename < 100):
        if (os.path.exists('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\'+str(cntFilename).rjust(4,'0')+'_conf.out') == False):
            cntFilename += 1
            #print('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\job_1491833005747_'+str(cntFilename).rjust(4,'0')+'_conf.out')
            continue
        fp = open('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\'+str(cntFilename).rjust(4,'0')+'_conf.out','r')
        #fpForW.write(str(cntFoldername) + "_" + str(cntFilename) + "\n")
        if(cnt == 0):
            for eachline in fp:
                output = eachline.split()
                if (len(AllTestConfig[output[0]]) > 1 and work(output[0])):
                    fpForW.write(output[0] + " ")
            fpForW.write("NumberOfTest\n")
            cnt += 1
        fp.close()
        fp = open('E:\\python\\xmlReader\\'+str(cntFoldername).rjust(2,'0')+'\\'+str(cntFilename).rjust(4,'0')+'_conf.out','r')
        for eachline in fp:
            output = eachline.split()
            if (len(AllTestConfig[output[0]]) > 1 and work(output[0])):
                fpForW.write(output[1] + " ")
        fpForW.write(str(cntFoldername) + "_" + str(cntFilename) + "\n")
        fp.close()

       #print(cntFilename)
        cntFilename += 1

    cntFoldername += 1
    cntFilename = 0
fpForW.close()