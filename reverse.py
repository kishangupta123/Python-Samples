#to find the reverse of a number
n = int(input("enter your desired number:"))
print("the number before sorting is:",n)
rev = 0
while n!=0:
    rev = rev * 10 + n % 10
    n=(n//10)
print(" after sorting array is:",rev)
