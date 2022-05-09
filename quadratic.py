import math
a=float(input('enter value '))
b=float(input('enter value '))
c=float(input('enter value'))
d=(b**2-4*a*c)
if d>0:
 e=math.sqrt(d)
x1=b+d/2*a
x2=b-d/2*a
print('answer is equal to ',x1)
print('answer is equal to ', x2)
print('positive discriminant ')
if d==0:
   print('zero discriminant ') 


   