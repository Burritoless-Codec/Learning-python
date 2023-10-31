import hashlib
from datetime import datetime
import os


#Take input from user about file.
print('Filename is case sensative! Include extention.')
fname = str(input('File Name:'))

#get time and date for log file
now = datetime.now()
ctime = now.strftime("%I:%M:%S%p")
cdate = now.strftime("%x")

#check if file exists
if os.path.exists(fname):
    #open and read file if exists
    with open(fname, 'rb') as ftc:

        data = ftc.read()

        #calculate hash's
        md5_r = hashlib.md5(data).hexdigest()
        sha1_r = hashlib.sha1(data).hexdigest()
        sha256_r = hashlib.sha256(data).hexdigest()
        sha512_r = hashlib.sha512(data).hexdigest()

        #convert into a writable string for log file
        #generate log file name and extention
        rh = str("MD5: " + md5_r + "  SHA-1: " + sha1_r + "  SHA-256: " + sha256_r + "  SHA-512: " + sha512_r)
        wfn = str(fname+'.hash')

        #open and or create logfile and append hash's
        wf = open(wfn, "a")
        wf.write(rh + ' ' + str(cdate) + ' ' + str(ctime) + "\n")
        wf.close()

        #open log file
        rf = open(wfn, "rt")
        #read and print logfile to command line
        print(rf.read())
        rf.close()
        print("Hashed successful. Logfile: ", wfn)
else:
    #if file does not exist error out for user to correct
    print('Error file does not exist!')
    print('File Requested:', fname)
