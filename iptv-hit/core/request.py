"""
This file is part of Scdev's iptvhit.  Scdev's iptvhit is free software: 
you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
Scdev's iptvhit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.You should have received a copy of the GNU General Public License along with Scdev's iptvhit.
If not, see <https://www.gnu.org/licenses/>. 
"""

import requests
from colorama import Fore, Back, Style

#Sending http Requests -----------------------------------------------------------------------------------
def send_requests(a,b):
     response = requests.get('http://'+a+'/get.php',params=b)

     


#Getting Data from url -----------------------------------------------------------------------------------    
     if response.status_code==200:
        with open("hits.txt", "w") as f:
          f.write("Active: "+response.url)   
          print(Fore.LIGHTGREEN_EX+str(response.status_code)+"Active,  SUCCESSFUL HIT: "+response.url)
     else:
         print(Fore.RED+str(response.status_code)+"Not Active,  UNSUCCESSFUL HIT: "+response.url)
     
  