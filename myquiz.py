# score=0
# def ask_question(quesNumber):
#     global score    #to access the global score
#     print(questions[quesNumber])
#     userAnswer=input('what is your answer?: ')
#     if userAnswer==answers[quesNumber]:
#        score+=20
#        print('bravo!, your score is now ', score)
       
#     else:
#         score=score
#         print('wrong!, your score is still ', score)
        


# questions=['what is your name? ', 'your age? ', 'are you tall or short? ', 'what is your complexion? ', 'how are you? ']
# answers=['samiat' , '22', 'short', 'dark', 'i am fine']
# for i in range(0,5):
#     queNumber=int(input('choose a number from  0-4: '))
#     quesNumber=queNumber-1
#     ask_question(queNumber)






# def newGame(questions):
#     guesses=[]
#     correctAnswer=0
#     questionNumb=1
#     for key in questions:
#         print('----------')
#         print(key)
#         for i in options[questionNumb-1]:
#           print(i)
#         guess=input('enter an option from (A,B,C,D): ')
#         guess=guess.upper()
#         guesses.append(guess)
#         correctAnswer += check_answer(questions.get(key), guess)
#         questionNumb+=1
    
#     display_score(correctAnswer,guesses)
  
#     #----------------------------------------

# def check_answer(answer,guess):  
#   if (answer==guess):
#     print('correct!')
#     return 1
#   else:
#     print('wrong!')
#     return 0
# #----------------------------------------

# def display_score(correctAnswer,guesses):
#     print('----------')
#     print('RESULTS')
#     print('----------')

#     print('answers:' , end=' ')
#     for i in questions:
#       print(questions.get(i), end=' ')
#     print()
    
#     print('guesses: ', end=' ')
#     for i in guesses:
#       print(i, end=' ')
#     print()

#     score=int((correctAnswer/len(questions))*100)
#     print('your score is: ' ,str(score),'%')
#  #----------------------------------------

# def playAgain():
#    response=input(' do you want to play again? (yes or no)')
#    response=response.upper()
#    if response=='YES':
#          return True
#    else:
#          return False
# #---------------------------------
# questions={
#             'what is your name? ': 'A',
#             'your age? ':'B',
#             'are you tall or short? ':'D',
#             'what is your complexion? ':'A',
#              'how are you? ':'C'
# }

# options=[['A. samiat','B. SAMIAT', 'C. NO NAME', 'D. WHAT'],
#          ['A. 21','B. 22', 'C. 20', 'D .12'],
#          ['A. oinn','B. average', 'C. tall', 'D. short'] ,
#          ['A. dumb','B. light', 'C. darrk', 'D. yinmu'],
#          ['A. fine', 'B. good', 'C. FINE', 'D. okay']]
# while playAgain(): 

#  newGame(questions)


# print('byeeeee')


#This is a guess the number game.
import random, sys
# secretNumber = random.randint(1, 20)
# print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
# for guessesTaken in range(1, 7): 
#       print('Take a guess.')
#       guess = int(input())
#       if guess < secretNumber:
#             print('Your guess is too low.')
#       elif guess > secretNumber:
#             print('Your guess is too high.')
#       else:
#             break # This condition is the correct guess!
# if guess == secretNumber:
#       print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
# else:
#       print('Nope. The number I was thinking of was ' + str(secretNumber))


# print('ROCK, PAPER, SCISSORS')
# wins=0
# losses=0
# ties=0

# while True:
#   print('%s wins, %s losses, %s ties' % (wins, losses, ties))
#   while True:  #the input loop
#     print('enter your move: (r)ock (paper) (s)cissors or (q)uit')
#     playerMove=input()
#     if playerMove=='q':
#           sys.exit()
#     if playerMove=='r' or playerMove=='p' or playerMove=='s':
#           break
#     print('type one of r, p, s, or q.')


# #display what the player chose:
#   if playerMove=='r':
#         print('ROCK versus....')
#   elif playerMove=='p':
#         print('PAPER versus....')
#   elif playerMove=='s':
#         print('SCISSORS versus....')


#   #display what the computer choses
#   randomNumber=random.randint(1,3)
#   if randomNumber==1:
#         computermove='r'
#         print('ROCK')
#   elif randomNumber==2:
#         computermove='p'
#         print('PAPER')
#   elif randomNumber==3:
#         computermove='s'
#         print('scissors')

    
# #display and record the win/lose/tie
#   if playerMove==computermove:
#         print('it is a tie!')
#         ties+=1
#   elif playerMove=='r' and computermove=='s':
#         print('you win!')
#         wins+=1
#   elif playerMove=='p' and computermove=='r':
#         print('you win!')
#         wins+=1
#   elif playerMove=='s' and computermove=='p':
#         print('you win!')
#         wins+=1
#   elif playerMove=='r' and computermove=='p':
#         print('you lose!')
#         losses+=1
#   elif playerMove=='p' and computermove=='s':
#         print('you lose!')
#         losses+=1
#   elif playerMove=='s' and computermove=='r':
#         print('you lose!')
#         losses+=1       

      