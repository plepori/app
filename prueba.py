from sys import path # usamos para importar modulos propios
path.append('C:\\Users\\EXT84085\\Desktop\\Python') # ruta del modulo que realizamos

#from app import *
#from flask import Flask, render_template
import ipaddress
from bs4 import BeautifulSoup
import xmltodict, json


"""###########################################################################################################################
Codigo del XML del cual se extrae la información
    <managedObject class="com.nokia.srbts.tnl:IPADDRESSV4" 
    distName="MRBTS-50149/TNLSVC-1/TNL-1/IPNO-1/IPIF-6/IPADDRESSV4-1" version="TNL21B_2105_002" operation="create">
      <p name="ipAddressAllocationMethod">MANUAL</p>
      <p name="localIpAddr">10.231.168.10</p>
      <p name="localIpPrefixLength">30</p>
	</managedObject>
"""###########################################################################################################################

filename = 'C:\\Users\\EXT84085\\Desktop\\Python\\server\\SCF.xml'  # Ruta del archivo

def eth(a):
	tag = [i.getText() for  i in  a.find_all("p")] 
	#print(tag)

 
def imprimir(datos):
	print("#"*40,end="# \n")
	print("#"," "*10, " Direcciones IP "," "*10, end="# \n")
	print("#"*40,end="# \n")
	print(" Control Plane LTE ", " "*3, datos['dir ip 1'])
	print(" User Plane LTE    ", " "*3, datos['dir ip 2'])
	print(" Control Plane UMTS", " "*3, datos['dir ip 3'])
	print(" User Plane UMTS   ", " "*3, datos['dir ip 4'])
	print(" CP/UP GSM         ", " "*3, datos['dir ip 5'])
	print(" IP de gestion     ", " "*3, datos['dir ip 6'])
	print(" Sync Plane ToP    ", " "*3, datos['dir ip 7'])


def extraccion(dato):
	#tag = {	i : i.getText() for  i in  dato.find_all("p")}	
	ip = [i.getText() for  i in  dato.find_all("p")]	
	del ip[0]
	ip = "/".join(map(str, ip))
	return ip

def clasificar_ip(s):
	var = 0
	dic = {}
	for i in range(len(s)):
			var = s[i]
			var = var[:6]
			if var == '10.227':
				dic['dir ip 1'] = s[i]
			elif var == '10.230':
				dic['dir ip 2'] = s[i]
			elif var == '10.237':
				dic['dir ip 3'] = s[i]
			elif var == '10.236':
				dic['dir ip 4'] = s[i]
			elif var == '10.234':
				dic['dir ip 5'] = s[i]
			elif var == '10.231':
				dic['dir ip 6'] = s[i]
			elif var == '10.232':
				dic['dir ip 7'] = s[i]
			else: break
	return dic




with open(filename,"r")	as page:
	plan = BeautifulSoup(page,'xml',from_encoding='utf-8')			#

mrbts = plan.find(class_="com.nokia.srbts:MRBTS").getText()  	# Busca dentro del SCF etiqueta "com.nokia.srbts:MRBTS" 
print("Cell ID ", mrbts)  										# Imprimimos el Cell ID

ip = [extraccion(dato) for dato in plan.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4")]
print(ip)



'''

dic = clasificar_ip(ip)
puerto = [eth(dato_1) for dato_1 in plan.find_all(class_="com.nokia.srbts.tnl:ETHLK")]
print(puerto)
#server(puerto)
imprimir(dic)
#server(dic)
'''
'''	
with open(data, 'r') as myfile:
    obj = xmltodict.parse(myfile.read())
print(json.dumps(obj))

a = open("scf.json","a")
a.write(json.dumps(obj))
a.close()
'''


	
	

#	print(ip)
	#input("ingrese un valor para terminar")
"""
def extraccion(dato):
	ip = {info : info.getText() for info in dato.find_all('p')}
		#print (ip)
#	obs_string =[extraccion(dato) for dato in soup.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4")] #  Busqueda de la dir IP


	obs_string = {dato['distName'] : dato.getText() for dato in soup.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4")} #  Busqueda de la dir IP
#	dic = { 'IP Addres' : dato.getText() for dato in obs_string }
	contenido = soup.find('managedObject').getText()
#	version = { 'version' :  obs_string['version']}
#	ip = {}
"""