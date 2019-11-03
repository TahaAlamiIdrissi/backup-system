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
    log_etc_file = directory+'/log_file'
    if not os.path.isfile(log_etc_file):
        saving_to_file(log_etc_file,data)

def saving_to_file(filename,data):
    with open(filename,'a+') as source:
        source.write(data)
        source.close()


""" def save_etc_sftp():
    sftp = sftp_connect()
    with sftp.cd('/'+'etc'):
        etc = sftp.listdir()
        create_data_file('log_dir',str(etc)) """


def save_directory_sftp(directory,sftp):
    with sftp.cd('/'+directory):
        directory_list = sftp.listdir()
        create_data_file('log_'+directory,str(directory_list))

def list_directory(directory,sftp):
    with sftp.cd('/'+directory):
        directory_list = sftp.listdir()
    return directory_list


def initialize_map_directories(directory,sftp):
    exist_directory_map = {}
    directories = list_directory(directory,sftp)
    for direc in directories:
        exist_directory_map[direc] = 0
    return exist_directory_map

def recursive_save_sftp(directory,sftp):
    exist_directory_map = initialize_map_directories(directory,sftp)
    for direc in exist_directory_map:
        if exist_directory_map[direc] == 0:
            #initialize_map_directories(direc,sftp)
            #recursive_save_sftp(direc,sftp)
            save_directory_sftp('usr/'+direc,sftp_connect())
            exist_directory_map[direc]= 1 
            
recursive_save_sftp('usr',sftp_connect())