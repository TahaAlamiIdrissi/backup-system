# coding=utf-8

''' Module de sauvegarde FTP '''
# Import du module ftplib built-in python 
import ftplib
# Import du module OS built-in python 
import os
from datetime import datetime
import shutil
#from smtpMAILING import send_email
#Import du fichier de conF
import conF
from smtpMAILING import send_email

#creation des variables qui contiendront les infos sur la connexion via FTP
hostname = conF.sftpConf.get("ip")
username = conF.sftpConf.get("username")
password = conF.sftpConf.get("password")
start_directory = conF.sftpConf.get("folder")
backup_dir = conF.sftpConf.get("backup-folder")

''' Cette fonctions permet de lister et de retouner tout les fichiers et dossier du répértoire courant '''
# name : get_files_directories : recupération des fichiers et des dossiers
# return : files,directories
def get_files_directories():
    # liste qui contiendra le callback de la methode retrlines
    dirlisting = []
    # retrlines prend en parametres (cmd FTP pour listing)
    # et deuxiéme parametre qui est un callback pour chaque line reçu du server
    # retourne a message 226 transfer complete et la liste si tout est ok
    # 550 sinon
    ftp_obj.retrlines('LIST',callback=dirlisting.append)

    # liste qui contiendra les fichiers
    files = []
    # liste qui contiendra les répértoire
    directories = []

    # type de retour 
    ''' drwxr-xr-x 2 root root 4096  25 11:41 .
       -rwxr-xr-x 1 root root  747  25 11:20 run.sh'''
       
    # on regarde si le premier element est 'd' -> directori
    # ou si ce dernier commence par '-' -> fichier
    for l in dirlisting:
        lastspace = l.rindex(' ')
        file_name = l[lastspace+1:]
        if l[0] == 'd' and file_name != '.' and file_name != '..':
            directories.append(file_name)
        elif l[0] == '-':
            files.append(file_name)

    return files,directories

    
def backup_directory(local_dir,remote_dir):
    # on ce positione sur le répértoire courant 
    os.chdir(local_dir)
    try:
        # on essaye de connecter au répértoire distant si on a les droits
        ftp_obj.cwd(remote_dir)
        print('In directory '+remote_dir)
        #recupération des fichiers et des répértoire
        files,directories = get_files_directories()
        # recupération pour chaque element de la lister des fichiers
        # on mode binaire 
        for f in files:
            print('Backing up '+f)
            try:
                ftp_obj.retrbinary('RETR '+f, open(f, 'wb').write)
            except ftplib.error_perm:
                print('Skipping '+f+' due to permissions')

        for d in directories:
            newremote = remote_dir+d+'/'
            newlocal = local_dir+'/'+d
            os.mkdir(newlocal)
            print(newlocal)
            backup_directory(newlocal,newremote)
        conF.smtpConf["subject"] = "Success Backup"
        conF.smtpConf["message"] = "The back up fineshed successfully , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
    except:
        conF.smtpConf["message"] = "An Error occured during the back up  , you can find the log of what has been done attached to the mail ,\n Thank you for choosing alassiBackup,\n"
        conF.smtpConf["subject"] = "Error Backup"
        print('Skipping '+remote_dir+' due to permissions!!!!!')


# Répértoire de backup

os.chdir(backup_dir)

# creation du répértoire ayant comme nom la date du jour courant

datestring = str(datetime.now().strftime("%d-%m-%y-à-%H-%M-%S"))

os.mkdir(datestring)
os.chdir(datestring)
local_dir = os.getcwd()

# connection au host 
ftp_obj = ftplib.FTP_TLS(host=hostname, user=username, passwd=password)

ftp_obj.connect(hostname,conF.portConf.get("ftps"))
ftp_obj.login(username,password)

remote_dir = start_directory

backup_directory(local_dir,remote_dir)



print("------------------------------------------------------------- END OF BACK UP\n")


send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("log_ftps"))
# fermeture de la connection
ftp_obj.quit()