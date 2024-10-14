number01=34
number02= 3.123456789
text="Szöveg"

print( "{} {}".format(number01,number02))
print("{:>20}".format(number01))
print("{}".format(number01))
print("{:^20}".format(number01))
print("{:.6}".format(number02))
print( "{1} {0}".format(number01,number02))
print( "Mennyiség:{1} Ár:{0}".format(number01,number02))
