#!/usr/bin/env python
import os
file = open('/etc/hosts','a+')
hn = os.popen('hostname -I').read()
dn = os.popen('hostname').read()
wcontent = hn.strip('\n') + " " +dn
file.write(wcontent)
file.close()
os.remove("/tmp/iphost.py")
 