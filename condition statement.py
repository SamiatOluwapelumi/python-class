from math import degrees


score=float(input('enter your score '))
if score>=73 and score<=100:
 print('your grade is A ')
elif score>=69 and score<=72.9:
  print('your grade is B ')
elif score>=59 and score<=68.9:
  print('your grade is C')
elif score>=49 and score<=58.9:
  print('your grade is D')
elif score>=39 and score<=48.9:
  print('your score is E')
elif score<=38.9:
  print('your grade is F ')
else:
  print('incorrect score')

weather=float(input('enther your value'))
if weather>= 60:
  print('the weather is sunny')
elif weather>=50:
  print('the weather is cool')
else:
  print('the weather is i dont know')



  #primary_colour=('blue,red,yellow')
  #secondary_colour=('orange,green,purple')
  #neutral_colour=('white,black')
  colour=input('what is your colour ')
  if colour=='blue':
     print('your colour is a primary colour')
  if colour=='red':
            print('your colour is a primary colour')
  if colour=='yellow':
            print('your colour is a primary colour')
  elif colour=='orange':
        print('your colour is a secondary colour')
  elif colour=='green':
            print('your colour is a secondary colour')
  elif colour=='purple':
            print('your colour is a secondary colour')
  elif colour=='white':
        print('your colour is a neutral colour')
  elif colour=='black':
            print('your colour is a neutral colour')
  else:
        print('i dont know your category')
