import numpy as np
# check version
print(np.__version__)

# numpy array
x = np.array([1,2,3,4])
print(x)

# multidimensional array
# 2d array
x = np.array([[1,2,3,4],[2,4,6,8]])
print(x)

# 3d array
x = np.array([[[1,2],[4,5]],[[6,7],[1,2]]])
print(x)

# How to check our array dimension?
print(x.ndim)

# how to one dimension array convert to 4d array
x = np.array([1,2,3,4],ndmin=4)
print(x)
print(x.ndim)

# Array indexing

arr = np.array([2,4,5,6,7])
print(arr)
print(arr[0])

# indexing adding
print(arr[2]+arr[3])

# How array indexing in multidimensional
# 2d array indexing
arr = np.array([[1,2,3],[3,2,1],[2,1,2]])
print(arr[1,0])

# 3d array indexing
arr = np.array([[[1,2],[3,2]],[[2,1],[3,2]]])
print(arr)
print(arr[1,0,0])

# Negative indexing
arr = np.array([2,4,5,6,7])
print(arr)
print(arr[-1])

# Array slicing

a = np.array([1,2,3,4,5])
print(x)
#x[start:end]
print(x[2:4])

# Negative indexing slicing
a = np.array([1,2,3,4,5])
print(x)
#x[start:end]
print(x[-5:-1])

# How to print selected value to end value print
print(x[2:])

# Step by Step slicing
print(x[1:2:2])

# how multi dimensional array using slicing
x = np.array([[1,2,3],[1,2,3],[3,2,3]])
print(x)
print(x[1,1:])

# Numpy data types
x = np.array([1,2,3,4])
print(x)
print(x.dtype)

# Customize data types
x = np.array([1,2,3,4],dtype='f')
print(x)
print(x.dtype)

# How to convert data types
x = np.array([1,2,3,4])
print(x)
print(x.dtype)
y = x.astype('f')
print(y)
print(y.dtype)

# views vs copies
# copy function
x = np.array([1,2,3,4])
y = x.copy()
print(x)
print(y)
# view function
x = np.array([1,2,3,4])
y = x.view()
print(x)
print(y)

# how to check original arrays
x = np.array([1,2,3,4])
y = x.view()
z = x.copy()

print(y.base)
print(z.base)

# Iterations
arr = np.array([[1,2,3],[1,2,3]])
for i in arr:
    print(i)

# one by one elements access
arr = np.array([[1,2,3],[1,2,3]])
for i in arr:
   for j in i:
     print(j)

# one by one elements access with nditer function
arr = np.array([[1,2,3],[1,2,3]])
for i in np.nditer(arr):
    print(i)

# step by step elements access with nditer function
arr = np.array([[1,2,3],[1,2,3]])
for i in np.nditer(arr[:,::2]):
    print(i)

# Element and related indexing print
arr = np.array([[1,2,3],[1,2,3]])
for i in np.ndenumerate(arr):
    print(i)

# Shapes and Reshape
# shapes
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.shape)

# one to 5d
arr = np.array([1,2,3,4],ndmin=5)
print(arr)
print(arr.shape)

# Reshapes
arr = np.array([1,2,3,4,5,6,7,8,9])
new = arr.reshape(3,3)
print(new)

# How to convert any dimension array to one dimension
arr = np.array([[1,2],[2,4]])
new = arr.reshape(-1)
print(new)

# Search - how to search elements or values in numpy array?
# where
arr = np.array([1,2,3,4,5,6,7,8,9])
x = np.where(arr == 4)
print(arr)
print(x)

x = np.where(arr % 2 == 1)
print(arr)
print(x)

# sort
arr = np.array([1,2,3,4,5,6,7,8,9])
x = np.searchsorted(arr,[2,3,4])
print(x)
x = np.searchsorted(arr,4,side='right')
print(x)

# Join and split - array joining using python numpy, using method concatenate( )

# join
arr1 = np.array([1,2,3,4])
arr2 = np.array([2,4,6,8])

newarr = np.concatenate((arr1,arr2))
print(newarr)

# Join 2d
arr1 = np.array([[1,2,3,4],[1,2,3,4]])
arr2 = np.array([[1,2,3,4],[1,2,3,4]])

newarr = np.concatenate((arr1,arr2),axis=0)
print(newarr)

# split
arr1 = np.array([1,2,3,4])
newarr = np.array_split(arr,2)
print(newarr)








