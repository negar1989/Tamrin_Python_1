w=int(input("enter the weight in kg"))
h=float(input("enter the height in meter"))
BMI=w/h
print(BMI)
if BMI<18.5:
    result="underweight"
if 18.5<BMI<24.9:
    result="normal"
if 25<BMI<29.9:
    result="overweight"
if 30<BMI<34.9:
    result="obese"
if BMI<35:
    result="extremely obese"
else:
    result="nothing"
print(result)

