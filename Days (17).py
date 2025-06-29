try:
    num = int(input('Enter a number from 1 to 7: '))
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    if 1 <= num <= 7:
        print(days[num-1])
    else:
        print('There are only 7 days in a week')
except:
    print('Enter integer')