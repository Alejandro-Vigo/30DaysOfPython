#Day 24: 30 Days of python programming

import numpy as np

python_list = [1,2,3,4,5]
numpy_array_from_list = np.array(python_list)
print(numpy_array_from_list, type(numpy_array_from_list))

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(numpy_two_dimensional_list)

print(numpy_two_dimensional_list.tolist(), type(numpy_two_dimensional_list.tolist()))

python_tuple = (1,2,3,4,5)
numpy_array_from_tuple = np.array(python_tuple)
print(numpy_array_from_tuple, type(numpy_array_from_tuple))

nums = np.array([1, 2, 3, 4, 5])
three_by_four_array = np.array([[0, 1, 2, 3],[4,5,6,7],[8,9,10, 11]])
print(nums.shape)
print(three_by_four_array.shape) #first row, second column

int_array = np.array([-3, -2, -1, 0, 1, 2,3])
print(int_array.dtype)

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8]])
print(numpy_array_from_list.size)
print(two_dimensional_list.size)

#Mathematical operations: not like Python lists, in Numpy we don't need to use loops to do mathematical operations
'''Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modules (%)
Floor Division(//)
Exponential(**)'''

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

#Converting types
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)
print(numpy_int_arr.astype('str'))

#Getting items
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
print(first_row)
first_column= two_dimension_array[:,0]
print(first_column)
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
print(two_dimension_array[::])
print(two_dimension_array[::-1,::-1]) #reverse the whole array
two_dimension_array[1,2] =44 #Changing values
print(two_dimension_array)

numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)

#Reshape
first_shape  = np.array([(1,2,3), (4,5,6)])
reshaped = first_shape.reshape(3,2)
print(reshaped)
#Flatten
flattened = reshaped.flatten()
print(flattened)

#Horizontal and vertical Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))

#Random numbers
    #float 
random_float = np.random.random(3)
print(random_float)
    #int
random_int = np.random.randint(0, 11) #between 0 and 10
print(random_int)
random_int = np.random.randint(0,11, size=(3,3))
print(random_int)
    #normal distribution
normal_array = np.random.normal(79, 15, 5) #79: mean, 15:std, 5:numbers
print(normal_array)
    #random letters
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
    #random floats with shape
rand = np.random.rand(2,2) #numbers between [0,1] of shape 2,2
print(rand)


#matrix
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print(four_by_four_matrix)
np.asarray(four_by_four_matrix)[2] = 2 #change values
print(four_by_four_matrix)

#arange
odd_numbers = np.arange(1, 20, 2)
print(odd_numbers)

#Creating sequence of numbers
print(np.linspace(1.0,5.0, num=10, endpoint= False)) #10 values between 1 and 5
print(np.logspace(1, 5.0, num=10)) #same as np.linespace but log scale

#NumPy Statistical functions
np_normal_dis = np.random.normal(5, 0.5, 5)
print(np_normal_dis.min())
print(np_normal_dis.max())
print(np_normal_dis.mean())
print(np_normal_dis.var())
print(np_normal_dis.std())
print(np.median(np_normal_dis))
    #if multiple dimensions
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
from scipy import stats
print(stats.mode(np_normal_dis))

#Repeating sequences
a=[1,2,3]
print(np.tile(a, 2)) #[1 2 3 1 2 3]
print(np.repeat(a, 2)) #[1 1 2 2 3 3]

import matplotlib.pyplot as plt
import seaborn as sns
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show();

#linear algebra
    #dot product
f = np.array([1,2,3])
g = np.array([4,5,3])
print(np.dot(f, g))  # 1*4+2*5 + 3*6= 23
    #matrix multiplication
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
print(np.matmul(h, i)) ### 1*5+2*7 = 19...

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show();

mu = 28
sigma = 15
samples = 100000
x = np.random.normal(mu, sigma, samples)
ax = sns.histplot(x)
ax.set(xlabel="x", ylabel='y')
plt.show();

'''To summarize, the main differences with python lists are:
Arrays support vectorized operations, while lists don’t.
Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
Every array has one and only one dtype. All items in it should be of that dtype.
An equivalent numpy array occupies much less space than a python list of lists.
numpy arrays support boolean indexing.'''