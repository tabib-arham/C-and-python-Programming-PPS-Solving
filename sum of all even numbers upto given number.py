n = int(input('Enter the integer number for the range: '))
sum_odd = 0
for i in range(1, n+1):
    if i % 2 != 0:   # check if i is odd
        sum_odd += i
print('Total sum of odd numbers up to', n, 'is:', sum_odd)
