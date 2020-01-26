# coding=utf-8
import os
import conF
from datetime import datetime
from smtpMAILING import send_email



# on definit les paramétres qu'on get depuis le fichier de conf
hostname = conF.sftpConf.get("ip")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")

#cette fonction nous permettra si l'element appartenant au repertoire courant passé en paramétre existe déja ou non
# retourn TRUE || FALSE
def is_directory_existing(dir):
    #lister les elements du rep courant
	files = os.listdir('.')
	for f in files:
		if f==dir and os.path.isdir('./' + f):
			return True
	return False

def backup_directory():
    try:
        #on se positione dans le repertoire de back up on crée l'element de sauvegarde
        os.chdir(backup_dir)
        print("In directory "+backup_dir)
        file = str(datetime.now().strftime("%d-%m-%y-à-%H-%M-%S"))
        create_file(file)
        print("Created file "+file)
        #----------------------
        copy_file ='rsync -r '+start_directory + ' ' + backup_dir + '/' + file + '/ --delete --links'
        os.system(copy_file)
        conF.smtpConf["subject"] = "Success Backup"
        conF.smtpConf["message"] = "The back up fineshed successfully , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
    except:
        conF.smtpConf["message"] = "An Error occured during the back up  , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
        conF.smtpConf["subject"] = "Error Backup"
        print('Skipping '+backup_dir+' due to permissions!!!!!')


def create_file(file):
	if is_directory_existing(file) is False:
		os.mkdir(file)
	os.chdir(file)



backup_directory()
send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("log_local"))



