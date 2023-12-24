import numpy as np
import sys
import time
import matplotlib.pyplot as plt


#how to create numpy arrays

# arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
# print(type(arr1))

# arr2 = np.array([[1, 2, 3,],
                # [4, 5, 6]])
# print(type(arr2))

# arr3 = np.zeros((4,4))
# arr4 = np.ones((3,3))
# arr5 = np.identity(5)
# arr6 = np.arange(10)
# arr7 = np.arange(10,28,2)
# arr8 = np.arange(10).reshape(2,5)
# arr9 = np.linspace(10,40,10)
# arr10 = arr9.copy()
# arr11 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])


# print(arr1,"\n")
# print(arr2,"\n")
# print(arr3,"\n")
# print(arr4,"\n")
# print(arr5,"\n")
# print(arr6,"\n")
# print(arr7,"\n")
# print(arr8,"\n")
# print(arr9,"\n")
# print(arr10,"\n")
# print(arr11)

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)
# print(arr11.shape)

# print(arr11.ndim)
# print(arr1.ndim)
# print(arr2.ndim)

# print(arr1.size)
# print(arr2.size)
# print(arr3.size)
# print(arr11.size)

# print(arr1.itemsize)
# print(arr3.itemsize)
# print(arr4.itemsize)
# print(arr8.itemsize)
# print(arr11.itemsize)

# print(arr1.dtype)
# print(arr3.dtype)

# list1 = range(100)
# arr12 =np.arange(100)

# print(sys.getsizeof(87)*len(list1))
# print(arr12.itemsize*arr12.size)


# x = range(100000000)
# y = range(100000000,200000000)

# start_time = time.time()

# c = [(x,y) for x,y in zip(x,y)]

# print(time.time() - start_time)

# a = np.arange(100000000)
# b = np.arange(100000000,200000000)

# start_time = time.time()

# c = a + b

# print(time.time() - start_time)

# print(arr12)
# arr12 = arr12.reshape(10,10)
# print(arr12)

# print(arr12[3:10])
# print(arr12[3])

# arr13 = np.arange(24).reshape(6,4)
# print(arr13)

# print(arr13[:2])
# print(arr13[:,2])
# print(arr13[:,1:3])
# print(arr13[2:4,1:3])

# for i in arr13:
#     print(i)

# for i in np.nditer(arr13):
#     print(i)

arr14 = np.arange(1,7)
arr15 = np.arange(4,10)
# print(arr14 + arr15)
# print(arr14 - arr15)
# print(arr14 * arr15)
# print(arr14 / arr15)
# print(arr14 % arr15)
# print(arr14*2)
# print(arr14>2)

arr16 = np.arange(6).reshape(2,3)
arr17 = np.arange(6,12).reshape(3,2)
# print(arr16.dot(arr17))

# print(arr17.max())
# print(arr17.max(axis = 0))
# print(arr17.max(axis = 1))
# print(arr17.min())
# print(arr17.sum())
# print(arr17.mean())
# print(arr17.std())
# print(np.median(arr17))
# print(np.sin(arr17))
# print(np.exp(arr17))

# Reshaping Numpy Array

# print(arr17.ndim)
# print(arr17.ravel())
# print(arr17.transpose())
# print(np.hstack((arr14,arr15)))
# print(np.vstack((arr14,arr15)))
# print(np.hsplit(arr17,2))
# print(np.vsplit(arr17,3))

# print(arr17[[0,2]])
# print(arr17[[0,1],[1]])
# print(arr17[[0,2],[0]])
# print(arr17)

# print(arr13[arr13>12])
# print(arr13[(arr13>12) & (arr13%2!=0)])
# arr13[(arr13>12) & (arr13%2!=0)] = 0
# print(arr13)

# x = np.linspace(-40,40,50)
# print(x.size)
# y = np.sin(x)
# print(y.size)
# print(plt.plot(x,y))

# print(arr14 * arr15)
# print(arr14)
# print(arr15)
# print(arr14 + arr16)

# print(np.random.random())
# print(np.random.random(3))
# print(np.random.seed(2),np.random.random())
# print(np.random.uniform(1,100))
# print(np.random.uniform(1,100,20).reshape(5,4))
# print(np.random.randint(1,50,10).reshape(2,5))
# a = np.random.randint(1,50,10).reshape(2,5)
# print(np.max(a))
# print(np.min(a))
# print(np.max(a))
# print(np.argmax(a))
# print(np.argmax(a))
# print(np.argmin(a))
# print(a[np.argmin(a)])
# print(np.argmax(arr15))
# print(arr15[np.argmax(arr15)])
# print(arr15)
# Change Value
# arr15[arr15%2==1]=-1
# print(arr15)
# Temporary Change Value
# np.where(arr15%2==1,-1,arr15)
# print(arr15)
# print(np.where(arr15%2==1,-1,arr15))
# print(arr15)
# arr18 = np.random.randint(1,100,20).reshape(4,5)
# print(arr18)
# print(np.sort(arr18))
# print(np.percentile(arr17,50))
# print(np.percentile(arr14,50))


