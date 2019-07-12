for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(i,j,i*j),end='')
    print( )

'''
九九乘法表
'''
'''
简单练习
'''
#print(65+3)

#print(int('5'))

print(5/3)
con=1;
while con<10:
    # print(con)
    con+=1;
c=1;
for i in range(100):
    if(i%c==0):
        c*=2;
        print(i)
a=True;
s="pp" if a else "pp"
print(s)


x = 4
y = 2
z = 3
if x > 1:
    print ('x > 1')
elif x < 1:
    print('x < 1')
else:
    print('x = 1')
print('finish')
import test2
test2.test1(9)