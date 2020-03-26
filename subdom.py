#!/usr/bin/env python
#coding : utf-8 -*-
#python3

import requests, os, sys, time, datetime

os.system("clear")
print ("""\x1b[00m\x1b[96m ╔══════════════════════════════╦════════════════╗
 ║ \x1b[1;91m╦ ╦ ╦   ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗  \x1b[1;96m║\x1b[41;92m    KMB • ID    \x1b[0m\x1b[1;96m║
 ║ \x1b[1;91m║ ╚-╣ • ╠╣  ║   ║   ║ ║ ║    \x1b[1;96m╠\x1b[41;96m════🛡️══════🛡️════\x1b[0m\x1b[96m╣
 ║ \x1b[1;97m╩╝  ╩   ╚═╝ ╩   ╩   ╚═╝ ╩ \x1b[93m404\x1b[1;96m║\x1b[1;47;91m© \x1b[94mcopyright \x1b[95m2019\x1b[0m\x1b[1;96m║
 ╚══════════════════════════════╩════════════════╝\033[97m\n
Code   = PYTHON 3
Contack = https://t.me/KMBL4
Upload   = 21-03-2020\033[0m""")
time.sleep(3)
os.system("clear")
Banner=(""" \033[95mB    \033[91m██\033[96m╗  \033[91m██\033[96m╗ \033[91m██████\033[96m╗ \033[91m███████\033[96m╗\033[91m████████\033[96m╗
\033[95m   U  \033[91m██\033[96m║  \033[91m██\033[96m║\033[91m██\033[96m╔═══\033[91m██\033[96m╗\033[91m██\033[96m╔════╝╚══\033[91m██\033[96m╔══╝
 \033[95m   G \033[91m███████\033[96m║\033[91m██\033[96m║   \033[91m██\033[96m║\033[91m███████\033[96m╗   \033[91m██\033[96m║
      \033[97m██\033[96m╔══\033[97m██\033[96m║\033[97m██\033[96m║   \033[97m██\033[96m║╚════\033[97m██\033[96m║   \033[97m██\033[96m║
      \033[97m██\033[96m║  \033[97m██\033[96m║╚\033[97m██████\033[96m╔╝\033[97m███████\033[96m║   \033[97m██\033[96m║
      ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝
\033[94m       🔛 TOOLS CHECKER \033[92mSUBDOMAIN 🔛
\x1b[1;41;96m💰NOOBY TEAM INDONESIA \x1b[1;47;91m KMB •ID {L4•ERROR}💰\x1b[0m""")


def main():
	os.system("clear")
	print (Banner)
	print (44*"\033[1;96m═")
	domain = input("\033[93m[✅] \033[94mDomain \033[97m(exc: facebook.com)\033[91m :\033[92m ")
	print ("\033[93m[❕] \033[94mPlease wait\033[91m !!!")
	print ("\033[93m[⏬] \033[94mProses\033[97m ... ")
	print (44*"\033[1;96m═")
	try:
		url = ("https://api.indoxploit.or.id/domain/{}".format(domain))
		data = requests.get(url).json()
		ambil_data = data['data']['subdomains']
		print ("\033[93m[🆗] \033[97mScan results \033[91m: ")
		for i in ambil_data:
			print("\033[92m"+i)
	
	except IOError:
		print ("\033[1;91m[!] No connection")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		main()
	except KeyError:
		print ("\033[1;91m[!] No Result")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		pilih(main)

def pilih(main):
	opsi = input("\033[1;91m[👍] \033[1;97mScan Domain other (try again) ? \033[1;92m[Y/N]\033[1;91m:\033[1;96m ")
	if opsi =="":
		print ("\033[1;91m[!] Wrong")
		pilih(main)
	elif opsi =="Y" or opsi =="y":
		os.system("clear")
		main()
	elif opsi =="N" or opsi =="n":
		print (" THANKS for Use... By KMB.ID") 
		os.system("exit")
	else:
		print ("\033[1;91m[!] Wrong")
		pilih(main)              
  
if __name__ == '__main__':
        main()
        pilih(main)