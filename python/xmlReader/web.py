from urllib import request
import re
import sys

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html

f = open('E:\\python\\实验数据及\\519terasortmap.txt','w')

tmp = sys.stdout

sys.stdout = f

for i in range(413,513):
    numStr = str(i).rjust(4,'0')
    html = getHtml("http://192.168.130.56:19888/jobhistory/job/job_1494728058968_" + numStr)
    reg = r'Elapsed:[\s\S]*?</table>'
    configre = re.compile(reg)
    configlist = re.findall(configre,html)
    print(configlist,end='')
    print(' ' + str(i))

sys.stdout = tmp
f.close()