import random
toker=['rock','paper','scissors']
com=random.choice(toker)
while 1:
    user=input("Rock,Paper or Scissors: ")
    print('computer guess is', com)
    if user==com:
        print("tie")
    elif user=='rock' and com=='paper':
        print("You lose")
    elif user=='rock' and com=='scissors':
        print("You win")
    elif user=='paper' and com=='rock':
        print("You win")
    elif user=='paper' and com=='scissors':
        print("You lose")
    elif user=='scissors' and com=='rock':
        print("You lose")
    elif user=='scissors' and com=='paper':
        print("You win")
    play_again=input("Do you want to play again? enter yes or no: ")
    if play_again=='NO' or play_again=='no':
        break