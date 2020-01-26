# coding=utf-8
import os
import conF
from datetime import datetime
from smtpMAILING import send_email

hostname = conF.sftpConf.get("ip")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")

def is_directory_existing(dir):
	files = os.listdir('.')
	for f in files:
		if f==dir and os.path.isdir('./' + f):
			return True
	return False

def backup_directory():
	os.chdir(backup_dir)
	file = str(datetime.now().strftime("%d-%m-%y-à-%H-%M-%S"))
	create_file(file)
	copy_file ='rsync -r '+start_directory + ' ' + backup_dir + '/' + file + '/ --delete --links'
	os.system(copy_file)

def create_file(file):
	if is_directory_existing(file) is False:
		os.mkdir(file)
	os.chdir(file)



backup_directory()
send_email(conF.smtpConf.get("subject"),conF.smtpConf.get("content"))


