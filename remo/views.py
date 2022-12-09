from django.shortcuts import render
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views import View  
import xml.etree.ElementTree as ET

#filename = 'C:\\Users\\EXT84085\\Desktop\\Python\\server\\prueba\\SCF\\SCF.xml'  # Ruta del archivo
'''
def home(request):
    with open(filename,"r")	as page:
        plan = BeautifulSoup(page,'xml',from_encoding='utf-8')			#
        #print(plan)
    return render(request, "remo/home.html", {"plan":plan})
# Create your views here.

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'remo/index.html', {
            'uploaded_file_url': uploaded_file_url, 
        })
    return render(request, 'remo/index.html')
'''

class home(View):

    template_name = 'remo/home.html'

    def get(self,request):
        return render(request, 'remo/home.html')

    def post(sefl,request):
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        with open(filename,"r") as page:
            plan = BeautifulSoup(page,'xml',from_encoding='utf-8')
        fs.delete(filename)
        return render(request, "remo/home.html", {"plan":plan})

