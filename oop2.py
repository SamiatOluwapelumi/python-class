# from logging import raiseExceptions


# try:
#     print(x)
# except:
#     print('an exception occured')
# #try block will generate and error because 'x' is not defined, the ecxept block wil executed
# print('-----------')

# try:
#     print(x)
# except NameError:
#     print('variable x is not defined')
# except:
#     print('something else went wrong')
#  # prints one message if the ry block raises a name error and another for another errors
# print('-----------')

# #ELSE
# try:
#     print('hello')
# except:
#     print('something went wrong')
# else:
#     print('nothing went wrong')
# # since derez no error, the else statemnt is printed
# print('-----------')


# #FINALLY: if specified, will execute regardless if the try block raises an error or not

# try:
#     print(x)
# except:
#     print('something went wrong')
# finally:
#     print("the 'try except' is finished")
# print('-----------')

# try:
#     f=open('demofile.txt', 'w')
#     try:
#         f.write('samiat is a girl')
#     except:
#         print('something went wrong when writing to file')
#     finally:
#         f.close()
# except:
#     print('something went wrong when opening the file')
# print('-----------')
 


#  #raise an exception

# # x=-1
# # if x<0:
# #     raise Exception('sorry, no numbers below zero')
# # print('-----------')


# x='hello'
# # print(type(x))
# if not type(x) is int:
#   raise TypeError('only integers are allowed')
#ask sis racheal
# print('________')



class Complex:
 def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r)
print(x.i)    



# class Dogm:
#     kind = 'canine' # class variable shared by all instances
#     def __init__(self, name):
#      self.name = name # instance variable unique to each instance
# d = Dogm('fuddo')
# # e = Dog('Buddy')
# print(d.kind) # shared by all dogs

# print(e.kind) # shared by all dogs

# print(d.name) # unique to d

# print(e.name) # unique to e




class Dog:
    tricks = [] # mistaken use of a class variable
    def __init__(self, name):
      self.name = name
    def add_trick(self, trick):
      self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)