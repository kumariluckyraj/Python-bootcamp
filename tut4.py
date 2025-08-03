import numpy as np # used for perfoming mutliple operations with arrays
list = [1,2,3,4]
arr = np.array(list)
print(arr)#1-d array
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[5,3,6,7]

arr2 = np.array([l1,l2,l3]) # 2-d array
print(arr2)
print(arr2.shape)
print(arr2.reshape(4,3)) # if we write 4,5 the total number of elemnts will be 20 which is more than the existing value so we will get error , you can do 1,12
print(arr2[0:2,0:2])
        #row,column
      
      #copy() function and broadcasting
arr1=[1,4,5,6]
arr1=arr
arr1[2:]=100
print(arr1)
arr1=arr.copy()
print(arr1)      
rand=np.random.rand(3,8)
print(rand)
randn=np.random.randn(3,8)
print(randn)   
randint=np.random.randint(0,100,8)#b/w 0 to 100 select 8 numbers
print(randint)