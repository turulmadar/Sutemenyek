import random
import math

origList=[]
copyList=[]

for i in range (100):
	origList.append(random.randint(1,500))

print(origList)
for num in origList:
	
	copyList.append(math.sqrt(num))
	 
print(copyList)
