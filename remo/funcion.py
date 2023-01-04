
"""###########################################################################################################################
CODIGO XML - INFORMACIÓN A BUSCAR
    <managedObject class="com.nokia.srbts.tnl:IPADDRESSV4" 
    distName="MRBTS-50149/TNLSVC-1/TNL-1/IPNO-1/IPIF-6/IPADDRESSV4-1" version="TNL21B_2105_002" operation="create">
      <p name="ipAddressAllocationMethod">MANUAL</p>
      <p name="localIpAddr">10.231.168.10</p>
      <p name="localIpPrefixLength">30</p>
	</managedObject>
###########################################################################################################################"""

#def prueba(datos):

    

'''
#-INFORMACIÓN DE PUERTOS 

def eth(a):
	tag = [i.getText() for  i in  a.find_all("p")]
	return(tag)

#-CLASIFICA LAS DIR IP
def clasificar_ip(s):
	var = 0
	dic = {}
	for i in range(len(s)):
			var = s[i]
			var = var[:6]
			if var == '10.227':
				dic['CP_LTE'] = s[i]
			elif var == '10.230':
				dic['UP_LTE'] = s[i]
			elif var == '10.237':
				dic['CP_UMTS'] = s[i]
			elif var == '10.236':
				dic['UP_UMTS'] = s[i]
			elif var == '10.234':
				dic['CPUP_GSM'] = s[i]
			elif var == '10.231':
				dic['Gestion'] = s[i]
			elif var == '10.232':
				dic['Sync'] = s[i]
			else: break
	return dic

	print(" Control Plane LTE ", " "*3, datos['dir ip 1'])
	print(" User Plane LTE    ", " "*3, datos['dir ip 2'])
	print(" Control Plane UMTS", " "*3, datos['dir ip 3'])
	print(" User Plane UMTS   ", " "*3, datos['dir ip 4'])
	print(" CP/UP GSM         ", " "*3, datos['dir ip 5'])
	print(" IP de gestion     ", " "*3, datos['dir ip 6'])
	print(" Sync Plane ToP    ", " "*3, datos['dir ip 7'])

#-EXTRACCION DE DIR IP Y LAS GUARDA EN UNA LISTA
def extraccion(dato):
	#tag = {	i : i.getText() for  i in  dato.find_all("p")}	
	ip = [i.getText() for  i in  dato.find_all("p")]	
	del ip[0]
	ip = "/".join(map(str, ip))
	return ip

#-APP

#### SOLUCIONAR EL TEMA DE CARGAR SCF ####

with open(filename,"r")	as page:
	plan = BeautifulSoup(page,'xml',from_encoding='utf-8')			#
	mrbts = plan.find(class_="com.nokia.srbts:MRBTS").getText()  	# Busca dentro del SCF etiqueta "com.nokia.srbts:MRBTS" 
	print("Cell ID ", mrbts)  										# Imprimimos el Cell ID

	ip = [extraccion(dato) for dato in plan.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4")]
	print(ip)

	dic = clasificar_ip(ip)
	print(dic)
	
	puerto = [eth(dato_1) for dato_1 in plan.find_all(class_="com.nokia.srbts.tnl:ETHLK")]
	print(puerto)
	server(mrbts,dic)
'''