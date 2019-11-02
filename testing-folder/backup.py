from ftplib import FTP
import os
import fileinput


ftp = FTP()
ftp.set_debuglevel(2)
ftp.connect('your ftp server',21)
ftp.login('taha','organisation2018')

