#this pysftp lib is needed so we can do some work on sftp easly
#like creating connection changing directories and so on
import pysftp
# the os lib is needed to work on folders and files
# with this lib we can easly test if a given path is a file or a folder ..
import os

# and this lib is needed to work with regular expression like the others do
# this lib is know for facilitating the work with regex
import re


""" this function will return a connection to an sftp server  """
def sftp_connect():
    return pysftp.Connection('172.18.250.211',username="taha",password="organisation2018")



def create_folder_if_not_existing(directory):
    if not os.path.exists(directory):
        print('Creating directory '+directory)
        os.makedirs(directory)

""" this function will append data to a file"""
def saving_to_file(filename,data):
    with open(filename,'a+') as source:
        source.write(str(data)+"\n")
        source.close()

def create_data_file(directory,data):
    create_folder_if_not_existing(directory)
    log_etc_file = directory+'/log_file'
    if not os.path.isfile(log_etc_file):
        #use the save_to_file function created previously
        saving_to_file(log_etc_file,data)




""" def save_etc_sftp():
    sftp = sftp_connect()
    with sftp.cd('/'+'etc'):
        etc = sftp.listdir()
        create_data_file('log_dir',str(etc)) """



""" this function will take a directory as a parameter and with the help
of the sftp package change directory to the given parameter and then get the list
of element within this directory and create a data file for each one of them"""
def save_directory_sftp(directory,sftp):
    with sftp.cd('/'+directory):
        directory_list = sftp.listdir()
        create_data_file('log_'+directory,str(directory_list))


def list_directory(directory,sftp):
    with sftp.cd('/'+directory):
        directory_list = sftp.listdir()
    return directory_list

""" return a initialized with direc:0 map"""
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
            save_directory_sftp('usr/'+direc,sftp)
            exist_directory_map[direc] = 1;

def recursive_parser(directory):
    for direc in directory:
        recursive_parser(direc)
        print(direc)

def isWhat(directory):
    if os.path.isdir(directory):
        print("Dir")
    else:
        print("Not Dire")


def parsing_log_file(filename):
    with open(filename,"r") as source:
        for element in source:
            new_str = re.sub('[^a-zA-Z]',' ',element)

        print(new_str)

""" what i'should do now is correct the format of the log files
after that save recursively folders inside folders  """

recursive_save_sftp('usr',sftp_connect())
