text="    _szöveg_    "
sentence="Ez eGy teszt szÖveg.txt"

print(text)
print(text.strip())
print(text.rstrip())
print(text.lstrip().rstrip())
print(text.lstrip())

print(sentence.endswith(".txt"))
print(sentence.endswith(".tx"))

print(sentence.startswith("Ez"))
print(sentence.startswith("z"))

print(sentence.find( "szt" ))
print(sentence.find( "st" ))
print(sentence.find( "st" ))

