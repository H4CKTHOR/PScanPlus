#Nəyə girmisəne ala bura?
#Created by: H4CKTHOR
#My First Python Tool .d

from socket import *
from threading import *
import optparse
import os 

os.system('clear')

banner=("""
'##::::'##::::'##::::::::::::'######:::::'##:::'##::::'########::::'##::::'##:::::'#######:::::'########::
 ##:::: ##:::: ##:::'##:::::'##... ##:::: ##::'##:::::... ##..::::: ##:::: ##::::'##.... ##:::: ##.... ##:
 ##:::: ##:::: ##::: ##::::: ##:::..::::: ##:'##::::::::: ##::::::: ##:::: ##:::: ##:::: ##:::: ##:::: ##:
 #########:::: ##::: ##::::: ##:::::::::: #####:::::::::: ##::::::: #########:::: ##:::: ##:::: ########::
 ##.... ##:::: #########:::: ##:::::::::: ##. ##::::::::: ##::::::: ##.... ##:::: ##:::: ##:::: ##.. ##:::
 ##:::: ##::::...... ##::::: ##::: ##:::: ##:. ##:::::::: ##::::::: ##:::: ##:::: ##:::: ##:::: ##::. ##::
 ##:::: ##:::::::::: ##:::::. ######::::: ##::. ##::::::: ##::::::: ##:::: ##::::. #######::::: ##:::. ##:
..:::::..:::::::::::..:::::::......::::::..::::..::::::::..::::::::..:::::..::::::.......::::::..:::::..::
---------------------------------------------------------------------------------------------------------- 
""")

print(banner)

media=("\33[31mSocial Media: \nInstagram: https://www.instagram.com/h4ckthor/ \nYoutube: https://www.youtube.com/channel/UCDx7p7M6WRP5iEQh_gtbw5A \nLinkedin: https://linkedin.com/in/nij4trahimov\33[0m");

os.system('sleep 2')

print(media)

print()

def portScan(targethost,targetport):
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.connect((targethost,targetport))
        print(f"[+] {targetport} => Port Açığdır!")
    except:
        print(f"[-] {targetport} => Port Bağlıdır!")
    finally:
        sock.close()



def hostScan(targethost,targetports):
    try:
        targetIp = gethostbyname(targethost)
        print("*"*15,"*"*len(targetIp),sep="")
        print(f"[+] Ip Adressi: {targetIp}")
    except:
        print(f"[-] Host Tapılmadı!: {targethost}")

    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=portScan,args=(targethost,int(targetport)))
            t.start()
        except ValueError:
            print("<Xeta!>")

def main():
    parser = optparse.OptionParser("python3 Pscan+.py -H google.com -p 21,443")
    parser.add_option("-H", dest="targetHost", type="string", help="Hedef Ip Adress")
    parser.add_option("-p", dest="targetPort", type="string", help="(,) veya (,)'süz port yaz!")
    (options,args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    if (targetHost == None) or (targetPorts[0] == None):
        print(parser.usage)
        exit(0)
    hostScan(targetHost,targetPorts)

if __name__ == "__main__":
    main()
