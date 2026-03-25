string = input("Enter a string: ")
string = string.lower()
albhabet = input("Enter the alphabet you wanna find: ")
albhabet = albhabet.lower()
count=0

for i in string:
    if i in albhabet:
        count+=1

print(count)