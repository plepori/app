
"""###########################################################################################################################
CODIGO XML - INFORMACIÓN A BUSCAR
    <managedObject class="com.nokia.srbts.tnl:IPADDRESSV4" 
    distName="MRBTS-50149/TNLSVC-1/TNL-1/IPNO-1/IPIF-6/IPADDRESSV4-1" version="TNL21B_2105_002" operation="create">
      <p name="ipAddressAllocationMethod">MANUAL</p>
      <p name="localIpAddr">10.231.168.10</p>
      <p name="localIpPrefixLength">30</p>
	</managedObject>
###########################################################################################################################"""

class datos:
    def __init__(self, plan):
        ip = 0
        self.plan = plan
        self.ip = ip
        a = []
        self.a = a

    def clasificar_ip(self,s):
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
                    dic['CP_UP_GSM'] = s[i]
                elif var == '10.231':
                    dic['GESTION'] = s[i]
                elif var == '10.232':
                    dic['SYNC_TOP'] = s[i]
                else: continue
        return dic

    
    def extraccion(self,dato):
        self.ip = [dato.find("p",{"name":"localIpAddr"}).getText()]
        self.ip.append(dato.find("p",{"name":"localIpPrefixLength"}).getText())
        self.ip = "/".join(map(str, self.ip))
        return self.ip

    def buscar(self):
        for dato in self.plan.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4"):
            ip = self.extraccion(dato)
            self.a.append(ip)
        self.a = self.clasificar_ip(self.a)
        return self.a

    def mrbts(self):
        return self.plan.find(class_="com.nokia.srbts:MRBTS").getText()
    
    def eth(self,b):
        ethp = [i.getText() for  i in  b.find_all("p")]
        return ethp
    
    def info_port(self,s):
        info = {}
        var = 0
        for i in s:
            for b in i:
                if 'EIF1' in b:
                    info[var] = 'EIF1'
                    var+=1
                if 'EIF2' in b:
                    info[var] = 'EIF2'
                    var+=1
                if 'EIF3' in b:
                    info[var] = 'EIF3'
                    var+=1
                if 'EIF4' in b:
                    info[var] = 'EIF4'
                    var+=1
                if 'EIF5' in b:
                    info[var] = 'EIF5'
                    var+=1
                if '100MBIT_FULL' in b:
                    info[var] = '100MBIT_FULL'
                    var+=1
                if '1000MBIT_FULL' in b:
                    info[var] = '1000MBIT_FULL'
                    var+=1
        return info 

    def puertos(self):
        puerto = [self.eth(i) for i in self.plan.find_all(class_="com.nokia.srbts.tnl:ETHLK")]
        dato_port = self.info_port(puerto)
        return dato_port

    def vlanid(self):
        vlan = [i.getText() for i in self.plan.find_all("p",{"name":"vlanId"})]
        return vlan

