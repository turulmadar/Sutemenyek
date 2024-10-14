import random
#[1,2,3,4,5] ind.0,1,2,3,4
#keresem a 6-ot de nincs benne ezért keresi de nics benne és keresi
#
myList=[]
pattern=217

for i in range (100):
	myList.append(random.randint(1,500))

i=0
while myList[i] != pattern and i < len(myList)-1:
	
	i+=1
print("keresett érték a {} helyen van".format(i+1))
