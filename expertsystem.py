# Heart Attack Symptoms in Women: lightheadedness,nausea,extreme fatigue,fainting,dizziness, or pressure in the upper back.
# Signs and Symptoms of a Stroke;Face drooping,Arm weakness,Speech difficulty

HAsymptoms=['lightheadedness','nausea','extreme fatigue', 'fainting','dizziness','pressure in the upper back']
symotomsOfStroke=['face dropping','arm weakness','speech difficulty']
print('Welcome to Zealarax Clinic!\nCan I know Your Name?')  
userName=input('')
print(userName,', Can I know at least two of the symptoms you get, so as to know what your disease is?')

symptoms1=input()
symptoms2=input()
symptoms3=input()

if (symptoms1 in HAsymptoms) and (symptoms2 in HAsymptoms) or (symptoms3  in HAsymptoms):
    print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')
elif (symptoms1 in HAsymptoms) or (symptoms2 in HAsymptoms) and (symptoms3  in HAsymptoms):
    print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')
elif (symptoms1 in HAsymptoms) and (symptoms3 in HAsymptoms) or (symptoms2  in HAsymptoms):
    print('sorry',userName,', You\'re most likely to have an Heart Attack, please see our specialist in the Next Office. ')

elif (symptoms1 in symotomsOfStroke) and (symptoms2 in symotomsOfStroke) or (symptoms3  in symotomsOfStroke):
    print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')
elif (symptoms1 in symotomsOfStroke) or (symptoms2 in symotomsOfStroke) and (symptoms3  in symotomsOfStroke):
    print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')
elif (symptoms1 in symotomsOfStroke) and (symptoms3 in symotomsOfStroke) or (symptoms2  in symotomsOfStroke):
    print('sorry',userName,', You\'re most likely to have a Stroke, please see our specialist in the Next Office. ')

else:
    print('sorry',userName,', We\'ll need to run some tests to be sure of what disease your\'re having. \n please call the next patient on your way out.')

