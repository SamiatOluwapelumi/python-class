# with open('sample.txt','w') as f:
#  f.write('the lord is good')
#  f.write('i am fine')
#  r=open ('sample.txt')
#  print (r.read())



# try:
#      f = open('file.txt','r') 
#      print(f.read())

# finally:
#     print('error')


# a=open('file.txt', 'r')
# print(a.readline(),end='#')
# print(a.readline())


a=open('file.txt', 'r')
b=open('sample.txt', 'a')
f1=open('abc', 'w')
f1.write('something ')
f1=open('abc', 'a')
f1.write( 'im smart')
b.write('she is brilliant')

print(a.read())



#copy all data from file.txt and save them in abc

for data in a:
    f1.write(data)

