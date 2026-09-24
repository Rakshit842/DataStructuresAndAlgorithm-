import array as arr
arrayName = arr.array('i', [12,35,56,67])


sum = 0
product = 1
for val in arrayName:
    sum+=val
    product *= val

# T/C = 0(N)
# s/C = 0(1)

print(sum)
print(product)

count = 0
target = int(input("Enter taget value: "))
for val in arrayName:
    if val == target:
        count += 1


inc = True
dec = True
for i in range(0,len(arrayName)):
    if(arrayName[i] > arrayName[i+1]):
        inc = False
    if(arrayName[i] < arrayName[i+1]):
        dec = False
if(inc==True):
    print("In increasing order")
elif(dec == True):
    print("In decreasing order")
else:
    print("Not sorted")



#1. Add
#a) append(value) -> Add teh values in last, T/C - 0(1), 0(N)
#b) insert(index, value) -> insert the value at index, T/C - 0(1), 0(n)

#2. Delete
#1, remove()
#2.pop()

arrayName.remove(12)
print(arrayName)

arrayName.pop(1)
print(arrayName)

arrayName[0] = 40
print(arrayName)

for i in range(0, len(arrayName), 2):
    print(arrayName[i], end=" ")