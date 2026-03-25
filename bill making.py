while True:
    name=input("enter customer name: ")
    total=0
    while True:
        print('enter the amount and quantity')
        amount=float(input('enter the amount: '))
        quantity=int(input('enter the quantity: '))
        total+=amount*quantity
        repeat=input('Do you want to continue? enter yes or no ')
        if repeat=='no' or repeat=='No':
            break
    print('-'*40)
    print('Name: ',name)
    print('Total Amount To be paid: ',total)
    print('----happy shopping----')
    repeat1=input('Do you want to continue for another customer? enter yes or no ')
    if repeat1=='no' or repeat1=='No':
        break

