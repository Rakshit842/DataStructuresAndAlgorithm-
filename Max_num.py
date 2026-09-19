# Finding first maximum number
arr = [12, 7, 8, 9, 0]
maxno = arr[0]
for i in range(len(arr)):
    if arr[i] > maxno:
        maxno=arr[i]
print("maximum number is", maxno)



# Finding second maximum number
import math
arr1 = [12, 7, 8, 9, 0]
firstmax = -math.inf
secondmax = -math.inf

for curValue in arr1:
    if curValue > firstmax:
        secondmax = firstmax
        firstmax = curValue

    elif curValue > secondmax:
        secondmax = curValue
print("second maximum number is", secondmax)


# Assignment Q2
arr=[5,6]
sum=0
product=1
for i in range(len(arr)):
    sum=sum+arr[i]
    product=arr[i]*product
print(sum)
print(product)
