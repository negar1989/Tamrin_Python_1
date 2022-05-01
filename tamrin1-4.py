name=input("student name:")
family=input("student family:")
m=float(input("enter Math grade:"))
s=float(input("enter Science grade:"))
e=float(input("enter English grade:"))
ave=(m+s+e)/3
print(name,family,"has the average:",ave)
if ave>=17:
    result="Great"
if 12<=ave<17:
    result="Normal"
if ave<12:
    result="Fail"
else:
    result="nothing"
print(result)

