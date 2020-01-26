# coding=utf-8

''' Module de sauvegarde SFTP '''
import paramiko
import os
from datetime import datetime
import shutil
from smtpMAILING import send_email
import conF

#creation des variables qui contiendront les infos sur la connexion via SFTP
hostname = conF.sftpConf.get("ip")
port = conF.portConf.get("sftp")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")


''' Cette fonctions permet de lister et de retouner tout les fichiers et dossier du répértoire courant '''
# name : get_files_directories : recupération des fichiers et des dossiers
# return : files,directories
def get_files_directories():

    # recupération via sftp de la liste des elements du répértoire courant 
    filelisting = sftp.listdir('.')
    
    # creation de la liste des fichiers ainsi que celle des répértoire
    files = []
    directories = []
    
    #pour chaque élément de la liste récupéré via listdir on regarde :
    # type de retour 
    ''' drwxr-xr-x 2 root root 4096  25 11:41 .
       -rwxr-xr-x 1 root root  747  25 11:20 run.sh'''
       
    # on regarde si le premier element est 'd' -> directori
    # ou si ce dernier commence par '-' -> fichier
    for file_name in filelisting:
        try:
            stat = str(sftp.lstat(file_name))
            if stat[0] == 'd':
                directories.append(file_name)
            elif stat[0] == '-':
                files.append(file_name)
        except PermissionError:
            print('Skipping '+file_name+' due to permissions')
            
    return files,directories
    
def backup_directory(local_dir,remote_dir):

    os.chdir(local_dir)
    sftp.chdir(remote_dir)
    print('In directory '+remote_dir)

    files,directories = get_files_directories()

    for f in files:
        print('Backing up '+f)
        try:
            sftp.get(f, f)
            conF.smtpConf["subject"] = "Success Backup"
            conF.smtpConf["message"] = "The back up fineshed successfully , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
        except PermissionError:
            conF.smtpConf["subject"] = "Error Backup"
            conF.smtpConf["message"] = "An Error occured during the back up  , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
            print('Skipping '+f+' due to permissions')


    for d in directories:
        newremote = remote_dir+d+'/'
        newlocal = local_dir+'/'+d
        os.mkdir(newlocal)
        backup_directory(newlocal,newremote)
        

# Répértoire de backup
os.chdir(backup_dir)

# creation du répértoire contenant la date courante
datestring = str(datetime.now().strftime("%d-%m-%y-%H-%M-%S"))


os.mkdir(datestring)
os.chdir(datestring)
local_dir = os.getcwd()

# etablition de la connectioon au host distant
transport = paramiko.Transport((hostname, port))
transport.connect(username = username, password = password)
sftp = paramiko.SFTPClient.from_transport(transport)

# sauvegarde de . 
remote_dir = start_directory

backup_directory(local_dir,remote_dir)
print("------------------------------------------------------------- END OF BACK UP\n")

send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("log_sftp"))

# fermeture de la connection sftp
sftp.close()
transport.close()