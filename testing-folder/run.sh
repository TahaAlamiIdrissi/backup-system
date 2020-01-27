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
		echo -e "\t\t3- Local backup "
		echo -e "\t\t4- FTPS backup "
		echo -e "\t\t5- RSYNC backup "
		echo -e "\t\t6- quit "
		echo -e "\t\tchoose (1) (2) (3) (4) (5) or (6) "
		read choice

        case $choice in
			"1") python backupSFTP.py >> ./logs/log_sftp
				;;
			"2") python backupFTP.py >> ./logs/log_ftp
				;;
			"3") python backupLOCAL.py >> ./logs/log_local
				;;
			"4") python backupFTPS.py >> ./logs/log_ftps
				;;
			"5") python backupRSYNC.py >> ./logs/log_rsync
				;;
			"6") echo -e "\t\t\e[3;33m GNU\Taha \n \t\t2019-2020\n \t\tBOOO-BYEEEEE \e[0m"
				break
				;;
		esac
		done
}

menu