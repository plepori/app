from django.shortcuts import render
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views import View  
from remo.funcion import * 


#filename = 'C:\\Users\\EXT84085\\Desktop\\Python\\server\\prueba\\SCF\\SCF.xml'  # Ruta del archivo

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
                else: break
        return dic

    
    def extraccion(self,dato):
        self.ip = [i.getText() for  i in  dato.find_all("p")]	
        del self.ip[0]
        self.ip = "/".join(map(str, self.ip))
        return self.ip

    def buscar(self):
        for dato in self.plan.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4"):
            ip = self.extraccion(dato)
            self.a.append(ip)
        #self.a = [self.extraccion(dato) for dato in self.plan.find_all(class_="com.nokia.srbts.tnl:IPADDRESSV4")]
        self.a = self.clasificar_ip(self.a)
        return self.a

    def mrbts(self):
        return self.plan.find(class_="com.nokia.srbts:MRBTS").getText()
    
    def eth(self,b):
        #ethp=[]
        ethp = [i.getText() for  i in  b.find_all("p")]
        return ethp
    
    def puertos(self):
        puerto = [self.eth(i) for i in self.plan.find_all(class_="com.nokia.srbts.tnl:ETHLK")]
        return puerto
 
        


class home(View):

    template_name = 'remo/home.html'
    def get(self,request):
        return render(request, 'remo/home.html')

    def post(sefl,request):
        myfile = request.FILES['myfile']
        myfile2 = request.FILES['myfile2']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        filename2 = fs.save(myfile2.name, myfile2)
        with open(filename,"r") as page:
            plan = BeautifulSoup(page,'xml',from_encoding='utf-8')
        with open(filename2,"r") as page:
            plan2 = BeautifulSoup(page,'xml',from_encoding='utf-8')        
        scf = datos(plan)           #instanciamos la clase datos
        cid = scf.mrbts()           #llamamos a la funcion mrbts
        ip = scf.buscar()
        port = scf.puertos()           

        scf2 = datos(plan2)           #instanciamos la clase datos
        cid2 = scf2.mrbts()           #llamamos a la funcion mrbts
        ip2 = scf2.buscar()


        fs.delete(filename)
        fs.delete(filename2)
        return render(request, "remo/home.html", {"cid":cid,"ip":ip, "port":port, "cid2":cid2,"ip2":ip2})



