#-*- coding:UTF-8 -*-
import paramiko
import string
import os
import sys
import hashlib
#import socket
import Crypto
import ecdsa
import time
#import argparse
def ssh_connect(hostname,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,username,password)
    return ssh

def ssh_disconnect(client):
    client.close()

def put_file(hostname,port,username,password,src,dst):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password,hostkey=None)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(src,dst)
    sftp.close()
    t.close()
def get_file(hostname,port,username,password,src,dst):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    t = paramiko.Transport((hostname,port))
    t.connect(username=username,password=password,hostkey=None)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(src,dst)
    sftp.close()
    t.close()
def mk_dl_dirs(mdir,ssh):
    sftp = paramiko.SFTPClient.from_transport(ssh)
    sftp.mkdir(mdir)

def exec_command(ipadd,ssh):
    '''
    windows客户端远程执行linux
    '''
    command = open('jcshell.txt','r')
    ddir = 'd:/result/'
    dfile = ddir + ipadd + '_jc.txt'
    tmpfile = open(dfile,'a+')
    for line in command:
        stdin,stdout,stderr = ssh.exec_command(line)
        tmpfile.write(stdout)

if __name__ == "__main__":
    files = open('D:/shell/userpasswd.txt','r')
    port = 22
    mdir1 = '/tmp/jcshell.sh'
    mdir2 = '/tmp/shellexec.py'
    srcfile1 = "D:/shell/jcshell.sh"
    srcfile2 = "D:/shell/shellexec.py"
    line = files.readline()
    while line != '\n':
        list = line.split(' ')
       # mdir3 = "/tmp/" + list[0].strip() + "_jcresult.txt"
        #srcfile3 = "D:/shell/jcresult/" + list[0].strip() + "_jcresult.txt"
        list[2] = list[2].strip('\n')
        ssh = ssh_connect(list[0],port,list[1],list[2])
        #print (list[2])
        #ssh.exec_command("mkdir /usr/java")
        #put_file(list[0],port,list[1],list[2],srcfile1,mdir1)
        #put_file(list[0],port,list[1],list[2],srcfile2,mdir2)
        #ssh.exec_command("cd /usr/java/;tar -xf jdk1.6.0_13_x64.tar.gz")
        #ssh.exec_command("chmod u+x /tmp/shellexec.py")
        #ssh.exec_command("python /tmp/shellexec.py")
        time.sleep(2)
        #get_file(list[0],port,list[1],list[2],mdir3,srcfile3)
        stdin,stdout,stderr = ssh.exec_command("ulimit -n")
        out = stdout.readline()
        #print(out)
        #ssh.exec_command("rm -f /tmp/*jcresult.txt")
        if out == str(1024):
            print ("the nofiles of %s is: %s "%(list[0],stdout))
        ssh_disconnect(ssh)
        line = files.readline()

    #for hline,uline in hostfile,userfile:
        #执行检查脚本，把检查的结果存
        #ssh = ssh_connect(hline,port,uline[0],uline[1])
        #exec_command(hline,ssh)

    #for hline,uline in hostfile,userfile:
        #上传计算md5 python脚本，计算完成
        #ssh = ssh_connect(hline,port,uline[0],uline[1])










