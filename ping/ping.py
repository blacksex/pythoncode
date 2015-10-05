__author__ = 'blackline'
import subprocess
import shlex
import os
hostfile = open('D:/ping/hosts.txt','r')
line = hostfile.readline()
while line != '\r\n':
    if not line.strip():break
    list = line.split()
    ping_command = "ping -n 1"
    command_line = ping_command + ' ' + list[0]
    args = shlex.split(command_line)
    try:
        subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        print ("%s is ok"%(list[0]))
    except subprocess.CalledProcessError:
        print ("%s is not ok"%(list[0]))
    line = hostfile.readline()
print ("completed")