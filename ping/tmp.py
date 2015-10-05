__author__ = 'blackline'
import time
import urllib.request
url1 = "http://180.166.148.176:16913/tradeweb/probe.jsp"
url2 = "https://180.166.148.176:16914/tradeweb/probe.jsp"
while(1):
    filelog1 = open('D:/16913/jcresultlog.txt','a+')
    curtime = time.strftime("%Y-%m-%d_%H:%M:%S")
    content11 = curtime + ":  16913 is OK" + "\n"
    content12 = curtime + ":  16913 is ERROR"+ "\n"
    content21 = curtime + ":  16914 is OK" + "\n"
    content22 = curtime + ":  16914 is ERROR"+ "\n"
    req1 = urllib.request.urlopen(url1)
    res1 = req1.getcode()
    req2 = urllib.request.urlopen(url2)
    res2 = req2.getcode()
    if res1 == 200:
        print ("%s: 16913 is ok"%(curtime))
        filelog1.write(content11)
    else:
        print("%s:ERROR"%(curtime))
        filelog1.write(content12)
    if res2 == 200:
        print ("%s: 16914 is ok"%(curtime))
        filelog1.write(content21)
    else:
        print("%s:ERROR"%(curtime))
        filelog1.write(content22)
    filelog1.close()
    time.sleep(60)
filelog1.close()

