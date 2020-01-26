# BACKUP SYSTEM (MEMOIRE TECHNIQUE)

Systéme de Sauvegarde automatique qui permet de selectionner des éléments (dossier ou autres) à inclure dans le processus de sauvegarde.

## Usage

une fois avoir 'unzip' le dossier localement , on remarque qu'on a un ensemble de fichier backupPROTOCOL.py
chaque fichier correspond a un mode de sauvegarde .

### Backup (FTP)

Commencant par la sauvegarde en ftp :

```python
import ftplib
import os
import shutil
from datetime import datetime
```
- tout d'abord nous commençons par importer le module ftplib. Ce dernier definit la classe FTP qui implémente le côté client du protocole FTP,  et quelques éléments associés.
- Viens aprés l'utilisation du module os, qui lui,  fournit une maniére portable d'utiliser les fonctionalités dépendantes du systéme d'exploitation. 
- Le module datetime qui permettra de definier la date de sauvegarde
- Puis viens le module shutil qui offre des fonctions utilitaire pour la copie et l'archivage des fichiers .

Contenue du fichier :

```python
def get_files_directories()

def backup_directory(local_dir,remote_dir)
```

dans ce fichier deux méthodes sont definis, la premiére permet de recupérer tout les fichiers et les dossiers du répértoire courant via retrlines sous le format suivant en cas de succés.
``` bash
drwxr-xr-x 2 root root 4096  25 11:41 .
-rwxr-xr-x 1 root root  747  25 11:20 run.sh
```
la deuxiéme , via les paramétres definis plus haut, permet de ce placer sur le répértoire à sauvegarder, ainsi d'appeler la prémiére fonction pour éffectuer la sauvegarde de ce dérnier.
l'objet du message envoyé à l'utilisateur est definis lors de la sauvegarde tel que si tout c'est bien passé "Success Backup " est alors mis dans le champ qui lui est attribué dans le fichier de configuration, ainsi on pourra récupérer cette information par la suite,sinon c'est  "Error Backup" qui est ecris dans la conf.

- Versions

Premiére méthodes : 

```python
datestring = str(datetime.date.today())
if os.path.exists(datestring):
    conF.sftpConf["version"] = conF.sftpConf["version"]+1
    datestring = str(datestring)+"-V-"+str(conF.sftpConf.get("version"))
    
os.mkdir(datestring)
os.chdir(datestring)
local_dir = os.getcwd()
```

En ce qui concerne les versions, la premiére sauvegarde est effectué sous la forme suivant par exemple: 
 - 2020-01-25
si on veut effectuer une deuxiéme version de la sauvegarde, on recupére alors une valeur qui est initialisé a 0 dans le fichier de conf, qu'on incrémente à chaque sauvegarde pour avoir l'affichage suivant:
 - 2020-01-25-V-i avec i dans {1,2,3...}
Or les données concernant le numéro de versions n'etaient pas persistés .

Deuxiéme méthodes :

```python
datestring = str(datetime.now().strftime("%d-%m-%y-à-%H-%M-%S"))
```

Utilisation de l'affichage temporel suivant : 26-01-20-à-15-20-01  le 26 janvier 2020 à 15h20min01sec qui est simple et éfficace.

- Envoi du contenu du log file à l'utilisateur

Premier Essaie : 
Au tout debut nous avons essayé d'envoyer dans le corps du mail les informations et logs , on a procédé de la façons suivante:
```python
with open('/usr/src/backup-system/testing-folder/logs/log_ftp','r') as file:
    data = file.read()
conF.smtpConf["content"] = data  

send_email(conF.smtpConf["subject"],conF.smtpConf["content"])
```
Or, ceci n'etait pas assez générique, ni professionel, le message devait être simple et clair avec une piéce jointe détaillée.

```python
send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("log_ftp"))
```
on remplacé alors la section "content" par message qui definis un text simple et clair, et on a rajouté une piéce jointe au mail.

on suit le meme pattern utilisé pour initialiser le paramétre "subject" dans la conf, mais cette fois, on effectue une lecture du fichier de log pour ensuite envoyer son contenue comme message du mail.

### Backup (SFTP)

On ce qui concerne la backup via SFTP on garde le meme pattern, tout d'abord commencant par les 'imports'.

```python
import paramiko
```

 - Utilisation de paramiko : c'est une implémentation du protocole SSHv2 qui fournis à la fois des fonctionalités coté client et coté serveur. Le choix de ce module repose sur plusieurs facteurs: 
  - popularité du module 
  - documentation 
  - connaissance et utilisation dans d'autre projet (Projet interface administration)

```python
def get_files_directories()

def backup_directory(local_dir,remote_dir)
```

En ce qui concerne la méthodoligie c'est la meme utilisé dans le module FTP.

```python
# Répértoire de backup
os.chdir(backup_dir)

# creation du répértoire contenant la date courante
datestring = str(datetime.date.today())

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

```

### Backup (Local)

En ce qui concerne le fichier de  sauvegarde local, ce dernier contient trois fonctions :

```python 
def is_directory_existing(dir)
def create_file(file)
def backup_directory()
```

la premiére fonction nous permet de voir si les éléments dans le repértoire passé en paramétre sont existant ou non, elle retournera True si l'élément existe déja, False sinon. 

la deuxiéme fonction quant à elle, permet de tester si le répértoire existe déja via la premiére fonction, si cette dérniére retourne True , c'est que l'élément existe , ainsi il suffit de ce positionner dans ce répértoire. sinon on créer un nouveau.

et enfin, la troixiéme fonction backup_directory() qui permet de faire le back up via la commande rsync.



### Fichier de Configuration

Le fichier de configuration est un fichier ou sont definis les arguments générique de quelques modules.
dans notre cas on a definis le fichiers de conf comme etant un dictionnaire de données:

```python
sftpConf = {
    "ip": "192.168.0.0",
    "username": "tse_2020",
    "password": "tsetse",
    "folder": "/usr/src/backup-system/",
    "version":0,
    "backup-folder":"/home/tse_2020/backup_dir/"
}
```
pour chaque protocol (FTP,SFTP..) on dispose d'information qu'on doit fournir , pour que ce dernier fonctione.
comme par exemple l'ip , le username ou autre, et parfois, il possible que le port par defaut du protocol ne soit pas libre.
du coup , on utilise un dictionnaire pour les ports:

```python
portConf = {
    "sftp": 22,
    "ftp": 21,
    "smtp":587,
    "ftps":21
}
``` 

On dispose aussi d'informations concernant l'envoie de mail en cas de succes ou bien d'echec.
```python
smtpConf = {
    "mail":"mail@gmail.com",
    "password": "password",
    "subject":"",
    "content":""
}
```
On reste toujours sur des dictionnaires, avec cette fois comme donnée , l'adresse mail et le mot de passe à fournir.
Et en ce qui concerne les deux autres champs, "subject" et "content", il seronts initialisé par la validité de la sauvegarde respectivement.

- exemple

```python
      conF.smtpConf["subject"] = "Success Backup"
    except:
      conF.smtpConf["subject"] = "Error Backup"
```

Et enfin, pour définir quelle est le fichier de log à envoyer comme piéce jointe, on definie les paramétres suivant:

```python
logConf = {
    "log_ftp": "/usr/src/backup-system/testing-folder/logs/log_ftp",
    "log_sftp": "/usr/src/backup-system/testing-folder/logs/log_sftp",
    "log_rsync": "/usr/src/backup-system/testing-folder/logs/log_rsync",
    "log_local": "/usr/src/backup-system/testing-folder/logs/log_local",
    "log_ftps": "/usr/src/backup-system/testing-folder/logs/log_ftps"
}
```
tel que comme troisiéme arguments de la fonction "send_email", on choisie le log à envoyer.


```python
send_email(conF.smtpConf["subject"],conF.smtpConf["message"],conF.logConf.get("<fichier_de_log>"))

```

### Fichier install_all.sh

afin de faciliter et d'automatiser la mise en place de l'utilitaire au client, le script shell suivant va nous permettre d'installer les dependances nécéssaire au fonctionement de ce dernier, ainsi que les modules utilisés dans nos script python, en donnant au client le choix
d'utiliser la version de "pip" dont il dispose.

```bash
#! /bin/bash

apt-get install sshpass
$1 install -r requirements.txt
```

$1 : la version de pip (pip || pip3)


### Systéme d'envoi de mail


```python
import smtplib
import conF
```

utilisation du module smtplib presenter dans le cours , qui représente un client smtp utilisé pour l'envoi de mail vers n'importe quelle machine via un demon smtp.

Comme le montre le code suivant:
```python
    mail_content = message
    #The mail addresses and password
    sender_address = conF.smtpConf.get("mail")
    sender_pass = conF.smtpConf.get("password")
    receiver_address = conF.smtpConf.get("mail")
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject
    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = attachment
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
```
sources: tutorialspoint.com/send-mail-with-attachment-from-your-gmail-account-using-python

## License
[MIT](https://choosealicense.com/licenses/mit/)