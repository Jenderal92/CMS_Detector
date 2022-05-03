#CMS FILTER
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
#####################################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
   - Jamet Crew aka KNTL Megalodon - 
      - CMS CHECKER !!! - Jenderal92 -
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[Online Tools : http://secpriv8.com\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
   \033[32m>----------------------------------<
   [-] 1. CMS Wordpress
   [-] 2. CMS Joomla
   [-] 3. CMS Laravel
   [-] 4. CMS  OpenCart
   [-] 5. CMS Drupal
   [-] 6. CMS Prestashop
   [-] 7. CMS Magneto 
   [-] 8. CMS vBulletin
   [-] 9. CMS osCommerce
   [-] 10. Scanning All !!! 

   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

pilihmas = raw_input(':~# \033[34mChoose\033[32m Number : ')

########JANCOKSURAIMU####
users = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}

def cms_wordpress(url):
	try:
		cek = requests.get(url+'/xmlrpc.php?rsd', headers=users, timeout=15)
		if 'Wordpress' in cek.text.encode('utf-8'):
			print(kuning + '[Found Cms Wordpress --> ]' + ijo + url)
			open('cms/wp.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found Cms Wordpress --> ]' + abang + url)
	except:
		pass
	pass

def cms_joomla(url):
	try:
		ceks = requests.get(url+'/administrator/index.php', headers=users, timeout=15).text
		if 'Joomla!' in ceks and '/language/en-GB/en-GB.xml' in ceks:
			print(kuning + '[Found Cms Joomla --> ]' + ijo + url)
			open('cms/joomla.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found Cms Joomla --> ]' + abang + url)
	except:
		pass
	pass

def cms_laravel(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'X-XSRF-TOKEN' in get_source and 'XSRF-TOKEN' in get_source:
			print(kuning + '[Found Laravel Cookies --> ]' + ijo + url)
			open('cms/laravel.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found Laravel Cookies --> ]' + abanb + url)
	except:
		pass
	pass

def cms_opencart(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'index.php?route=common/home' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS Opencart --> ]' + ijo + url)
			open('cms/opencart.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS Opencart--> ]' + abanb + url)
	except:
		pass
	pass

def cms_drupal(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'sites/default' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS Drupal --> ]' + ijo + url)
			open('cms/drupal.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS Drupal--> ]' + abanb + url)
	except:
		pass
	pass

def cms_prestashop(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'sites/default' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS Prestashop --> ]' + ijo + url)
			open('cms/prestashop.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS Prestashop--> ]' + abanb + url)
	except:
		pass
	pass

def cms_magneto(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'Mage.Cookies' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS Magneto --> ]' + ijo + url)
			open('cms/magneto.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS Magneto--> ]' + abanb + url)
	except:
		pass
	pass

def cms_vBulletin(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'vBulletin' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS vBulletin --> ]' + ijo + url)
			open('cms/vBulletin.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS vBulletin--> ]' + abanb + url)
	except:
		pass
	pass

def cms_osCommerce(url):
	try:
		get_source = requests.get(url, headers=users, timeout=15).cookies
		if 'osCommerce' in ceks.text.encode('utf-8'):
			print(kuning + '[Found CMS osCommerce --> ]' + ijo + url)
			open('cms/osCommerce.txt', 'a').write(url+'\n')
		else:
			print(kuning + '[Not Found CMS osCommerce--> ]' + abanb + url)
	except:
		pass
	pass

def allgas(url):
	try:
		cms_wordpress(url)
		cms_joomla(url)
		cms_laravel(url)
		cms_opencart(url)
		cms_drupal(url)
		cms_prestashop(url)
		cms_magneto(url)
		cms_vBulletin(url)
		cms_sCommerce(url)
	except:
		pass

######MENGONTOL#####
def Main():
	try:
		if pilihmas =='1':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev1 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_wordpress, rev1)
		if pilihmas =='2':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev2 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_joomla, rev2)
		if pilihmas =='3':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev3 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_laravel, rev3)
		if pilihmas =='4':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev4 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_opencart, rev4)
		if pilihmas =='5':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev5 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_drupal, rev5)
		if pilihmas =='6':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev6 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_prestashop, rev6)
		if pilihmas =='7':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev7 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_magneto, rev7)
		if pilihmas =='8':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev8 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_vBulletin, rev8)
		if pilihmas =='9':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev9 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(cms_vBulletin, rev9)
		if pilihmas =='10':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev10 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(allgas, rev10)
	except:
		pass

if __name__ == '__main__':
	Main()