food = input('What food would you like to have, sir? ')
drinks = input('What drinks would you like to drink? ')

if food != "" and drinks != "":
    print('You have ordered ' + food + ' and ' + drinks + ' drink.')
elif food == "" and drinks != "":
    print('You have not ordered food but ' + drinks + ' drink.')
elif food == "" and drinks == "":
    print('You have not ordered anything.')
else:
    print('You have ordered food ' + food + ' but no drink.')
