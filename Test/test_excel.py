import xlrd
from openpyxl import *
import pandas   as pd


filename = 'C:\\Users\\EXT84085\\Desktop\\Python\\server\\CO.xlsx'  # Ruta del archivo

input_cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

df = pd.read_excel(filename, sheet_name = "Configuracion-Tareas-Materiales", header=2)

print(df.shape)

tit_col = df.columns.ravel()

print(tit_col)

conf = {}
b = {}
a = 0
for i in tit_col:
    if ((i == '2G') or (i == '2G.1') or (i == '3G') or (i == '3G.1') or (i == '4G') or (i == '4G.1') or (i == '4G.2') or (i == '4G.3') or (i == '4G.4') or (i == '4G.5')):
        a = df[i].head(6).tolist()
        conf[i]=a

'''
    if ((i == '2G') or (i == '2G.1') or (i == '3G') or (i == '3G.1') or (i == '4G') or 
        (i == '4G.1') or (i == '4G.2') or (i == '4G.3') or (i == '4G.4') or (i == '4G.5')):
        a = df[i].head(6).tolist()
        print(a)
        b = {'Tecnologia': i, 'Banda': a[0],'Solucion':a[1], 'Ran':a[2]}
    conf[i]=b
print(conf)
'''





#print(df['2G'].head(6).tolist())

#print(df.head(9))






'''
wb = load_workbook(filename)
wb.active
#print (wb.sheetnames)
sheet_ranges = wb['Prueba']
for i in range(0,9):
    var = 
    #print((j))

cell_range = sheet_ranges['A1'].value
print(cell_range)
'''