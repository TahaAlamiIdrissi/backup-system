import pysftp
import os

def create_folder_if_not_existing(directory):
    if not os.path.exists(directory):
        print('Creating directory '+directory)
        os.makedirs(directory)
    
def create_data_file(directory,data):
    create_folder_if_not_existing(directory)
    log_etc_file = directory+'/log_etc'
    if not os.path.isfile(log_etc_file):
        saving_to_file(log_etc_file,data)

def saving_to_file(filename,data):
    with open(filename,'a+') as source:
        source.write(data)
        source.close()


def get_data_sftp():
    with pysftp.Connection('172.18.250.170',username="taha",password="organisation2018") as sftp:
        with sftp.cd('/etc/'):
            etc = sftp.listdir()
            create_data_file('log_dir',str(etc))

get_data_sftp()