#!/bin/python3.7
#By: Dark Geek
#Ver 1.0
#Egyption Mobile Number Genrator
###################################################
import os
import var
from os import chdir
from os import mkdir
from var import *
import itertools
print (banner)
def menu():
	print (menu1)
	opt=str(input(om))
	if (opt=="1"):
		print(networklist)
		netw=str(input(om))
		nw=netselect(netw)
		if(nw=="011"):
			print(etisalat_msg)
			enn=input(om)
			nn=etisalat_sel(enn)
			pass
		if(nw=="012"):
			print(ong_msg)
			onn=input(om)
			#1nn=
		file=str(input("Enter file name: "))
		tel(file,nw,nn)
		pass
	elif (opt=="3"):
		os.system("bash about.sh")
		pass
	elif (opt=="2"):
		os.system("python bruteforce.py")
		pass
	elif (opt=="0" or opt=="exit"):
		exit
	else:
		print("\033[40mPlease Choose correctly")
		restart_program()
menu()
