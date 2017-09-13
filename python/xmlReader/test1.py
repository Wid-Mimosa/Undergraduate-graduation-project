
import mode
import  sys



f = open('E:\\python\\实验数据及\\input','r')
tmpstd = sys.stdout

f1 = open('E:\\python\\实验数据及\\terasortreduce','w')
sys.stdout = f1

for line in f:
    line = line.strip('\n')
    print(line + '  30')
    print(line + '  60')
    print(line + '  100')
    print(line + '  180')


