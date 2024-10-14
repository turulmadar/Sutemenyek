import random

#muszáj a random a random kell
#number = random.randint(0,6)

myList=[]
for i in range( 5000 ):
	myList.append(random.randint(0,200))
	
counter=0

for i in range(len(myList)):
	
	if myList[i]<100:
	
		counter += 1

	
print("100 alatti értékek száma:{:>10}".format(counter))
