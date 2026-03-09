from colorama import Fore, Style

number = int(input("Enter a number: "))
if number % 2 == 0 and number != 0:
    print(Fore.RED + "Even" + Style.RESET_ALL)
else:
    print(Fore.RED + "Odd" + Style.RESET_ALL)
