#!/usr/bin/env python
import os
hn = os.popen('hostname -I').read().strip('\n')
filename = "/tmp/" + hn.strip() + "_jcresult.txt"
os.system(r'touch %s'%filename)
os.popen("chmod u+x /tmp/jcshell.sh")
os.system(r'/bin/bash /tmp/jcshell.sh > %s'%filename)
#os.remove("/tmp/jcshell.sh")
#os.remove("/tmp/shellexec.py")
