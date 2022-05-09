import math
from functools import reduce
# def primeNumber(a):
#  if a%2==1 and a%a==0:
#     print(a, ' is a prime number')
#  else:
#     print(a, 'is not a prime number')

    
# a=int(input('enter number: '))
# primeNumber(a)



# sammy=[]
# for a in range(1,31):
#     sammy.append(a**2)
# print(sammy)
 

# sammyDic={}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# sammyDic.update(dic1)
# sammyDic.update(dic2)
# sammyDic.update(dic3)
# print(sammyDic) 

# dic={}
# for a in range(1,16):
#     dic[a]=a**2
# print(dic)




# lambda a:a+15
# a=int(input('a?:'))
# print(a+15)

# a=int(input())
# x=(lambda a,b: a+b)(a,15)
# print(x)


# a=(lambda x,y: x*y)(2,3)
# print(a)



# list1=[1,2,3,4,5,6]
# a=int(input('??'))
# b = lambda a:a%2==1
# myList=list(filter ( b, list1))
# print(myList)



# list1=[1,2,3,4,5,6,7,8,9,10]
# for a in list1:
    # b= reduce(lambda a,c: a*c,list1)
# print(b)



# list1=[1,2,3,4]
# list2=[2,4,6,8]
# list3=[3,6,9, 8]
# a=list(map(lambda a,b,c:a+b+c, list1,list2 , list3 ))
# print(a) 



# list1=[1,2,3,4,5,6]
# list2=[2,4,6,8]
# output=list(filter(lambda x:x in list1,list2))
# print(output)         


# array=[1,2,3,4,5,6,7,8,9,10]
# x=(reduce(lambda a,b:a+b,array))
# print(x)



# for a in range(10,51):
#     if a%3==0:
#         print(a)

# for a in range(100,201):


# myList=[2,5,8,2,3,4]
# myList.sort()
# print('largest element is ', myList[-1])
# print('the largest element is ', max(myList))


# list=[2,1,3,4,2,5,6]
# list.insert(2,0)
# print(list)


# a={2,3,4,5,7,6,8}
# b={12,10,9,0,1,13,11}
# print(a)
# print(b)
# print(a.isdisjoint(b))


# def function(list1,list2):
#    if list1.isdisjoint(list2)==True:
#        res=True
#    else:
#        res=False
#    return res
# list1={1,2,3,4,5}
# list2={6,2,8,9,10}
# print(list1.isdisjoint(list2))
# print(type(list1))



# vowels=['a','e','i','o','u',]
# vowels.pop(2)
# vowels.reverse()
# print(vowels)
# print('i' in vowels)


# power=[]
# for a in range (1,20):
#     power.append(a**2)
# print(power)



# power=[a**2 for a in range(1,20)]
# print(power)



# set={1,2,2,3,4,5,6}
# set.add(8)
# print(set)
# set.update({7,10,9})
# print(set)
# set.remove(8)
# print(set)
# set.clear()
# print(set)



 