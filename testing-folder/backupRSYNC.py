import os
import conF

#Le protocol RSYNC n'est pas fonctionelle ! 

hostname = conF.sftpConf.get("ip")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")


rsync ='sshpass -p '+ '"' + password + '"' +' rsync -r '+ start_directory + ' ' + username + '@' + hostname+ ':' + backup_dir + '/ --delete --links'
os.system(rsync)
print(rsync)

