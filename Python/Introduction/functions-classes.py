#!/usr/bin/env python
# coding: utf-8

# # Functions and Classes

# ## Functions

# Another useful feature of SageMath that is inherited from Python is the concept of a function.  If we ever need to perform the same operation repeatedly, it may be useful to define a function that contains that code instead.  See the code below, where we define the average function, that takes the average of a list.

# In[ ]:


def average(x: list):
    total = 0
    for item in x:
        total = total + item
    
    average = total / len(x)
    
    return average


# After running the cell above, the function `average()` is now available to us.  There are a few things to note here.  In the function declaration, we use the keyword `def`, which is short for define, to let the interpreter know that we are defining a function.  Then we specify the name of the function, and what parameters are needed to use the function.  In this case, the paramter is `x`, and has to be of type `list`.  Then, as we have seen before, we declare a new variable total, sum all the numbers in the list `x`, then we devide the total by the number of elements in `x`, and return that average.  Below we can see this function being used.

# In[ ]:


x = [3,2,4,56,5,4,3,2]
print(average(x))


# Note that even though the variable `x` is used in the function declaration, defining `x=[3,2,4,56,5,4,3,2]` does not affect the function at all.  This is refered to as variable scope, and will not be discussed here.  Here is a more advanced example of a function:

# In[ ]:


# define a new function divisors, that requires a integer.
def divisors(x: int):
    # define a new array to contain all the divisors of x
    divisors = []
    # for each number up to x, if that number is a divisor
    # append it to the array.
    for i in range(1,x+1):
        if x % i == 0:
            divisors.append(i)
    
    # return the list of divisors
    return divisors

print(divisors(12))


# The key word `return` here means that whatever comes after that keyword will be the output of that function.  Functions do not need a return value, but often they are useful.  This means that we can make statements like the following:

# In[ ]:


# define x to be 60
x = 60
# define y to be the list of all divisors of x
y = divisors(x)

# print out y
print(y)


# ## Classes

# While functions alone are often very useful, Often we will wish to use SageMath to represent some sort of object.  We have already been using this terminology in this series of documents, we have introduced the reader to different data types such as `int` and `str` for Integers and Strings, but what these objects really are are classes.  
# 
# There are many pre-defined classes that are ready for us to use once we have loaded SageMath, and although on occasion we will find it useful to define our own classes, for the vast majority of the time we will be using the classes that SageMath has by default.  One such class is the matrix class (technically, the matrix class is what is called an abstract class, and the class the next example uses is the Matrix_Integer_dense class, which is a type of matrix, but we will not worry about that here), for example, to define a matrix, we put:

# In[ ]:


x = matrix([[1,3],[6,3]])
type(x)


# The 'function' `matrix()` that we use here to define the matrix is called a constructor, because it constructs an instance of the class matrix for us to use.  Since `x` is now a matrix object, we have operations that we can use on `x` that we cannot use on lists or Integers or other objects.  For example:

# In[ ]:


print(x.transpose())
y = x.echelon_form()

# print a blank line
print()
print(y)


# The reason behind this is because the matrix class has functions built into it that lists and Integers do not.  Representing real everyday objects in programming with classes is refered to as Object Oriented Programming, and is very powerful.  We will see a few custom classes defined in this course, namely when we look in Algebraic Coding theory.  For now, we merily need to know that they are out there.
