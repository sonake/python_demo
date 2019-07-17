a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
    print(i/2,j*2)

fun=lambda x,y:x+y
x=int(input("x="))
y=int(input("y="))
print(fun(x,y))

a=set({"1","2"})
