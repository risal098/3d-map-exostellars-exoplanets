import pandas as pd
import math
import json
import random
def writeJsonfile(data,filename):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=4, default=str)
file1 = 'complete.xlsx'
sistem = pd.read_excel(file1, sheet_name = 0)
file2 = 'planet plain.xlsx'
planet = pd.read_excel(file2, sheet_name = 3)
datasistem={"datasistem":{}}

for i in range(len(sistem["ra"])):
	mau=random.randint(1,9)
	datasistem[sistem["sy_name"][i]]={
			"nama_sistem":sistem["sy_name"][i],
			"nama_bintang":sistem["hostname"][i],
			"xcor":float(sistem["xcor"][i]),
			"ycor":float(sistem["ycor"][i]),
			"zcor":float(sistem["zcor"][i]),
			"jumlah_planet":int(sistem["sy_pnum"][i]),
			"jarak_parsec":sistem["sy_dist (parsec)"][i],
			"temperature":sistem["st_teff"][i]
			}
	if mau<5:
		datasistem[sistem["sy_name"][i]]["zcor"]=-(datasistem[sistem["sy_name"][i]]["zcor"])
writeJsonfile(datasistem,"tesout.json")
"""
{
"datasistem"=
	
		{
			"nama_sistem"={
			"nama_bintang"="<string>",
			"xcor"=<float>,
			"ycor"=<float>,
			"zcor"=<float>,
			"jumlah_planet"=<int>,
			"jarak_parsec"=<float> 
			}
		,
		...
		}
	
	
}
"""



