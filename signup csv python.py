import csv
newUserData = []

def getUserEmail():
    userEmail=input('Enter email: ')
    filename=open('regData.csv', 'r')
    file=csv.DictReader(filename)
    Emails=[]
    for columns in file:
        Emails.append(columns['email'])

    for emailAddress in Emails:
        currentIndex = Emails.index(emailAddress)
        print(currentIndex)
        emailsLength = len(Emails) - 1

        if emailAddress==userEmail:
            print('Email Exists! Enter Another Email Adderess.')
            getUserEmail() #calling a function inside itself iscalled recursion
            break

        if (currentIndex == emailsLength and emailAddress != userEmail):
            newUserData.append(userEmail)
            print('Email Saved! \nUser data', newUserData)
            getUserUsername()
            break

def getUserUsername():
    userUsername=input('Enter Username: ')
    filename=open('regData.csv', 'r')
    file=csv.DictReader(filename)
    Usernames=[]
    for columns in file:
        Usernames.append(columns['username'])

    for userName in Usernames:
        currentIndex = Usernames.index(userName) 
        print(currentIndex)
        usernamesLength = len(Usernames) - 1

        if userName == userUsername:
            print('Username Exists! Enter Another Username ')
            getUserUsername() #calling a function inside itself iscalled recursion
            break

        if (currentIndex == usernamesLength and userName != userUsername):
            newUserData.append(userUsername) 
            print('Username Saved! \nUser data', newUserData)
            getUserPassword()
            break


def getUserPassword():
    userPasswordEntered=input('Enter Password: ')
    userPasswordConfirmed=input('Confirm Password: ')
    if userPasswordEntered == userPasswordConfirmed:
        newUserData.append(userPasswordEntered) 

        #save list to the end of the csv rows
        with open('regData.csv', 'a+', newline = '') as fileSave:
            csv_writer = csv.writer(fileSave)  
            csv_writer.writerow(newUserData) 
            print('Password Saved!User data', newUserData, '\nAccount successfully created') 

    else:
        print('Password does not match! Enter Password again')
        getUserPassword() 


def userSignUp():
    print('Welcome! \nCreate your account >')
    getUserEmail()

#Main program
userSignUp()
