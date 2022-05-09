import csv
# userEmail=input('enter email: ')
# print('\nlets print what is saved in each column:')
# filename=open('Registration.csv', 'r')
# file=csv.DictReader(filename)
# usernames=[]
# Emails=[]
# Passwords=[]
# for columns in file:
#       usernames.append(columns['username'])
#       Emails.append(columns['email'])
#       Passwords.append(columns['password'])
# print('saved emails: ',Emails)
# for emailAddress in Emails:
#       if emailAddress==userEmail:
#             print('Email Exists! Enter Another Email Adderess.')


def getUserEmail():
    
    userEmail=input('Enter email: ')
    # print('\nlets print what is saved in each column:')
    filename=open('Registration.csv', 'r')
    file=csv.DictReader(filename)
    Emails=[]
    for columns in file:
        Emails.append(columns['email'])
    print('saved emails: ',Emails)
    for emailAddress in Emails:
        # print(Emails.index(emailAddress))
        if emailAddress==userEmail:
            print('Email Exists! Enter Another Email Adderess.')
            getUserEmail() #calling a function inside itself iscalled recursion
        # else:
        # if Emails.index(emailAddress)==len(Emails):
            print('Email Saved!')
    getUserUsername()   

def getUserUsername():
    userUsername=input('Enter Username: ')
    # print('\nlets print what is saved in each column:')
    filename=open('Registration.csv', 'r')
    file=csv.DictReader(filename)
    usernames=[]
    for columns in file:
        usernames.append(columns['username'])
    print('saved username: ',usernames)
    for userusername in usernames:
        if userusername==userUsername:
            
            print('Username Exists! Enter Another Username ')
            getUserUsername() #calling a function inside itself iscalled recursion
            print('Username Saved!') 

def userSignUp():
    getUserEmail()


userSignUp()
# getUserUsername()
# getUserEmail()
