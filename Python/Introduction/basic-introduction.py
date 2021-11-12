#!/usr/bin/env python
# coding: utf-8

# # Using SageMath 

# ## Commands and Operators

# This will be a basic introduction to SageMath, and its syntax, to provide us the tools we will need to study some Abstract Algebra.  First of all, each input and output box is referred to as a cell.  SageMath will only run one cell at a time unless instructed to do otherwise. All SageMath code is run in the Sage kernel, which can be used outside of Jupyter Notebooks, although Jupyter provides us with a good environment to develop our understanding, so we will be using Jupyter Notebooks.
# 
# In Sage, if a cell has a box around it with a blue tab on the left side, this means we have selected that cell in Command mode, while if a cell has a box around it with a green tab on the left side, this indicates that we have selected that cell in Edit mode.  If we are in Command mode (blue), we can use the keys `j` and `k` to move our selection down and up, respectively (the arrow keys also work).  We need to be very careful though, while in Command mode, the command `dd` will delete the current cell and Sage will not ask you if you are sure that you want to delete it.  For this reason, I recommend using the command `ctrl + S` frequently, which creates a checkpoint, just in case we make any mistakes.  There are many keyboard commands that you could accidentally type while in Command mode,  click on `help` and then `keyboard shortcuts` to see more.  If at any point, we accidentally delete somthing, we can open `file` and then select `revert to checkpoint` to undo any changes since the last checkpoint.  
# 
# When we open a document that we have already created, the SageMath kernel does not remember anything that we have already written in the document, each cell must be run again if the kernel is to use any information contained in that cell.  For example, in the next cell, we define a varible `x = 56`, then in the following cell, we use the `print` function to print out the value of `x`.  While in Command mode, use the command `Ctrl+Enter` to run the following two cells to see this in action. 
# 
# Note: If in Command mode, to enter Edit mode, hit `Enter`, if in Edit mode, to enter Command mode, hit `Esc`.

# In[ ]:


x = 56
print(x)


# If done correctly, we should now see the number 56 below the statement `print(x)`.  Here we introduce a few more operators that we will use frequenly, `=`, `+`, `-`, `*`, `/`, `%`, and `//`.  Most of these work how we would expect them to. That is, `+` is addition, `-` is subtraction, and `*` and `/` are multiplication and division.  In Sage, the `=` operator is not used as a statement of equality, but rather as an assignment.  Take for example the code above, this cell **assigns** the variable `x` the value of 56, we will see many examples of this and use it often.  The `%` operator gives us the residue mod *n* of a number.  The `//` operator will give us the quotient when one number is divided by the other.  For example:

# In[ ]:


x = 103454
y = 34865
print(f"The sum of {x} and {y} is {x+y}")
print(f"x/y = {x/y}")
print(f"x mod y = {x%y}")
print(f"The quotient when x is divided by y is {x//y}")


# You may notice in the code above that in the print statements, although we type statments such as `x//y`, we do not see the literal characters "x//y" print out to the screen, but rather the value of the calculation.  This is due to String formatting in Python.  If you are familiar with Python, first of all this introduction must seem pretty dull, but the syntax of the code will be pretty much the same, although we will see in the future some things that we can use in SageMath that are not readily available to us in Python.  When we wish to format a String in Python (or in SageMath), one way of doing so is to put the letter `f` in front of the string itself, and then any variable that we place in brackets in the string will be formatted as its value.  For example, the code
# 
# > x = 56  
# > print(f"The value of x is {x}")
# 
# will print out "The value of x is 56" becuase the second `x` is placed in brackets.
# 
# At any point in this brief introduction to the syntax of SageMath, to practice or experiment with the commands we are discussing, while in Command mode we can use the commands `a` or `b` to place a new cell `a`bove or `b`elow the selected cell so that you have a new environment to enter Edit mode and write your code. 
# 
# Exponents in SageMath are implemented with the `^` command.  See below.

# In[ ]:


print(2^8)


# Here are a few more examples of performing basic arithmetic in SageMath.  Remember at any time, while in Command mode, you can press the buttons `a` or `b` to create a new cell, then press `enter` to edit that cell to practice on your own.

# In[ ]:


x = 10^500
print(x/6.745)


# In[ ]:


x = 5.67
y = 3.45423
z = 9.3861

total = x + y + z
average = total/3

print(f"The average of these three numbers is {average}")


# It is important to know that Python (and by extension, SageMath) follows the order of operations.  Thus if we run the code 
#  
# > 5+4\*3-(10+4)\*\*2
# 
# We would get exactly what we would expect to, since Python knows what we mean when we type this in.
# 

# In[ ]:


5+4*3-(10+4)**2


# This is important to know, although we may not use it much in our study of Abstract Algebra. 
# 
# Another thing to note, in Python, we are allowed to perform multiple assignments at once.  We will demonstrate with the following code.

# In[ ]:


x, y, z = 1, 5, 6

print(x)
print(y)
print(z)


# We can see that the line 
# 
# > x, y, z = 1, 5, 6
# 
# assigns $x\rightarrow 1$, $y\rightarrow 5$, and $z\rightarrow 6$, in the order that they were declared.  This is useful for writing compact code.  

# #### Comments
# 
# We will use many, many comments.  Comments help us to understand what code is doing (both others' code and our own when looking back on it).  Most of the code here in this project will have comments or commentary to go along with it.  To write a comment in our code in Python, or in SageMath, we use the `#` symbol.  This tells the Python interpreter that the line following that symbol is not code and does not need to be run.  See the following code for an example. 

# In[ ]:


# This line is a comment
x, y = 1, 2

# here we print out the values of x and y
print(x, " ", y)

# change the value of x to be 17
x = 17

# print out the new value of x
print(x)


# ## Types of Data

# In SageMath (and any other object oriented programming language), any kind of data or information we put into the code is assigned (or rather declared) as a type of object.  To see this in action, run the code below and observe the output.

# In[ ]:


x = 56
print(type(x))


# We should see the text "<class 'sage.rings.integer.Integer'>" below the cell above.  If using SageMath as a simple calculator such as the examples above, one does not need to worry about this much, but we will see later on, that this will be very important to us in our study of Abstract Algebra, since different types of objects are often not compatible with one another.  We can see this in the next example, try to run the following code.

# In[ ]:


x = 56
y = "hello"
print(f"The type of x is {type(x)} and the type of y is {type(y)}")
x+y


# We should see that the `print` statement runs just fine, but since x is an Integer object while y is a 'str' (short for String) object, we should see an error message, which will give us information about where the error happened, as well as a summary of the error in the last line, which should read "TypeError: unsupported operand parent(s) for +: 'Integer Ring' and <class 'str'>'".  
# 
# Be careful when writting your own code in SageMath, if you are not careful with what types of data you are working with, your code may not run as expected, or at all.  There are many different types of data available to us
# 
# * str
# * Integer Ring
# * Lists
# * Matrices
# * and many others
# 
# Above, we see that lists are a data type that we are able to use.  These are very useful and they are defined by enclosing the desired information in the list with brackets, each separated by a comma.  See the example below.

# In[ ]:


y = [1,4,3,23,4,32,5]
print(y)
print(type(y))


# We can then access individual elements of the list by typing commands such as
# 
# > y = [2,3,3,2]  
# > print(y[0])  
# > y[0] = 5  
# > print(y)
# 
# which will print out the first element of y, which is 2, then will change the first element of y to 5, then will print the list y.  Note that the first element of a list is in spot zero.  Also, attempting to access an invalid index of a list will result in an error.  For example, try to run the following code.

# In[ ]:


y = [1,10,30,40] # spots 0,1,2,3 are available
print(y[4])


# There is much to learn about many different data types and how the all play together.  This document mainly uses the part of SageMath that is inherited from Python, with the notable exception of the Integer Ring class that we have been introduced to.  For more information about data types in Python please see [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp) by W3Schools.
# 
# At this point, we might be tempted to try something such as multiplying all of the elements in a list by some number, much as we would with a vector, run the following code and notice that no error messages are given.

# In[ ]:


x = [2,4,6,8]
y = 2*x


# Although nothing went wrong during runtime, this code did not do what we thought it would, to see this, let's find out what is being stored in `y`.

# In[ ]:


print(y)


# We should see two copies of the list `x`, one after the other, stored in `y`.  So it did not multiply each element by 2, but rather, made two copies of the list!  Take some time to experiment with lists, for we will see these often in our study of Abstract Algebra.
