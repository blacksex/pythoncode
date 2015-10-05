#!/usr/bin/env python
#__author__ = 'hanlong'
#2015-08-06
import os
import os.path
import hashlib
import string

def calmd5(files):
    m = hashlib.md5()
    a_file = open(files,'rb')
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
def searchdir(ipadd):
    os.chdir("/root/shell")
    curd = os.getcwd()
    fn = curd + '/' + ipadd.strip() + '.md5.txt'
    md5file = open(fn,'a+')
    os.popen("find /root/shell > tmp.txt")
    file = open('tmp.txt','rb')
    line = file.readline()
    while line:
        linetmp = line.strip('\n')
        if not os.path.isdir(linetmp):
            md5num = calmd5(linetmp)
            fcontent = md5num + "  " + line
            md5file.write(fcontent)
        line = file.readline()
if __name__ == "__main__":
    ips = os.popen("hostname -I").read().strip('\n')
    print (ips)
    searchdir(ips)

