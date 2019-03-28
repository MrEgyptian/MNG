import itertools
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()

etisalat_msg='''/
\033[40mChoose The Number:-
        \033[36m [1] \033[93m 0111
	\033[36m [2] \033[93m 0112
        \033[36m [3] \033[93m 0110
	\033[36m [4] \033[93m 0114
	\033[36m [5] \033[93m 0115
	\033[36m [6] \033[93m 0119
'''
ong_msg='''/
\033[40mChoose The Number:-
        \033[36m [1] \033[93m 0122
	\033[36m [2] \033[93m 0121
        \033[36m [3] \033[93m 0127
	\033[36m [4] \033[93m 0128
	\033[36m [5] \033[93m 0120
'''
om="\033[92mMNG\033[91m> \033[92\033[47m"
menu1='''
        \033[40mHow can we help:-
        \033[36m [1] \033[93m Genrate
	\033[36m [2] \033[93m Fb Bruteforce
        \033[36m [3] \033[93m About
        \033[36m [0] \033[91m Exit
        '''
fbbanner='''
\033[91m
 ▄▄▄▄▄▄ █             █                      ▄
 █      █▄▄▄          █▄▄▄    ▄ ▄▄  ▄   ▄  ▄▄█▄▄   ▄▄▄
 █▄▄▄▄▄ █▀ ▀█         █▀ ▀█   █▀  ▀ █   █    █    █▀  █
 █      █   █   ▀▀▀   █   █   █     █   █    █    █▀▀▀▀
 █      ██▄█▀         ██▄█▀   █     ▀▄▄▀█    ▀▄▄  ▀█▄▄▀
'''
banner='''
\033[92m    __  ____   ________
\033[92m   /  |/  / | / / ____/         \033[91m#######################
\033[92m  / /|_/ /  |/ / / __           \033[91m#This tool is a gift  #
\033[92m / /  / / /|  / /_/ /           \033[91m#To Greengoblinsteam♥ #
\033[92m/_/  /_/_/ |_/\____/            \033[91m#    By:Dark  Geek    #
                                \033[91m# ------Enjoy-------- #
\033[93mMobile Number Genrator          \033[91m#######################
        \033[95mGitHub: https://github.com/midasdaro/
'''
networklist='''\033[92m\033[40m
Choose The Network:-
\033[93m[1] \033[92mEtisalat
\033[93m[2] \033[93mOrange
\033[93m[3] \033[91mVodafone
\033[93m[4] \033[35mWe
\033[93m[0] \033[41m\033[30mExit'''
chrs="1234567890"
orange="012"
etisalat="011"
we="015"
vodafone="010"
def tel(file_name,network,net_num):
        arq =open(file_name, 'w')
        for i in range(7, 8):
                for j in itertools.product(chrs, repeat=i):
                        temp = ''.join(j)
                        print("\033[92m\033[40m"+network+net_num+"-"+temp)
                        arq.write(network+net_num+temp + '\n')
        arq.close()

def netselect(net):
	if (net=="1"):
		net1=etisalat
		pass
	elif (net=="2"):
                net1=orange
                pass
	elif (net=="3"):
		net1=vodafone
		pass
	elif (net=="4"):
		net1=we
		pass
	else:
                net1=etisalat
	return net1
def etisalat_sel(eti):
	if(eti=="1"):
		val="1"
		pass
	if(eti=="2"):
		val="2"
		pass
	if(eti=="3"):
		val="0"
		pass
	if(eti=="4"):
		val="4"
		pass
	if(eti=="5"):
		val="5"
		pass
	elif(eti=="6"):
		val="9"
		pass
	return val

def orange_sel(ong,aval):

	if(ong=="1"):
		aval="2"
		pass
	if(ong=="2"):
		aval="1"
		pass
	if(ong=="3"):
		aval="7"
		pass
	if(ong=="4"):
		aval="8"
		pass
	if(ong=="5"):
		aval="0"
		pass

