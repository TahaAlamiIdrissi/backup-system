import pysftp
import os


def sftp_connect():
    return pysftp.Connection('172.18.250.170',username="taha",password="organisation2018")



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


def save_etc_sftp():
    sftp = sftp_connect()
    with sftp.cd('/'+'etc'):
        etc = sftp.listdir()
        create_data_file('log_dir',str(etc))


def save_directory_sftp(directory):
    sftp = sftp_connect()
    with sftp.cd('/'+directory):
        directory_list = sftp.listdir()
        create_data_file('log_'+directory,str(directory_list))

save_directory_sftp('usr/src')