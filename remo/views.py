from django.shortcuts import render, get_object_or_404
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
from django.views import View  
from remo.funcion import *


class home(View):

    def get(self,request):
        return render(request, 'remo/home.html')

    def post(sefl,request):
        try:
            myfile = request.FILES['myfile']
            myfile2 = request.FILES['myfile2']
        except:
            return render(request,"remo/home.html")        
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
        qos = scf.sw()           

        scf2 = datos(plan2)           #instanciamos la clase datos
        cid2 = scf2.mrbts()           #llamamos a la funcion mrbts
        ip2 = scf2.buscar()
        port2 = scf2.puertos()
        vlan2 = scf2.vlanid()
        qos2 = scf2.sw()

        return render(request, "remo/home.html", {"cid":cid,"ip":ip, "port":port, "vlan":vlan, "qos":qos, "cid2":cid2,"ip2":ip2, "port2":port2, "vlan2":vlan2, "qos2":qos2})


class scf(View):
    def get(self, request):
        return render(request, "remo/scf.html")
    
    def post(self,request):
        try:
            myfile3 = request.FILES['myfile3']
        except:
            return render(request,"remo/scf.html")     
           
        fs = FileSystemStorage()

        filename3 = fs.save(myfile3.name, myfile3)
        df = pd.read_excel(filename3, sheet_name = "Configuracion-Tareas-Materiales", header=2)
        fs.delete(filename3)

        tit_col = df.columns.ravel()
        conf = {}
        a = 0

        for i in tit_col:
            if ((i == '2G') or (i == '2G.1') or (i == '3G') or (i == '3G.1') or (i == '4G') or 
                (i == '4G.1') or (i == '4G.2') or (i == '4G.3') or (i == '4G.4') or (i == '4G.5')):
                a = df[i].head(6).tolist()
                #conf[i]=a
                i = dict
                i = {'Tecnologia': a[0]}
        return render(request, "remo/scf.html", {"conf":conf})


        '''
        with open(filename3,"r") as page:
            plan = BeautifulSoup(page,'xml',from_encoding='utf-8')
        with open(filename2,"r") as page:
            plan2 = BeautifulSoup(page,'xml',from_encoding='utf-8')        
        
        fs.delete(filename) 
        fs.delete(filename2)'''
    

