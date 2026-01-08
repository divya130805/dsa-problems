import array as arr
ar=arr.array('i',[1,2,3,4,5,6,7,8,9])
print(ar)
x=[]
for i in ar:
    x.append(i)
print("the arr element was:",ar)
print("the x element was:",x)