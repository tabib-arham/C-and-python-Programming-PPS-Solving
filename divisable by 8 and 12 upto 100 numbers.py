number=int(input("Enter a number up to 100: "))
if(number>=0 and number<=100):
    if(number%8==0 and number%12==0):
        print('number is divisable by 8 and 12')
    else:
        print('number is not divisible by 8 and 12')
else:
    print('please enter a number that is greater than or equal to 0 and less than or equal to 100')