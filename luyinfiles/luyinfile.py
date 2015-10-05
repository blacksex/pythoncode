#-*- coding:utf-8 -*-
#__author__ = 'blackline'
import os
import time
import shutil
#import sys
#import string
def DirCreat(phonenum,curdate):
    dst = "E:/客服录音文件/"
    path = curdate + '/' + phonenum
    newpath = dst  + path
    if not os.path.isdir(newpath):
        os.makedirs(newpath)
    return newpath

def CopyFiles(recordnum,srcDir,dstDir):
  #  os.chdir(srcDir)
    count=0
    for root,dirs,files in os.walk(srcDir,True):
       print(root)
       for items in files:
            tmppath = os.path.join(root,items)
            if - 1 != tmppath.find(recordnum):
                count = count + 1
                path = os.path.basename(tmppath)
                destpath = dstDir+'/'+path
                shutil.copyfile(items,destpath)
   # print(count)




#    for root, dirs, files in os.walk(srcDir, True):
#        if - 1 != root.find(recordnum):   #路径名中是否存在要查找的字符
#            print(root)
#        for item in files:
#             path = os.path.join(root, item)
#             if - 1 != path.find(recordnum):         #文件列表中是否有要查找的字符
#               # print(path.find(src))
#                count=count+1
#                print(path)
#                filename=os.path.basename(path)
#                destpath=dstDir+'/'+filename
#                shutil.copyfile(path,destpath)



curdate = time.strftime("%Y-%m-%d")
fjhnum = ['Distance_6','Distance_7','Distance_8','Distance_9']
#print(destdir)
sourcedir = "D:/OE录音/"+ curdate+'/'
#sourcedir = sourcedir + curdate
for num in fjhnum:
    destdir = DirCreat(num,curdate)
    CopyFiles(num,sourcedir,destdir)




