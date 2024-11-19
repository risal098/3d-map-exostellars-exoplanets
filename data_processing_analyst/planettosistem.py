import pandas as pd
import json
import math
'''
0
1=
3000
2=
7000
3=
12000
4=
18000
5=
26000
6=
80000
7=
....
'''
def ttype(xcor):
	dist=xcor*10
	if dist>130000:
		return 7
	elif dist>80000:
		return 6
	elif dist>20000:
		return 5
	elif dist>9000:
		return 4
	elif dist>6000:
		return 3
	elif dist>3000:
		return 2
	elif dist>0:
		return 1
def ptype(bmas,rade,disfstar):
	volume=(rade**3)*math.pi*4/3
	density=bmas/volume
	if density>5:
		return 0 #rocky
	elif density>1.7 and density<5 and disfstar<15000:
		return 1 #water
	elif density>1.7 and density<5 and disfstar>15000:
		return 2 #icy
	elif density<=1.7  :
		return 3 #gas
def int_to_color(value, min_value=1, max_value=1000):
    normalized_value = (value - min_value) / (max_value - min_value)
    if normalized_value < 0:

        return '#ff0000'

    elif normalized_value > 1:

     
        return '#0000ff'

    else:

        r = int(255 * (1 - normalized_value))

        g = 0

        b = int(255 * normalized_value)


        return '0x{:02x}{:02x}{:02x}'.format(r, g, b)
def writeJsonfile(data,filename):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4, default=str)
		
file = 'planet plain.xlsx'
sheet1 = pd.read_excel(file, sheet_name = 3)
hostlist=pd.read_excel(file, sheet_name = 4)
#print(sheet1)
sheet1=sheet1.fillna({'pl_orbper': 607})
sheet1=sheet1.fillna({'pl_bmasse': 949})
sheet1=sheet1.fillna({'pl_rade': 8})
systemplanet={}
for i in range(len(hostlist["hostname"])):
	systemplanet[hostlist["hostname"][i]]={}
for i in range(len(sheet1["pl_name"])):
#distance from star,orbit speed,dis method,dis year,dis facility,orbital period day,color,type planet,type texture in planet
	systemplanet[sheet1["hostname"][i]][sheet1["pl_name"][i]]=[
	sheet1["pl_orbper"][i]*10,#distance from star 0
	0.001/sheet1["pl_orbper"][i],#orbit speed 1
	sheet1["discoverymethod"][i],#dis method 2
	sheet1["disc_year"][i],#dis year 3
	sheet1["disc_facility"][i],#dis facility 4
	sheet1["pl_orbper"][i],#orbital period day 5
	int_to_color(sheet1["pl_orbper"][i]),#color 6
	ptype(sheet1["pl_bmasse"][i],sheet1["pl_rade"][i],sheet1["pl_orbper"][i]*10),#type planet 7
	ttype(sheet1["pl_orbper"][i]*10)]#type texture in planet 8
#OGLE-2012-BLG-0026L b
writeJsonfile(systemplanet,"systemplanet.json")

