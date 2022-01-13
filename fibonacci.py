first,second=0,1
n = int(input("number for fibonacci series : "))
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        temp=i
    else:
      temp = first + second;
      first = second;
      second = temp;
    print(temp)
