''' Configuration File'''

#Global config for all the protocols
sftpConf = {
    "ip": "161.3.40.196",
    "username": "username",
    "password": "password",
    "folder": "/usr/src/backup-system/",
    "version":0,
    "backup-folder":"/home/tse_2019/backup_dir/"
}

#port configuration
portConf = {
    "sftp": 22,
    "ftp": 21,
    "smtp":587,
    "ftps":21
}

#mailing configuration
smtpConf = {
    "mail":"mail@gmail.com",
    "password": "password",
    "subject":"",
    "content":"",
    "message":""
}

#log configuration
logConf = {
    "log_ftp":"/usr/src/backup-system/testing-folder/logs/log_ftp",
    "log_sftp":"/usr/src/backup-system/testing-folder/logs/log_sftp",
    "log_rsync":"/usr/src/backup-system/testing-folder/logs/log_rsync",
    "log_local":"/usr/src/backup-system/testing-folder/logs/log_local",
    "log_ftps":"/usr/src/backup-system/testing-folder/logs/log_ftps"
}