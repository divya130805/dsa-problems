import array as ar
arr=ar.array('i',[1,2,3,4,5,6,7,8,9,0])
print("the array was:",arr)
for i in arr:
    print(i)
print("the insertion operation:::")
arr.insert(8,1000)
print("updates:",arr)
arr.append(20000)
arr.remove(3)
arr.pop(2)
arr.pop()
arr[0]=199999
print(arr)
arr=ar.array('i',sorted(arr))
print(arr)
arr=ar.array('i',sorted(arr,reverse=True))
print(arr)


x=[1,2,3,4]
y=[6,7,8,9]
z=x+y
print(z)
print(len(z))
f=z.copy()
print(f)