import math
x=input("enter x:")
if x=="radical":
    result=(math.sqrt(x))
    if x=="sin":
    result=math.sin(math.radians(x))  
if x=="cos":
    result=math.cos(math.radians(x))
if x=="cot":
    result=math.cot(math.radians(x))
if x=="factorial":
    result=math.factorial(x)
print(result)