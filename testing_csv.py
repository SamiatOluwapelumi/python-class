import csv
from fileinput import filename
# header=['name', 'department','month']
# with open('okay.csv','w',newline='') as employeefile:
#     emplyee_writer=csv.writer(employeefile)
#     emplyee_writer.writerow(header)
#     emplyee_writer.writerow(['john smith','accounting','november'])
#     emplyee_writer.writerow(['erica mayers','IT','march'])

# header=['name', 'location','post']
# data=['samiat', 'ilaro','president']
# with open('EOBSNGO.csv', 'w',newline='') as file:
#     file_writer=csv.writer(file)
#     file_writer.writerow(header)
#     file_writer.writerow(data)


#reding csv files with cvs

# with open('okay.csv') as csvfile:
#     csvreader=csv.reader(csvfile, delimiter=',')
#     line_count=0
#     for row in csvreader:
#         # print(row)
#         if line_count==0:
#             print(f'column names are {", ".join(row)}')
#             line_count+=1
#         else:
            # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            # line_count+=1
    # print(f'processed {line_count} line')
 


# import csv
# exampleFile = open('example.csv', 'w', newline='')
# examplewriter = csv.writer(exampleFile)
# # exampleData = list(examplewriter)
# exampleData=[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
# ['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
# ['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
# ['4/10/2015 2:40', 'Strawberries', '98']]
# examplewriter.writerows(exampleData)



# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# for row in exampleReader:
#     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
#     print('_______________')

# with open('example.csv') as csvfile:
#     csvreader=csv.reader(csvfile, delimiter=',')
#     line_count=0
#     for row in csvreader:
#         print('row',str(csvreader.line_num),'.' ,row)


# outputFile = open('output.csv', 'w', newline='')
# outputWriter = csv.writer(outputFile)
# outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
# 21
# outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
# 32
# outputWriter.writerow([1, 2, 3.141592, 4])
# 16
# outputFile.close()

#to seperate data without using the comma, we use the tab and \n\n gives two lines in between the rows
#delimiter is the character that appears between the cells on a row.By default, the delimiter for a CSV file is a comma.
# The line terminator is the character that comes at the end of a row. By default, the line terminator is a newline.
#tsv means tab seperated value
#csv means comma seperated value

# csvFile = open('example.tsv', 'w', newline='')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# 24
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# 17
# csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
# 32
# csvFile.close()



#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.
# import csv, os
# os.makedirs('headerRemoved', exist_ok=True)
# Loop through every file in the current working directory.
# for csvFilename in os.listdir('.'):
#  if not csvFilename.endswith('.csv'):
#   continue # skip non-csv files
#  print('Removing header from ' + csvFilename + '...')
 # TODO: Read the CSV file in (skipping first row).
 # TODO: Write out the CSV file.


# userName=input('enter username: ')
userEmail=input('enter email: ')
# userPassword=input('enter password: ')
print('\nlets print what is saved in each column:')
filename=open('Registration.csv', 'r')
file=csv.DictReader(filename)
usernames=[]
Emails=[]
Passwords=[]
for columns in file:
      usernames.append(columns['username'])
      Emails.append(columns['email'])
      Passwords.append(columns['password'])
# print('saved username: ',usernames)
print('saved emails: ',Emails)
# print('saved password: ',Passwords)
for emailAddress in Emails:
      if emailAddress==userEmail:
            print('Email Exists! Enter Another Email Adderess.')



# datas=[ a,b,c]
# data=[]
# with open('Registration.csv', 'w',newline='') as file:
  # csvfile=csv.writer(file)
  # csvfile.writerow(header)
  # csvfile.writerow(datas)
  














# for registration in range(1,3):
#     print('enter details for registration: ')
#     if datas[0]==data[0]:
#         print('username already exist') 
#     elif datas[1]==data[1]:
#         print('email already exist')
#     elif datas[2]==data[2]:
#         print('password already exist')
