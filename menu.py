B
    �W�]�V  �               @   s   d dl Z ee �d�� dS )�    Ns%  �               @   s   d dl Z ee �d�� dS )�    Ns�$  �               @   s   d dl Z ee �d�� dS )�    Ns$  �               @   s   d dl Z ee �d�� dS )�    Ns�#  �               @   s   d dl Z ee �d�� dS )�    Ns#  �               @   s   d dl Z ee �d�� dS )�    Ns�"  �               @   s   d dl Z ee �d�� dS )�    Ns"  �               @   s   d dl Z ee �d�� dS )�    Ns�!  �               @   s   d dl Z ee �d�� dS )�    Ns!  �               @   s   d dl Z ee �d�� dS )�    Ns�   �               @   s   d dl Z ee �d�� dS )�    Ns   �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns   �               @   s   d dl Z ee �d�� dS )�    Ns~  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsz  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsv  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsr  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsn  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsj  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsf  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Nsb  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    Ns^  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    NsZ  �               @   s   d dl Z ee �d�� dS )�    Ns�  �               @   s   d dl Z ee �d�� dS )�    NsV  �               @   sH  d dl Z d dlZd dlZdd� Zdd� Zdd� Zdd	� Zd
d� Zdd� Zdd� Z	e �
d� e�  ed�Zedksxedkr�e�  n�edks�edkr�e�  n�edks�edkr�e�  n�edks�edkr�e�  nredks�edkr�e�  nZedks�edk�re �
d� ed� e �
d� n*ed � e �
d!� ed"� e �
d� e	�  e �
d#� dS )$�    Nc               C   sB   t �d� t td� td� td� td� td� td� d S )Nzbash .menu/indexz)[33;1m [[37;1m01[33;1m][37;1m Encryptz)[33;1m [[37;1m02[33;1m][37;1m Decryptz/[33;1m [[37;1m03[33;1m][37;1m Install Bahanz,[33;1m [[37;1m04[33;1m][37;1m Info Toolsz,[33;1m [[37;1m05[33;1m][37;1m Contact usz([33;1m [[37;1m06[33;1m][37;1m Keluar)�os�system�print� r   r   �<file>�menu   s    
r   c               C   s&   t �d� td� t �d� t�  d S )Na  cd $EXTERNAL_STORAGE ; echo -en "[33;1m Input File Name :[37;1m "; read lama; echo -en "[33;1m Output File Name :[37;1m "; read new; echo -en "[33;1m PROCESSING"; sleep 1; echo -en "[37;1m."; sleep 2; echo -en "."; sleep 3; echo -en "."; echo; bash-obfuscate $lama -o 0203760.sh &> /dev/null; bash-obfuscate 0203760.sh -c 2 -o 0203860.sh &> /dev/null; rm 0203760.sh; bash-obfuscate 0203860.sh -o 0203760.sh &> /dev/null; rm 0203860.sh; bash-obfuscate 0203760.sh -c 2 -o 0203860.sh &> /dev/null; rm 0203760.sh; bash-obfuscate 0203860.sh -o 0203760.sh &> /dev/null; rm 0203860.sh; bash-obfuscate 0203760.sh -c 2 -o 0203860.sh &> /dev/null; rm 0203760.sh; bash-obfuscate 0203860.sh -o 0203760.sh &> /dev/null; rm 0203860.sh; bash-obfuscate 0203760.sh -c 2 -o $new &> /dev/null; rm 0203760.sh;z)
[33;1m [[37;1m+[33;1m][37;1m SELESAIzsleep 3)r   r   r   �restartr   r   r   r   �encrypt   s    

r	   c              C   s�   t �d� td�} d}d}t �d|  d � tdd�}x$t�d�D ]}|�|�||�� qBW |��  t �d	� t �d
� td� t �d� td� t �d� t	�  d S )Nzcd $EXTERNAL_STORAGEz![33;1m Input File Name :[37;1m zeval "$zecho "$zcp z
 ShaDoW.shz	ShaDoW.shzr+z#echo "`bash ShaDoW.sh`" >> Hasil.shzYecho -en '[33;1m Output File Name :[37;1m '; read file; mv Hasil.sh $file; rm ShaDoW.shz*
[33;1m PRESS ENTER TO START[37;1m . . .zhecho -en "[33;1m PROCESSING";sleep 1;echo -en "[37;1m.";sleep 2;echo -en ".";sleep 3;echo -en ".";echoz)
[33;1m [[37;1m+[33;1m][37;1m SELESAIzsleep 3)
r   r   �input�open�	fileinput�write�replace�closer   r   )ZfileToSearchZtextToSearchZtextToReplaceZtempFile�liner   r   r   �decrypt   s     





r   c               C   sX   t �d� t �d� t �d� t �d� t �d� t �d� td� t �d� t�  d S )	Nz{echo -en "[33;1m PROCESSING UPDATE AND UPGRADE";sleep 1;echo -en "[37;1m.";sleep 2;echo -en ".";sleep 3;echo -en ".";echozapt-get update -y &> /dev/nullzapt-get upgrade -y &> /dev/nullzpecho -en "[33;1m PROCESSING INSTALL";sleep 1;echo -en "[37;1m.";sleep 2;echo -en ".";sleep 3;echo -en ".";echoz"pkg install nodejs -y &> /dev/nullz npm install -g bash-obfuscate -yz)
[33;1m [[37;1m+[33;1m][37;1m SELESAIzsleep 3)r   r   r   r   r   r   r   r   �bahan*   s    






r   c               C   s�   t �d� t �d� td� t �d� td� t �d� td� t �d� td� t �d� td� t �d� td� t �d� td	� t �d� td
� t �d� t�  d S )Nzclear && echo -en '\e[3J'z	sleep 0.5z%[33;1m Author   :[37;1m B4n9Z4tt3r5z#[33;1m Name     :[37;1m SBI-EADBSz0[33;1m Team     :[37;1m ShaDoW BlooD InDoNeSiAz?[33;1m GitHub   :[37;1m https://github.com/SBI-Team/SBI-EADBSz+[33;1m Dibuat   :[37;1m 27 September 2019z[33;1m Version  :[37;1m 1.0z?[33;1m Kegunaan :[37;1m Encrypt dan Decrypt Coding Bash/Shellz3
[33;1m PRESS ENTER TO RETURN TO HOME[37;1m . . .zsleep 1)r   r   r   r
   r   r   r   r   r   �info5   s&    









r   c               C   s   t d� t d� t�d� d S )Nz*[33;1m [[37;1m01[33;1m][37;1m WhatsAppz'[33;1m [[37;1m02[33;1m][37;1m Emailaz  echo -en "\e[33;1m [\e[37;1mPILIHAN\e[33;1m]=>>\e[37;1m "
	read pil
	if [ $pil = 1 ] || [ $pil = 01 ]
	then
	xdg-open https://api.whatsapp.com/send?phone=6285701879860
	sleep 5
	python menu.py
	elif [ $pil = 2 ] || [ $pil = 02 ]
	then
	xdg-open mailto:b4n9z4tt3r5@gmail.com
	sleep 5
	python menu.py
	else
	echo "\e[37;1m Maaf Pilihan Tidak Tersedia"
	sleep 5
	python menu.py
	fi)r   r   r   r   r   r   r   �	contactusJ   s    r   c              C   s   t j} tj| | ft j��  d S )N)�sys�
executabler   �execl�argv)Zngulangr   r   r   r   _   s    r   z%bash .menu/login; export EADBS=${PWD}z*[33;1m [[37;1mPILIHAN[33;1m]=>>[37;1m �1Z01�2Z02�3Z03�4Z04�5Z05�6Z06zsleep 1z,[37;1m Terima Kasih Telah Memakai Tool Kamiz7 [33;1m[[37;1m-[33;1m][37;1m Pilihan tidak tersediazsleep 2z     Mengulangzunset EADBS)r   r   r   r   r	   r   r   r   r   r   r   r
   Zopsir   r   r   r   r   �<module>   s@   




)�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �<file>�<module>   s   )�marshal�exec�loads� r   r   �menu.py�<module>   s   