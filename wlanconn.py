#!/usr/bin/python3

import sys
import subprocess
from getpass import getpass


def DoConn(wifiIn):
    passwdFlag = True    
    historyList = subprocess.getoutput("ls /etc/sysconfig/network-scripts/keys* | awk -F'/' '{print $5}'")  
    keyId = historyList.split('\n')  
    for i in range(len(keyId)):        
        if str(keyId[i])[5:] == str(wlanArr[wifiIn])[2:-2]:            
            passwdFlag = False
            break

    if passwdFlag == True:        
        passwd = getpass(prompt='Type Your Password -> ')
        wifiConn = subprocess.getoutput(f'nmcli dev wifi connect {str(wlanArr[wifiIn])[2:-2]} password {passwd}')
    else:        
        wifiConn = subprocess.getoutput(f'nmcli connection up {str(keyId[i])[5:]}')    
    

strTxt = ''
k = 0
wlanArr = []

wlanList = subprocess.getoutput("nmcli dev wifi list | awk '{print $1}'")

for i in range(len(wlanList)):
    strTxt += wlanList[i]
    if wlanList[i] == '\n':                
        wlanArr.append(strTxt.splitlines())
        strTxt = ''
        k += 1

del wlanArr[0]
for i in range(len(wlanArr)):
    print(f'{i} -> {str(wlanArr[i])[2:-2]}')   

wifiIn = int(input('Connect In WiFi Network ( 99 to Exit ) -> '))
sys.exit if wifiIn == 99 else DoConn(wifiIn)