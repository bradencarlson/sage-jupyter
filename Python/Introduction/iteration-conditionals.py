#!/usr/bin/env python
# coding: utf-8

# # Iteration and Conditionals

# ## Loops and Iteration

# Previously, we saw how to declare lists for our use, and how to access their elements.  In our study of Abstract Algebra, there will be many situations where we need to perform an operation many times on many different elements.  One example of this that we will see in the future is computing a Coset of an element in a given group.  For now we will deal with simpler examples.  Consider the list defined below.  If we want to add all the elements of this list together and print out the sum, we could define a new variable called `total`, then use a `for` loop to iterate over each element in the list. Run the next cell.

# In[ ]:


# define the list x
x = [3,5,4,6,5]

# define the new variable total
total = 0

# use a for loop to go through each element in the list
for item in x:
    total = total + item
    
# when its done, print out the total
print(total)


# There are several new ideas in the cell above.  First of all, `for item in x` is the declaration of the `for` loop.  This tells the program to do some set of actions for each element in the list `x`.  The set of actions that we wish the program to execute for each element in the list `x` is denoted by an indented block of code.  So notice that since the `print(total)` statement is not indented, it is not executed by the for loop, but rather, the program waits until the for loop is finished to execute that line of code.  This same code could have been executed in a different, but similar, way, as follows.

# In[ ]:


# define the list x
x = [3,5,4,6,5]

# define the new variable total
total = 0

# use a for loop to go through each element in the list
for i in range(0,len(x)):
    total = total + x[i]
    
# print out the total
print(total)


# Very similar, but the notable difference is in the syntax of the for loop.  This code uses an index to access the items in the list `x` rather than telling the interpreter to access them directly.  That being so, we must tell the program which values of `i` we want it to use.  The command `range(0,len(x))` is how we accomplish this.  This command creates a new list of integers from and including zero, to but not including `len(x)`, which is the length of `x`, in this case 5.  There will situations where one of these methods is advantageous over the other, depending on what our code needs to do.  
# 
# There are other types of ways to perform iteration, such as the while loop, but in this project, we will gain the most mileage out of the for loop.  For more information about how to use loops, please visit [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

# ## Conditional Statements

# Being students of mathematics, conditional statements and logic come up frequently.  Python provides a rich set of options that we can use to implement some logic in our code as we go through some of the topics in Abstract Algebra. Consider the following cell.

# In[ ]:


x = 1000

if x > 500:
    print(f"{x} is greater than 500")
else:
    print(f"{x} is less than 500")


# The second print statement is not evaluated at all, because the conditions for that block of code are not satisfied.  This allows us alot of options when we are using Sage, for example, we will see this when we test to see if two groups are isomorphic, or if two cosets are equal to each other.  Another way we can implement conditional logic is the following.

# In[ ]:


x = [100,200,309,293,487,293,123,243,198,475,398,847,876,435,321,345,623,546,786,765,487,172]

OneHundreds = 0
TwoHundreds = 0
ThreeHundreds = 0
FourHundreds = 0
FiveHundreds = 0
SixHundreds = 0
SevenHundreds = 0
EightHundreds = 0
NineHundreds = 0

for number in x:
    if number <= 100:
        OneHundreds = OneHundreds + 1
    elif number <= 200:
        TwoHundreds = TwoHundreds + 1
    elif number <= 300:
        ThreeHundreds = ThreeHundreds + 1
    elif number <= 400:
        FourHundreds = FourHundreds + 1
    elif number <= 500:
        FiveHundreds = FiveHundreds + 1
    elif number <= 600:
        SixHundreds = SixHundreds + 1
    elif number <= 700:
        SevenHundreds = SevenHundreds + 1
    elif number <= 800:
        EightHundreds = EightHundreds + 1
    elif number <= 900:
        NineHundreds = NineHundreds + 1
    else:
        print("Number too large.")
        
print(f"total between 400 and 500: {FourHundreds}")


# One might think this code has the mistake that if the current number being considered is 102, then the conditions for all but the first conditional statement are true, and thus the number would be counted multiple times by the program.  This is not so because the `if..elif..else` statement works together as one conditional statement (`elif` is short for "else if").  Once one of the conditions has been met, none of the others are considered.  So for the number 102, the first condition (number <= 100) is not satisfied, but the second one is, thus it is counted with the `TwoHundreds`, and since one of the conditions was already met, while the rest are true, they are not considered, thus giving us the correct counts at the end. 
# 
# W3Schools has a great introduction to `if..else` command in Python, to learn more, go to [Python Conditions](https://www.w3schools.com/python/python_conditions.asp)
