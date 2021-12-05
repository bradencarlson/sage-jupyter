#!/usr/bin/env python
# coding: utf-8

# # Matrix Groups
# 
# In this document, we explore the Matrix Groups:
# * The General Linear Group
# * The Special Linear Group
# * The Orthogonal Group
# * The Special Orthogonal Group
# * and the Unitary Group
# 
# In SageMath, these groups are use the following syntax:
# 
# | Group Name |   Syntax |
# |---------------|----------|
# |    General Linear Group of degree $n$ over field $F$:    |    GL($n$,$F$)    |
# |    Special Linear Group of degree $n$ over field $F$:    |    SL($n$,$F$)    |
# |    Orthogonal Group of degree $n$ over field $F$:        |    GO($n$,$F$)    |
# |    Special Orthogonal Group of degree $n$ over field $F$:|    SO($n$,$F$)    |
# |    Unitary Group of degree $n$ over field $F$:           |    GU($n$,$F$)    |   
# |    Special Unitary Group of degree $n$ over field $F$:   |    SU($n$,$F$)    |
# 
# 
# We also make a note here that the field $\mathbb{R}$ in SageMath is denoted $RR$ and the field $\mathbb{C}$ is denoted $CC$.  Finite fields are denoted GF($p$), where $p$ is necessarily a prime.
# 
# Here we go over an example, we note that from Linear Algebra, that the area of the parallelogram given by two vectors in $\mathbb{R}^2$ is 
# 
# \begin{equation*}
# A=\det([\vec{x}\:\: \vec{y}]) 
# \end{equation*}
# 
# where $\vec{x}$ and $\vec{y}$ are written as column vectors.  Thus if we take any element of $SL_2(\mathbb{R})$, then we have that the area of the parallelogram with sides $A\vec{x}$ and $A\vec{y}$ is the same as the area of the parallelogram with sides $\vec{x}$ and $\vec{y}$.  We leave the proof to the reader, but provide numerical evidence here. 

# In[ ]:


# here we define the Special Linear Group of degree 2 over the Real numbers.
# then we define R^2 to be the set of all 2x1 matrices with Real entries,
# as well as the MatrixSpace of all 2x2 matrices with Real entries, this will only 
# be used to calculate the determinants (and thus the areas) for the problem given. 
S = SL(2,RR)
M1 = MatrixSpace(RR, 2, 1)
M2 = MatrixSpace(RR, 2, 2)

# here we define an element of SL_2(R), that will be used for scaling x and y to see
# that the area is left unchanged.
# feel free to enter your own numbers here to test more matrices from SL_2(R).
A = S([1  , -1 ,
       1/2, 1/2])

# here we define two elements of R^2, once again, feel free to change these numbers to 
# experiment with the values.
x = M1([ 2,0])
y = M1([1,3])

# This defined the matrix with x and y as column vectors, don't change these lines.
area_matrix = M2([x[0][0], y[0][0],
                  x[1][0], y[1][0]])

# print the matrix with x and y as column vectors, then print its determinant, which
# is the area of the parallelogram formed by x and y in R^2
print(area_matrix)
print(f"Area in R^2 before multiplying by A: {area_matrix.determinant()}\n")

# scale both x and y by the matrix A defined above
ax = A*x
ay = A*y

# form a new area matrix with the scaled vectors as columns. 
new_area_matrix = M2([ax[0][0], ay[0][0],
                      ax[1][0], ay[1][0]])

# print out the new matrix, which will have changed, as well as the determinant, which 
# will not change, since SL_2(R) preserves the geometry of R^2
print(new_area_matrix)
print(f"Area in R^2 after multiplying by A: {new_area_matrix.determinant()}\n")

# in these lines, we plot the vectors, as well as the polygons that they form, the
# first graphic is before the transformation, while the second if after the transformation,
# we can see that while the area is preserved, the angle between vectors is not, we will
# see that replacing SL_2(R) by O_2(R) creates a symmetry group that not only preserves 
# distance, but also angles.  
graphics = [
    arrow((0,0),(x[0][0],x[1][0]),arrowsize=2,color='red')+
    arrow((0,0),(y[0][0],y[1][0]),arrowsize=2,color='red')+
    polygon([(0,0),(x[0][0],x[1][0]),(x[0][0]+y[0][0],x[1][0]+y[1][0]),(y[0][0],y[1][0])],alpha=0.5),

    arrow((0,0),(ax[0][0],ax[1][0]),arrowsize=2,color='red')+
    arrow((0,0),(ay[0][0],ay[1][0]),arrowsize=2,color='red')+
    polygon([(0,0),(ax[0][0],ax[1][0]),(ax[0][0]+ay[0][0],ax[1][0]+ay[1][0]),(ay[0][0],ay[1][0])],alpha=0.5)
]

show(graphics[0])
show(graphics[1])


# In[ ]:


# same as above, but replace SL_2(R) with O_2(R)
G = GO(2,RR)
M1 = MatrixSpace(RR, 2, 1)
M2 = MatrixSpace(RR, 2, 2)

# here we define an element of O_2(R),
A = G([3/5,-4/5,
       4/5,3/5])

# here we define two elements of R^2, once again, feel free to change these numbers to 
# experiment with the values.
x = M1([ 2,0])
y = M1([1,3])

# This defined the matrix with x and y as column vectors, don't change these lines.
area_matrix = M2([x[0][0], y[0][0],
                  x[1][0], y[1][0]])

# print the matrix with x and y as column vectors, then print its determinant, which
# is the area of the parallelogram formed by x and y in R^2
print(area_matrix)
print(f"Area in R^2 before multiplying by A: {area_matrix.determinant()}\n")

# scale both x and y by the matrix A defined above
ax = A*x
ay = A*y

# form a new area matrix with the scaled vectors as columns. 
new_area_matrix = M2([ax[0][0], ay[0][0],
                      ax[1][0], ay[1][0]])

# print out the new matrix, which will have changed, as well as the determinant, which 
# will not change, since O_2(R) preserves the inner product of R^2
print(new_area_matrix)
print(f"Area in R^2 after multiplying by A: {new_area_matrix.determinant()}\n")

# same as before
graphics = [
    arrow((0,0),(x[0][0],x[1][0]),arrowsize=2,color='red')+
    arrow((0,0),(y[0][0],y[1][0]),arrowsize=2,color='red')+
    polygon([(0,0),(x[0][0],x[1][0]),(x[0][0]+y[0][0],x[1][0]+y[1][0]),(y[0][0],y[1][0])],alpha=0.5),

    arrow((0,0),(ax[0][0],ax[1][0]),arrowsize=2,color='red')+
    arrow((0,0),(ay[0][0],ay[1][0]),arrowsize=2,color='red')+
    polygon([(0,0),(ax[0][0],ax[1][0]),(ax[0][0]+ay[0][0],ax[1][0]+ay[1][0]),(ay[0][0],ay[1][0])],alpha=0.5)
]

show(graphics[0])
show(graphics[1])

