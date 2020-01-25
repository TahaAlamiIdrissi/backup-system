# BACKUP SYSTEM (MEMOIRE TECHNIQUE)

Systéme de Sauvegarde automatique qui permet de selectionner des éléments (dossier ou autres) à inclure dans le processus de sauvegarde.

## Usage

une fois avoir 'unzip' le dossier localement , on remarque qu'on a un ensemble de fichier backupPROTOCOL.py
chaque fichier correspond a un mode de sauvegarde .

### backupFTP

Commencant par la sauvegarde en ftp :

```python
import ftplib
import os
import shutil
import datetime
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

### backupSFTP

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
### backupRSYNC


### backupFTPS





## License
[MIT](https://choosealicense.com/licenses/mit/)