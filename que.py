import math
       #1
class methods:
    string=' '
    def getstring(self):
        self.getstring=input('enter a string: ')
        

    def printstring(self):
        print(self.getstring.upper())
f=methods()
f.getstring()
f.printstring()
print('---------------')


#         #2
class rectangle:
    def __init__(self,l,w):
        self.lenght=l
        self.width=w

    def areaOfRectangle(self):
        areaOfRectangle=(f.lenght * f.width)
        print(f.lenght)
        print(f.width)
        print('area Of The Rectangle is equal to ',areaOfRectangle)
   
f=rectangle(int(input('enter ur length: ')),int(input('enter ur width: ')))
f.areaOfRectangle()
print('---------------')

        #3
class circle:
    def __init__(self,radius):
        self.radius=radius

    def AOC(self):
        a=math.pi*self.radius**2
        print('area of the circle is: ', a)

    def perimeter(self):
        b=2*math.pi*self.radius
        print('perimeter of the circle is: ', b)

p1=circle(int(input('enter ur radius: ')))
p1.AOC()
p1.perimeter()
print('---------------')

          #4
class rev:
    def __init__(self,word):
        self.word=word
p1=rev(input('enter a word to be revesed: '))
a=p1.word.split()
b=reversed(a)
print('the reverse is: ', ' '.join(b))
print('---------------')



            #5

mylist=[-25,-10,-7,-3,2,4,8,10]
n=len(mylist)

def threedigits(mylist,n):
    found=False
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if (mylist[i]+mylist[j]+mylist[k]==0):
                    print(mylist[i],mylist[j],mylist[k])
                    found=True
threedigits(mylist,n)