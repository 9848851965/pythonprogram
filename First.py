import random
num=random.randint(100,1000)
while True:
    a=int(input('enter a number'))
    if a==num:
        print('your entered a cureect number',num)
        break
    elif a<num:
        print('enter greater number')
    elif a>num:
        print('enter a lesser number')
