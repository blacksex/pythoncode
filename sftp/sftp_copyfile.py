__author__ = 'blackline'
import paramiko
import getpass
import argparse
import Crypto
import ecdsa
srcfile = 'D:/downloaded/software/python/paramiko-master/setup.py'
dstfie = '/tmp/setup.py'

def copy_file(hostname,port,username,password,src,dst):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    print("Connecting to %s \n with username=%s"%(hostname,username))
    t = paramiko.Transport((hostname,port))
    t.connect(username="root",password="dragon")
    sftp = paramiko.SFTPClient.from_transport(t)
    print("Copying file:%s to path:%s"%(src,dst))
    sftp.put(src,dst)
    sftp.close()
    t.close()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Remote file copy')
    parser.add_argument('--host',action="store",dest="host",default='192.168.233.2')
    parser.add_argument('--port',action="store",dest="port",default=22,type=int)
    parser.add_argument('--src',action="store",dest="src",default=srcfile)
    parser.add_argument('--dst',action="store",dest="dst",default=dstfie)

    given_args = parser.parse_args()
    hostname,port = given_args.host,given_args.port
    src,dst = given_args.src,given_args.dst

    username = input("Enter the username:")
    password = getpass.getpass("Enter password for %s: " %username)
    copy_file(hostname,port,username,password,src,dst)