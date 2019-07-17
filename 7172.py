import numpy as np

array=np.array([[1,2,3],[4,5,6]],dtype=np.int32)
array2=[[1,2,3],[4,5,6]]
#print(array)
#print(array2)
#print(array.ndim) #维度
#print(array.shape) #行数和列数
#print(array.size)


a=np.zeros((5,5))
#print(a)
b=np.linspace(1,10,20).reshape(5,4)
#print(b)
c=np.empty((3,4))
print(c)