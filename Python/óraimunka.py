myList=[]

for i in range (500):
	
	square=(i+1 )* 5
	myList.append(square)

result=0

for listItem in myList:
	result+=listItem

print("Összeg: {:>0}".format(result))
