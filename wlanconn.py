#!/usr/bin/python3

import sys
import subprocess
from getpass import getpass


def DoConn(wifiIn):
    passwdFlag = True         
    historyList = subprocess.getoutput("ls /etc/sysconfig/network-scripts/keys* | awk -F'/' '{print $5}'")  
    keyId = historyList.split('\n')  
    for i in range(len(keyId)):        
        if str(strTxt[wifiIn]) in str(keyId[i])[5:]:                   
            passwdFlag = False
            break

    if passwdFlag == True:        
        passwd = getpass(prompt='Type Your Password -> ')
        subprocess.getoutput(f'nmcli dev wifi connect {str(strTxt[wifiIn])} password {passwd}')
    else:        
        subprocess.getoutput(f'nmcli connection up {str(strTxt[wifiIn])}')    
    

wlanList = subprocess.getoutput("nmcli dev wifi list | awk '{print $1}'")
strTxt = wlanList.split('\n')
for i in range(len(strTxt)):
    print(f'ID# -> {i} Network SSID -> {str(strTxt[i])}')

wifiIn = int(input('Connect To A WiFi Network Using ID ( 99 to Exit ) -> '))
sys.exit if wifiIn == 99 else DoConn(wifiIn)