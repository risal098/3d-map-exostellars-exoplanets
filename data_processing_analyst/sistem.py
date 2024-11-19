import pandas as pd
import math

def radians(degree):
    return degree * math.pi / 180

def sin(degree):
    return math.sin(radians(degree))  # Closing parenthesis added

def cos(degree):
    return math.cos(radians(degree))  # Closing parenthesis added

def derajatxyz(panjang, theta_deg, phi_deg):
    # Convert angles to radians first
    theta_rad = radians(theta_deg)
    phi_rad = radians(phi_deg)

    # Use the converted radian values
    x = panjang * cos(theta_deg) * sin(phi_deg)
    y = panjang * sin(theta_deg) * sin(phi_deg)
    z = panjang * cos(phi_deg)

    return [x, y, z]

file = 'system2.xlsx'
sheet1 = pd.read_excel(file, sheet_name = 6)
xcor=[]
ycor=[]
zcor=[]
for i in range(len(sheet1)):
	tempcor=derajatxyz(sheet1["sy_dist (parsec)"][i],
										 sheet1["ra"][i],
										 sheet1["dec"][i])
	xcor.append((round(tempcor[0],2)))
	ycor.append((round(tempcor[1],2)))
	zcor.append((round(tempcor[2],2)))

sheet1["xcor"]=xcor
sheet1["ycor"]=ycor
sheet1["zcor"]=zcor

sheet1.to_excel('tesout.xlsx')

                
