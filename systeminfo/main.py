import os
import getpass
import platform
import ctypes
from datetime import datetime
import uuid
import re

try:
    ia = os.getuid() == 0
except AttributeError:
    ia = ctypes.windll.shell32.IsUserAnAdmin() != 0

now = datetime.now()
ctime = now.strftime("%I:%M:%S%p")
cdate = now.strftime("%x")
dash = r'''|-------------------------------------------------------|'''

print(r"""
 ____            _                   ___        __
/ ___| _   _ ___| |_ ___ _ __ ___   |_ _|_ __  / _| ___
\___ \| | | / __| __/ _ \ '_ ` _ \   | || '_ \| |_ / _ \
 ___) | |_| \__ \ ||  __/ | | | | |  | || | | |  _| (_) |
|____/ \__, |___/\__\___|_| |_| |_| |___|_| |_|_|  \___/
       |___/
       """)
print(dash)
print('OS Information')
print('OS Name:', str(platform.system()))
print('OS Release:', str(platform.release()))
print('OS Version:', str(platform.version()))
print('OS Raw:', str(platform.platform()))
print(dash)
print('User Information')
print('Current User:', getpass.getuser())
print('Current User Path:', os.path.expanduser('~'))
print(dash)
print('System Information')
print('Current Time:', ctime)
print('Current Date:', cdate)
print ('Mac Address:',':'.join(re.findall('..', '%012x' % uuid.getnode())))
print(dash)
print('Session Information')
print('Running Admin:', ia)
