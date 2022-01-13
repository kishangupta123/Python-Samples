#swap 2 number without 3rd variable
a=int(input("enter first number:"))
b=int(input("enter second number"))
a=a-b
b=a+b
a=b-a
print("after swapping result are:",a,b)
