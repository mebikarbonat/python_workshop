#Muhammad Azizi Mohd Ariffin
#mazizi@fskm.uitm.edu.my

import platform
import subprocess as sub

plat = str(platform.platform())

if 'Window' in plat :
    cmd = 'ipconfig'
elif 'Linux' in plat :
    cmd = 'ifconfig'

proc = sub.Popen([cmd],stdout=sub.PIPE)
while True:
  line = proc.stdout.readline()
  if not line:
    break
  print(str(line.rstrip()))