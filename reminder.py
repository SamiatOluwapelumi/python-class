import time
print('what are you cooking?')
food_type=input()
if food_type.isalpha()==False:
    print('enter a correct food type')
    quit()

print('rough estimate of time required?')
estimateTime=input()
# print(estimateTime.isdigit())
if estimateTime.isdigit()==False:
    print('enter a correct estimateTime')
    quit()
else:
    estimateTime=int(estimateTime)*60
    
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
print('interval of time to be reminded?')
Time=input()
if isfloat(Time)==False:
    print('enter a correct Time Interval')
    quit()
else:
    Time=float(Time)*60
a=0
count_time=0
for cc in range(estimateTime):
    a = a+1
    # time.sleep(Time)

    if a==Time:
        count_time=count_time+Time
        print(a,' you still have food on the fire! this is ',count_time, 'seconds after!')
        
        # print(count_time)
        # print(float(estimateTime))
        if count_time==float(estimateTime):
            print('your food is most likely to be done!')
    a=0
