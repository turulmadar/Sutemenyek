text="Szeretem a tejet"

textSp=text.split(" ")

print(type(textSp))
print(len(textSp))
print(textSp)

for char in textSp:
	
	print(char)
print(text)
textCh=text.replace("tejet","sört")
print(textCh)

print(text[11:16])
