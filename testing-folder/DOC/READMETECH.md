# BACKUP SYSTEM (DOC UTILISATEUR)

Systéme de Sauvegarde automatique qui permet de selectionner des éléments (dossier ou autres) à inclure dans le processus de sauvegarde.

## Installation

Le projet peut etre cloné via 'the github repo ' : 

l'installation des modules ce fait en lançant le script install_all.sh . 
en précisant la version du gestionnaire de package (pip || pip3).

```bash
sudo ./install_all.sh pip
```
dans les fichiers présent, nous disposons d'un fichier conF.py où il faut préciser les informations de sauvegarde.

```python
Conf = {
    "ip": "<ip_du_serveur>",
    "username": "<username>",
    "password": "<password>",
    "folder": "<dir_a_sauvegarder>",
    "backup-folder":"<dir_ou_sauvegarder>"
}
```

et aussi les informations concernant le mailing

```python
smtpConf = {
    "mail":"<mail_de_reception>",
    "password": "<mot_de_passe>",
    "subject":"",
    "content":""
}
```
il faut aussi activer l'accés non sécurisé dans gmail comme le montre les images suivantes.

![alt text](./screenshots/lesssecure.png)


## Lancement de l'utilitaire

(POUR TEST)
une fois toute les étapes de l'installation effectué l'utilitaire peut être lancé manuellement comme suit:

```bash
sudo ./run.sh
```
ou automatiquement via crontab 

Ouvrir un terminal :
```bash 
export EDITOR=<editeur_préfére> ; crontab -e
```
ajouter : 
```bash
min h j d m python <path_to_current_folder>/<script_of_your_choice> > <name_of_log_file>
59 23 * * * python /usr/src/backup/backupSFTP.py > log_sftp
```
il suffit de modifier le fichier cronjobs.txt et de coller son contenue dans /var/spool/cron

## License
[MIT](https://choosealicense.com/licenses/mit/)