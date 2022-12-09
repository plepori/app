from flask import Flask, render_template
from bs4 import BeautifulSoup

"""###########################################################################################################################
CODIGO XML - INFORMACIÓN A BUSCAR
    <managedObject class="com.nokia.srbts.tnl:IPADDRESSV4" 
    distName="MRBTS-50149/TNLSVC-1/TNL-1/IPNO-1/IPIF-6/IPADDRESSV4-1" version="TNL21B_2105_002" operation="create">
      <p name="ipAddressAllocationMethod">MANUAL</p>
      <p name="localIpAddr">10.231.168.10</p>
      <p name="localIpPrefixLength">30</p>
	</managedObject>
###########################################################################################################################"""

filename = 'C:\\Users\\EXT84085\\Desktop\\Python\\server\\prueba\\SCF\\SCF.xml'  # Ruta del archivo

with open(filename,"r")	as page:
    plan = BeautifulSoup(page,'xml',from_encoding='utf-8')			#
    print(plan)
    
