#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.Write  a  NumPy  program  to  create  an  element-wise  comparison  (greater,  greater_equal,  less 
#and less_equal) of two given arrays.

import numpy as np
l1 = np.array([3,2])
l2 = np.array([3,4])
print("greatest: ")
print(np.greater(l1,l2))
print("greatest equal: ")
print(np.greater_equal(l1,l2))
print("less : ")
print(np.less(l1,l2))
print("less equal : ")
print(np.less_equal(l1,l2))


# In[42]:


#2.Write a NumPyprogram to create an array of all the even integers from 30 to 70.
import numpy as np
list= np.arange(30,71)
print("array of all even integers from 30 to 70 is : ")
print(list)


# In[43]:


#3.Write a NumPy program to create a 3x3 identity matrix.
import numpy as np
list= np.identity(3)
print("the 3x3 identity matrix is :")
print(list)


# In[44]:


#4.Write  a  NumPy  program  to  create  a  vector  with  values from  0  to  20 
#and  change  the  sign  of the numbers in the range from 9 to 15.
import numpy as np
l = np.arange(21)
l[(l>=9)&(l<=15)]*=-1
print("the resultant array is :")
print(l)


# In[45]:


#5.Write  a  NumPy  program  to  create  a  5x5  zero  matrix  with  elements  
#on  the  main  diagonal equal to 1, 2, 3, 4, 5.
import numpy as np
l=np.diag([1,2,3,4,5])
print("the array is")
print(l)


# In[46]:


#6.Write  a  NumPy  program  to  compute  sum  of  all  elements,  
#sum  of  each  column  and  sum  of each row of a given array
import numpy as np
l=np.array([[1,2],[3,4]])
print("the sum of all elements is")
print(np.sum(l))
print("row sum is")
print(np.sum(l,axis=1))
print("coloumn sum is: ")
print(np.sum(l,axis=0))


# In[52]:


#7.Write a NumPy program to save a given array to a text file and load it.
import numpy
List = [5,4,3,2,1]
Array = numpy.array(List)
file = open("file1.txt", "w+")
content = str(Array)
file.write(content)
file.close()
file = open("file1.txt", "r")
content = file.read()
print("new contents of the file are", content)
file.close()


# In[47]:


#8.Write a NumPy program to check whether two arrays are equal (element wise) or not.
import numpy as np
l1=np.array([3,2,1])
l2=np.array([3,2,1])
print(np.equal(l1,l2))


# In[49]:


#9.Write  a  NumPy  program  to  create  a  4x4  array  with  random  values,  now  create  a  new  array from the said 
#array swapping first and last rows
import numpy as np
l=np.random.rand(4,4)
print("the original array is:")
print(l)
l[[0,3]]=l[[3,0]]
print("the resultant array is :")
print(l)


# import numpy as np
# l1=np.array([1,2,3])
# l2=np.array([1,2,3])
# if(l1==l2):
#     print(np.multiply(l1,l2))

# In[50]:


#10.Write a NumPy program to multiply two given arrays of same size element-by-element.
import numpy as np 
l1=np.array([1,2,3]) 
l2=np.array([1,4,3]) 
print("array after multiplication")
print(np.multiply(l1,l2))

