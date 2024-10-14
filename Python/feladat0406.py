number01=28
number02=20
number03=12

if not (number01 < number02+number03 and number02 < number01+number03 and number03 <number02+number03  ):
	print("Háromszög")
	
else:
	
	result=number01+number02+number03
	print("Kerület:",result)
