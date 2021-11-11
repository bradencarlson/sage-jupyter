# Project Sage-Jupyter
SageMath files (via Jupyter Notebooks) that give an introduction to using SageMath to explore selected topics in Abstract Algebra.

Originally created as a project for Math 4220 at Southen Utah University, this Project will guide the user through installing SageMath and Jupyter Notebooks.  Then the
user will be introduced to basic computations in SageMath, as well as experimenting with group theory.  SageMath provides a rich environment for visualizing and 
experimenting with groups, including functionality with subgroups, cayley tables, isomorphisms, and more.

The goal of this Project is to help students everywhere, although it is primarily aimed at students of Abstract Algebra, to learn the syntax of SageMath, so as 
to provide them with a helpful tool to visualize and understand the topics taught in an undergraduate Abstract Algebra course.  While doing this, this Project 
will also guide the user through a few important and very interesting applications of the theory that is being studied, such as the Ceasar Cipher, the RSA 
Encryption system, as well as Algebraic Coding theory.   

## No Installation? No Problem!

This Project may be used with no local installation of SageMath or Jupyter Notebooks.  If one does not have access to these resources, 
all code used in this Project may be executed on the [Sage Cell](https://sagecell.sagemath.org/) webpage.  To do this, please visit the [Python](Python) folder, 
and copy the code that needs to be run, this code should then be pasted into the cell at the webpage above and can then be executed.   

## How to Help

If at any point while using this Project you encounter an error, or you would like to see an additional topic discussed, or if any of the topics discussed are 
unclear or need more explanation, please feel free to fill out an Issues form under the [Issues](https://github.com/bradencarlson/sage-jupyter/issues) tab.

## Getting Started

While the entirety of this Project may be used without installing SageMath or Jupyter Notebooks, the crux of this Project is to use both of these programs to 
help us better understand Abstract Algebra, thus in this project we will discuss how to [install SageMath](Installation/sage-installation.md) as well as how to
[install Jupyter Notebooks](Installation/jupyter-installation.md) onto a local machine to get the user up and running with both of these powerful programs.

We well then guide the user on how to [run a Jupyter Notebook Server](Running/running-jupyter.md).  Once these preliminary tasks are taken care of, we begin the 
discussion of selected topics in Abstract Algebra.  This will take place in a number of Jupyter Notebooks.  Note that the sequence of these notebooks will follow 
the Youtube series of [Abstract Algebra lectures](https://www.youtube.com/playlist?list=PLz7t89zv8Lp2D6xQOG7kUEbN1KP5u-mpH) given by Dr. Andrew Misseldine at 
Southen Utah University.  

We will mention here that while learning the SageMath syntax is much like learning any other computer programming language, in that it is done through much
trial and error, this project assumes that the user has little to no experience with SageMath or any other programming language.  Thus included in this Project 
is a very basic introduction to the syntax and some basic ideas of any programming language such as data types, conditional statements, variables, print 
statements, functions and classes, and more. All of the documents here in this Project are set up to run without the user having much knowledge about how the
language works, although most code is either commented or coupled with notes to inform the user of what the code is trying to accomplish.  Thus, any student of 
SageMath will find this Project helpful in their journey to using SageMath. 

## Series

This series can be followed however the user wishes, but was designed to go in the following order:

0. Beginnings
    1. [Install SageMath](Installation/sage-installation.md)
    2. [Install Jupyter Notebooks](Installation/jupyter-installation.md)
    3. [Running a Notebook](Running/running-jupyter.md)
1. [Introduction](Introduction)
    1. [Basic Introduction](Introduction/basic-introduction.ipynb)
    2. [Conditionals and Iteration](Introduction/iteration-conditionals.ipynb)
    3. [Functions and Classes](Introduction/functions-classes.ipynb)
2. [Groups](Groups)
    1. [Modular Arithmetic](Groups/modular-arithmetic.ipynb)
    2. [Groups](Groups/Groups.ipynb)
    3. [Subgroups](Groups/Subgroups.ipynb)
    4. [Cosets](Groups/Cosets.ipynb)
3. [Cryptography and Coding Theory](Cryptography)
    1. [Ceasar Cipher](Cryptography/CeasarCipher.ipynb)
    2. [Frequency Analysis](Cryptography/FrequencyAnalysis.ipynb)
    3. [Hill Cipher](Cryptography/Hill-cipher.ipynb)
    4. [RSA Encryption](Cryptography/RSA-encryption.ipynb)
    5. [Coding Theory](Cryptography/AlgebraicCoding.ipynb)
4. [Isomorphisms and Direct Products](Groups/Isomorphisms-Direct-Products.ipynb)
