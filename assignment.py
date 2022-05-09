# height=float(input('what is your height in meters? '))
# weight=float(input('what is your weight in kg? '))
# BMI=(weight/height**2)
# print('your BMI is ',str(BMI) ,'kg/m2')


weight=float(input('imput your weight '))
height=float(input('input your height '))
BMI=(weight/height**2)
if BMI<18.5:
    print('you are an underweight')
elif BMI>=18.5 and BMI<=24.9:
    print('healthy weight')
elif BMI>25 and BMI<=29.9:
    print('overweight')
elif BMI>=30 and BMI<=39.9:
    print('obesity')
else:
    print('i do not know you')