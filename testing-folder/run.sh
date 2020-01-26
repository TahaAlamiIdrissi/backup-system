#! /bin/bash


mkdir logs

menu(){
	echo -e "\t\t\e[5;33m Welcome in the GNU/GROUPS Loading ...\e[0m"
	sleep 3
	clear
	while true
	do
		echo -e "\n\n\t\t************ GROUPS/GNU **************\n"
		echo -e "\t\t1- SFTP backup"
		echo -e "\t\t2- FTP backup "
		echo -e "\t\t3- RSYNC backup "
		echo -e "\t\t4- backup Locally "
		echo -e "\t\t5- quit "
		echo -e "\t\tchoose (1) (2) (3) (4) (5) "
		read choice

        case $choice in
			"1") python backupSFTP.py > ./logs/log_sftp
				;;
			"2") python backupFTP.py > ./logs/log_ftp
				;;
			"3") python backupRSYNC.py
				;;
			"4") python backupLocal.py
				;;
			"5") echo -e "\t\t\e[3;33m GNU\Taha \n \t\t2019-2020\n \t\tBOOO-BYEEEEE \e[0m"
				break
				;;
		esac
		done
}

menu