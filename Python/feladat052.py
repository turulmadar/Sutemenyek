def first(num01,num02):
	
	result=num01-num02
	return result

def second(firstRestResult,multiplier):
	
	result=firstRestResult*multiplier
	
	return result

def third(secondRestResult):
	
	result=secondRestResult*2/8	
	
	return result

def out (summaResult):
	
	print("Számítás eredméyne:{:^15.2}".format(summaResult))
	
firstRestResult = first(4.5,3.7)
secondRestResult = second(firstRestResult,2.3)
summaResult = third(secondRestResult)
out(summaResult)
 
