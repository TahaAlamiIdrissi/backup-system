import os
import conF
from smtpMAILING import send_email

#Le protocol RSYNC n'est pas fonctionelle ! 

hostname = conF.sftpConf.get("ip")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")


rsync ='rsync -r '+ start_directory + ' ' + username + '@' + hostname+ ':' + backup_dir + '/ --delete --links'
os.system(rsync)
print(rsync)
send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("log_ftps"))


