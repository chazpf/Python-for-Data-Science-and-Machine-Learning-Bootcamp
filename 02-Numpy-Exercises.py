# #### Import NumPy as np

import numpy as np

# #### Create an array of 10 zeros

np.zeros(10)

# #### Create an array of 10 ones

np.ones(10)

# #### Create an array of 10 fives

np.zeros(10) + 5

# #### Create an array of the integers from 10 to 50

np.arange(10,51)

# #### Create an array of all the even integers from 10 to 50

np.arange(10,51, 2)

# #### Create a 3x3 matrix with values ranging from 0 to 8

np.arange(9).reshape(3,3)

# #### Create a 3x3 identity matrix

np.eye(3)

# #### Use NumPy to generate a random number between 0 and 1

np.random.rand(1)

# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

np.random.randn(25)

# #### Create the following matrix:

np.linspace(0.01,1,100).reshape(10,10)

# #### Create an array of 20 linearly spaced points between 0 and 1:

np.linspace(0,1,20)

# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

mat = np.arange(1,26).reshape(5,5)
mat

mat[2:,1:]

mat[3,4]

mat[:3, 1:2]

mat[4,:]

mat[3:]

# #### Get the sum of all the values in mat

mat.sum()

# #### Get the standard deviation of the values in mat

mat.std()

# #### Get the sum of all the columns in mat

mat.sum(axis=0)
