#!/bin/bash
echo '#########SYSTEM VERSION###############'
lsb_release -a
echo -e '\n'
uname -a
echo -e '\n'
echo '######## JAVA PROCCESS################'
ps -ef | grep java
echo -e '\n'
echo '########LISTEN OF PORTS###############'
netstat -lntp
echo -e '\n'
echo '#########USERS and GROUPS#############'
gawk -F: '{print $1}' /etc/passwd
echo -e '\n'
echo '##########GROUPS#######################'
gawk -F: '{print $1}' /etc/group
echo -e '\n'
echo '#######CHECK NULL OF PASSWORD##########'
gawk -F: '($2==""){print $1}' /etc/shadow
echo -e '\n'
echo '#######IPTABLES########################'
iptables -nvL
echo -e '\n'
echo '#######SELINUX#########################'
getenforce
echo -e '\n'
echo '######CATEGORY OF PASSOWRDS#############'
cat /etc/login.defs
echo -e '\n'
echo '#######SYSCTL##########################'
sysctl -e kernel.shmmax
sysctl -e kernel.shmall
sysctl -e kernel.shmmni
sysctl -e kernel.sem
sysctl -e net.ipv4.ip_local_port_range
sysctl -e net.core.rmem_default
sysctl -e net.core.rmem_default
sysctl -e net.core.wmem_default
sysctl -e net.core.rmem_max
sysctl -e net.core.wmem_max
sysctl -e fs.aio-max-nr
sysctl -e fs.file-max
sysctl -e net.ipv4.conf.all.arp_ignore
echo -e '\n'
echo '########SSH TIMEOUT SESSION##############'
grep "Client" /etc/ssh/sshd_config
echo -e '\n'
echo '########SERVICES LIST###################'
runlevel
echo -e '\n'
chkconfig --list
echo -e '\n'
echo '###########SYSLOG CONFIG################'
cat /etc/rsyslog.conf
echo -e '\n'
echo '########MOUNT############################'
mount -l
echo -e '\n'
echo '########disk use#########################'
df -h
echo -e '\n'
echo '#######completed#########################'


