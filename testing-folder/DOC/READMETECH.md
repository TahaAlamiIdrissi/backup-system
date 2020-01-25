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
## Lancement de l'utilitaire

une fois toute les étapes de l'installation effectué l'utilitaire peut être lancé manuellement comme suit:

```bash
sudo ./run.sh
```


## License
[MIT](https://choosealicense.com/licenses/mit/)