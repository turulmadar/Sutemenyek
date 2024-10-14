myList=[]
import random

for i in range( 2000 ):
	myList.append(i)
	myList.append(random.randint(-500,700))
	counter=0
for i in range(len(myList)):
	if myList[i]<0:
		counter+=1

print("Negatív számok{:^15}".format(counter))
