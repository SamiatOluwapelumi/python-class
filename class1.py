import math
print('hello world')
a=5
name='samiat'
print(type(name))
print(type(a))


a=5
b=10
sum=b+a
print('the sum is',sum)


#this program will print the area of a circle
r=2.4
area_of_circle=math.pi*r**2
print('the area of a circle is',area_of_circle)

#this program will print the area of a triangle and the perimeter
c=6
h=1
l=3
areaOfTriangle=(c*h)/2
perimeter=l*c
print('the area of the triangle is ',areaOfTriangle)
print('the perimeter of the triangle is ',perimeter)



x=4
y=3
c=(x+y)*(x+y)
print('the answer is ',c)



principal=int(input('enter your principal amount'))
rate=float(input('enter your rate'))
years=int(input('enter your year'))
interest=(principal*rate*years)/100
future_value=principal+interest
print('the future value is ',future_value)


