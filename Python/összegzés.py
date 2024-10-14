myList=[]

for i in range (100):
	
	square=pow((i+1),2)
	myList.append(square)

result=10
for listItem in myList:
	result+=listItem

print("Összeg: {:>20}".format(result))
