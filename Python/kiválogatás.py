import random
import math

origList=[]
chooseList=[]

for i in range (100):
	origList.append(random.randint(1,100))

print(origList)

for num  in origList :
	if(num>50):
	chooseList.append(num)
