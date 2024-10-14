myList=[]
summa=0

for i in range (100,600):
	myList.append(i)

for number in myList:
	summa+=number
print("Összeg:{:^20}".format(summa))		
