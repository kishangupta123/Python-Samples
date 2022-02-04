arr=[9,8,5,7,-6,4,2,1,3,10,100,13,15,14,12,17,16,19,18,20,25,-24,22,21,23]
#to find min element
arr.sort()
print("sorted array are:",arr)
print("minimum element is:",arr[0])
#to find if element present
exist = 5 in arr
print(exist)
#even and odd count
even_count,odd_count=0,0
for i in arr:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
print("number of even elements",even_count)
print("number of odd elements",odd_count)
#positive and neagtive count
pos,neg=0,0
for j in arr:
    if (j>0):
        pos+=1
    else:
        neg+=1
print("number of positive count",pos)
print("number of negative count",neg)