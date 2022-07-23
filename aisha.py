# password=input('enter your password: ')
# if len(password)>=6 and len(password)<=7:
#     print('good password!')
# elif len(password)>=8 and len(password)<=9:
#     print('strong password!')
# elif len(password)>=10 and len(password)<=12:
#     print('very strong password!')
# elif len(password)>12:
#     print('password is too long!')
# else:
#     print('invalid password! input a new password.(your password must be between 6-12 characters)')





category=input('what category do you want to print. we support lenght (l)')
if category=='l':
    unit_from= input('what unit are you converting from?: ')
    unit_to= input('what unit are you converting to?: ')
    number=input('what number are you converting?: ')

    #calculations

if unit_from== 'cm' and unit_to== 'm':
   answer=float(number)/100
elif unit_from== 'mm' and unit_to== 'cm':
   answer=float(number)/10
elif unit_from== 'm' and unit_to== 'cm':
   answer=float(number)*100
elif unit_from== 'cm' and unit_to== 'mm':
   answer=float(number)*10
elif unit_from== 'mm' and unit_to== 'm':
   answer=float(number)/1000
elif unit_from== 'm' and unit_to== 'mm':
   answer=float(number)*1000
elif unit_from== 'km' and unit_to== 'm':
   answer=float(number)/1000
elif unit_from== 'm' and unit_to== 'km':
   answer=float(number)*1000

print(answer)