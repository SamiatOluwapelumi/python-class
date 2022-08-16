class student_signup:
   def __init__(self,fname,lname,Mname,age,address,city,state,nationality,phone,email,gender,password):
       self.firstname=fname
       self.lastname=lname
       self.middleName=Mname
       self.age=age
       self.address=address
       self.city=city
       self.state=state
       self.nationality=nationality
       self.phone=phone
       self.email=email
       self.gender=gender
       self.password=password
   
   def signup(self):
       print(self.firstname,self.lastname,self.middleName,self.age,self.address)
       print(self.city,self.state,self.nationality,self.phone,self.email,self.gender,self.password)
       print('sign up succesful!')

sign=student_signup(
 input('input your first name: '),input('input your last name: '),
 input('input your middle name: '),int(input('input your age: ')),
 input('input your address: '),input('input your city: '),input('input your state: '),
 input('input your nationality: '),int(input('input your phone number: ')),input('input your email: '),
 input('input your gender: '),input('input your password: '),
)
sign.signup()

class student_login:
    
   def __init__(self, username,password):
       self.username=username
       self.pword=password

   def printuser(self):
       print(self.username, self.pword)
       print('login succesful!')
login=student_login(input('enter your username: '), input('enter your password: '))
login.printuser()