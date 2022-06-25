# def reverse(data):
#     for index in range (len(data)-1,-1,-1):
#         yield data[index]


# for char in reverse('golf'):
#     print(char)
# print('___________')


# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# rev = Reverse('spam')
# iter(rev)
# for char in rev:
#      print(char)



from logging import raiseExceptions


# nums=[1,2,3,4]
# for i in nums:
#     print(i)

# it=iter(nums)
# print(it.__next__())
# print(it.__next__())


# print(next(it))

# class TopTen:
#     def __init__(self):
#         self.num=1

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.num<=10:
#             val=self.num
#             self.num+=1

#             return val
#         else:
#             raise StopIteration

# values=TopTen()

# for i in values:
#     print(i)

  

  #yield keyword make it a generator
def squareNumbers(nums):
    for i in nums:
        yield(i*i)

myNum=squareNumbers([1,2,3,4,5])
print(next(myNum))
print(next(myNum))
print(next(myNum))
print(next(myNum))
print(next(myNum))
print('_______________')
for num in myNum:
    print (num)



#list comprehension
myNum=[x*x for x in [1,2,3,4,5]]
print(list(myNum))
for num in myNum:
    print (num)