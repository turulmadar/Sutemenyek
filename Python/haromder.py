print("Zsitnyák Ádám \n\t Háromszög Ellenőrzése")

sideA = 0
sideB = 0
sideC = 0

sideA = int( input(" A oldal:"))
sideB = int( input(" B oldal:"))
sideC = int( input(" C oldad:"))


#int(sideaA) konverzió

"""
 A < B + C
 B < A + C
 C < A + B
"""

if  not (sideA < sideB + sideC and
    sideB < sideA + sideC and
    sideC < sideA + sideC )  :
	
	print("Nem háromszög")

else:
	
	result = sideA+ sideB+ sideC
	print("Kerület:" ,result)
