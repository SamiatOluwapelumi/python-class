# class myclass:
#     x=5
# print(myclass)
# p1=myclass()
# print(p1.x)

# class person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age= age
# p1= person('john', 36)
# print(p1.name)
# print(p1.age)

#     def myfunc(self):
#      print('hello my name is ', self.name)
# p1=person('john', 36)
# p1.myfunc()


class person:

    def __init__(self, fname, lname):
     self.firstname=fname
     self.lastname=lname

    def printname(self):

        print(self.firstname, self.lastname)
# x=person('john','doe')
# x.printname()   #this is a func call, its absence does nt print anything

# creating a child class dah will inherit the properties and methods from the class person
class student(person):
  pass #this is used when you do not want to add any other properties or method to the class
# now the student class has the same properties and methods as the person class.

#using the student class to create an object and execute the printname method

# x=student('mike', 'olsen')
# x.printname()   

# __init__() func is being called automatically everytime the class is being used to create a new object

# class student(person):
    # def __init__(self,fname,lname): #add properties 
# wen u add init func, the child class will no longer inherit the parent init func, to keep the inheritance parent init function, add a call to d parent init funct.
# example

# class student(person):
#      def __init__(self,fname,lname):
#          person.__init__(self,fname,lname)
# super() function_____ is also anothe way to inherit prop and method from parent func.

# class student(person):
#     def __init__(self,fname,lname):
#          super().__init__(self,fname,lname)
#          self.graduationyear=2022  # this is a property added to the class student
 
class student(person):
        def __init__(self,fname,lname,year):
         super().__init__(fname,lname)
         self.graduationyear=year
x=student('mike','olsen',2019)
print(x.graduationyear)

def welcome(self):
  print('welcome ', self.firstname, self.lastname, 'to the class of ', self.graduationyear)
x=student('mike','olsen', 2019)
x.welcome()
        
  

