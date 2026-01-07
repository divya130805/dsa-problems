import array as ar
arr=ar.array('i',[1,2,3,4,5,6])
print(arr)
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print("the largest is :",i)