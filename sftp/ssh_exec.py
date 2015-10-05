__author__ = 'blackline'
import paramiko
import getpass
import Crypto
import ecdsa
import argparse
root = ""
none = ""
def ssh_connect(hostname,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,username,password)
    return ssh

def ssh_disconnect(client):
    client.close()

def exec_command(command,ssh):
    '''
    windows客户端远程执行linux服务器命令
    '''
    stdin,stdout,stderr = ssh.exec_command(command)
    err = stderr.readline()
    if "" != err:
        print("command:"+ command + "exec failed!\nERROR")
    else:
        print("command:" + command + "exec success\n" )
        for out in stdout:
            print (out)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="remotely exec command for linux")
    parser.add_argument('--host',action="store",dest="host",default='192.168.233.2')
    parser.add_argument('--port',action="store",dest="port",default=22,type=int)
    parser.add_argument('--username',action="store",dest="username",default=root)
    parser.add_argument('--password',action="store",dest="password",default=none)
    given_args = parser.parse_args()
    hostname,port = given_args.host,given_args.port
    username,password = given_args.username,given_args.password
    command = input("Enter the command to exec: ")
    ssh_session = ssh_connect(hostname,port,username,password)
    exec_command(command,ssh_session)
    ssh_disconnect(ssh_session)

