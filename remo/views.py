from django.shortcuts import render
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
from django.views import View  
from remo.funcion import *
 

class home(View):

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
        
        fs.delete(filename) 
        fs.delete(filename2)
        
        scf = datos(plan)           #instanciamos la clase datos
        cid = scf.mrbts()           #llamamos a la funcion mrbts
        ip = scf.buscar()
        port = scf.puertos()
        vlan = scf.vlanid()           

        scf2 = datos(plan2)           #instanciamos la clase datos
        cid2 = scf2.mrbts()           #llamamos a la funcion mrbts
        ip2 = scf2.buscar()
        port2 = scf2.puertos()
        vlan2 = scf2.vlanid()

        return render(request, "remo/home.html", {"cid":cid,"ip":ip, "port":port, "vlan":vlan, "cid2":cid2,"ip2":ip2, "port2":port2, "vlan2":vlan2})



