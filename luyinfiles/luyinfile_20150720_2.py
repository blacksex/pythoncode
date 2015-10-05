#-*- coding:utf-8 -*-
#__author__ = 'blackline'
import os
import time
import shutil
def DirCreat(phonenum,curdate):
    dst = "D:/客服录音文件/"
    path = curdate + '/' + phonenum
    newpath = dst  + path
    if not os.path.isdir(newpath):
        os.makedirs(newpath)
    return newpath
def CopyFiles(recordnum,srcDir,dstDir):
  #  os.chdir(srcDir)
    count=0
    for root, dirs, files in os.walk(srcDir, True):
        if - 1 != root.find(recordnum):   #路径名中是否存在要查找的字符
            print(root)
        for item in files:
             path = os.path.join(root, item)
             if - 1 != path.find(recordnum):         #文件列表中是否有要查找的字符
               # print(path.find(src))
                count=count+1
                print(path)
                filename=os.path.basename(path)
                destpath=dstDir+'/'+filename
                shutil.copyfile(path,destpath)
curdate = time.strftime("%Y%m%d")
fjhnum = ['8038','8039','8050','8068','8049','8051','8052','8072']
#print(destdir)
sourcedir = "D:/om录音软件/pbxrecord/"+ curdate+'/'
#sourcedir = sourcedir + curdate
for num in fjhnum:
    destdir = DirCreat(num,curdate)
    CopyFiles(num,sourcedir,destdir)
    if not os.listdir(destdir):
        os.rmdir(destdir)




