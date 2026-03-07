"""method 1 using  temp value"""
a=10
b=12
print('before swaping values are a= '+str(a),'and b= '+str(b))
temp=a
a=b
b=temp
print('after swaping values are a= '+str(a),'and b= '+str(b))

"""method 2 using swap"""
a=int(input("enter first number"))
b=int(input("enter second number"))
a,b=b,a
print('before swaping values are a= '+str(a),'and b= '+str(b))
print('after swaping values are a= '+str(a),'and b= '+str(b))