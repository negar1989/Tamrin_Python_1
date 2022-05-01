a=int(input("Andaze zele aval:"))
b=int(input("Andaze zele dovvom:"))
c=int(input("Andaze zele sevvom:"))
if a<b+c and b<a+c and c<a+b:
    result="Mosalas is ok"
else:
    result="khata"
print(result)