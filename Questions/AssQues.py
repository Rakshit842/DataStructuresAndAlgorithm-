# question 1
l1 = [1, 2, 3, 4, 5]
i=len(l1)-1
while i>=0:
    print(l1[i])
    i=i-1


# question 2
l1=[20,40,32,86,56,98]
a_75=0
b_40=0
for i in l1:
    if(i>75):
        a_75+=1
    elif(i<40):
        b_40+=1
print(a_75,b_40,sep=" ")

l1=[20,40,32,86,56,98]
i=0
a_75=0
b_40=0
while len(l1)>i:
    if(l1[i]>75):
        a_75=a_75+1
    elif(l1[i]<40):
        b_40=b_40+1
    i+=1
print(a_75,b_40, sep=" ")


# question 3
l1=[-1,7,-9,0,90]
p_ve=0
n_ve=0
for i in l1:
    if i>0:
        p_ve+=1
    elif i<0:
        n_ve+=1
print(p_ve,n_ve,sep=" ")


