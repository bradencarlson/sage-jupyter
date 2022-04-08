<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/bradencarlson/sage-jupyter" ></a>
<img src="https://img.shields.io/github/issues-raw/bradencarlson/sage-jupyter"></a>
<img src="https://img.shields.io/github/issues-closed-raw/bradencarlson/sage-jupyter"></a>
<img src="https://img.shields.io/github/last-commit/bradencarlson/sage-jupyter"></a>
<img src="https://img.shields.io/github/repo-size/bradencarlson/sage-jupyter"></a>


# Project Sage-Jupyter
SageMath files (via Jupyter Notebooks) that give an introduction to using SageMath to explore selected topics in Abstract Algebra.

Originally created as a project for Math 4220 at Southern Utah University, this Project will guide the user through installing SageMath and Jupyter Notebooks.  The 
user will then be introduced to basic computations in SageMath, as well as experimenting with group theory.  SageMath provides a rich environment for visualizing 
and experimenting with groups, including functionality with subgroups, cayley tables, isomorphisms, and more.

The goal of this Project is to help students everywhere, although it is primarily aimed at students of Abstract Algebra, to learn the syntax of SageMath, so as 
to provide them with a helpful tool to visualize and understand the topics taught in an undergraduate Abstract Algebra course.  While doing this, the Project 
will also guide the user through a few important and very interesting applications of the theory that is being studied; such as the Ceasar Cipher, the RSA 
Encryption system, as well as Algebraic Coding theory.   

## No Installation? No Problem!

This Project may be used with no local installation of SageMath or Jupyter Notebooks.  If one does not have access to these resources, 
all code used in this Project may be executed on the [Sage Cell](https://sagecell.sagemath.org/) webpage.  To do this, please visit the [Python](Python) folder, 
and copy the code that needs to be run. This code should then be pasted into the cell at the webpage above and can then be executed.  

In Addition to SageCell, which gives a feel for what it would be like to run this code from a terminal, an online alternative to Jupyter Notebooks is also 
available.  [CoCalc](https://cocalc.com/) is a great resource that may be used as an alternative to Jupyter Notebooks.  This will allow the user to view the 
documents used in this Project just as they were designed to be seen in Jupyter Notebooks.  To use this resource, download the code 
that needs to be run, (either the python code or the original `.ipynb` files, note that the latter will give prettier output), create an account with CoCalc, 
create a new project, and upload the file that needs to be executed.  **CoCalc is a free service, but there is a
[disclaimer](https://doc.cocalc.com/trial.html) that should be noted.**

## How to Help

If at any point while using this Project you encounter an error, you would like to see an additional topic discussed, or if any of the topics discussed are 
unclear or need more documentation, please feel free to fill out an Issues form under the [Issues](https://github.com/bradencarlson/sage-jupyter/issues) tab.

Please see our [Contributing](.github/CONTRIBUTING.md) page for more information.

## Getting Started

While the entirety of this Project may be used without installing SageMath or Jupyter Notebooks, the crux of this Project is to use both of these programs to 
help us better understand Abstract Algebra, thus, in this Project we will discuss how to [install SageMath](Installation/sage-installation.md) as well as how to
[install Jupyter Notebooks](Installation/jupyter-installation.md) onto a local machine to get the user up and running with both of these powerful programs.

We will then guide the user on how to [run a Jupyter Notebook Server](Running/running-jupyter.md).  Once these preliminary tasks are taken care of, we begin the 
discussion of selected topics in Abstract Algebra.  This will take place in a number of Jupyter Notebooks.  Note that the sequence of these notebooks will follow 
the Youtube series of [Abstract Algebra lectures](https://www.youtube.com/playlist?list=PLz7t89zv8Lp2D6xQOG7kUEbN1KP5u-mpH) given by Dr. Andrew Misseldine at 
Southen Utah University.  

We will mention here that while learning the SageMath syntax is much like learning any other computer programming language, in that it is done through much
trial and error, this project assumes that the user has little to no experience with SageMath or any other programming language.  Thus included in this Project 
is a very basic introduction to the syntax and some basic ideas of any programming language; such as data types, conditional statements, variables, print 
statements, functions and classes, and more. All of the documents here in this Project are set up to run without the user having much knowledge about how the
language works, although most code is either commented or coupled with notes to inform the user of what the code is trying to accomplish.  Thus, any student of 
SageMath will find this Project helpful in their journey to using SageMath. 

## Package

This project can now be found in a package! Please keep in mind that this package is still a work in progress, and is not fully functional at the moment.  Please 
visit the [Projects](https://github.com/bradencarlson/sage-jupyter/projects?type=beta) page to see which functions are working at the moment. 

Also note that this package, while found on [PyPi](https://pypi.org/project/sage-aata/), is made to be used with SageMath, and not Python.  This package can be 
installed with the following command:

```
python3 -m pip install sage-aata
```

And updated with the command 

```
python3 -m pip install --upgrade sage-aata
```



## Series

This series can be followed however the user wishes, but was designed to go in the following order:

0. Beginnings
    1. [Install SageMath](Installation/sage-installation.md)
    2. [Install Jupyter Notebooks](Installation/jupyter-installation.md)
    3. [Running a Notebook](Running/running-jupyter.md)
1. [Introduction](Introduction)
    1. [Basic Introduction](Introduction/basic-introduction.ipynb)
    2. [Conditionals and Iteration](Introduction/iteration-conditionals.ipynb)
    3. [Dictionaries](Introduction/Dictionaries.ipynb)
    4. [Functions and Classes](Introduction/functions-classes.ipynb)
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
    6. [Vigenere Cipher](Cryptography/VigenereCipher.ipynb) (optional)
    7. [Autokey Cipher](Cryptography/AutoKeyCipher.ipynb) (optional)
4. [More Groups](Groups)
    1. [Isomorphisms and Direct Products](Groups/Isomorphisms-Direct-Products.ipynb)
    2. [Conjugacy Classes](Groups/Conjugacy-classes.ipynb)
    3. [Matrix Groups](Groups/matrix-groups.ipynb)
5. [Rings](Rings)
    1. [Rings](Rings/Rings.ipynb)
6. [Group Rings](Group-Rings)
    1. [Group Rings](Group-Rings/GroupRings.ipynb)
7. [Fields](Fields)
    1. [Fields](Fields/Fields.ipynb)

## Miscellaneous Files

In the Misc folder, we discuss selected topics that do not neccessarily have to do with the Abstract Algebra course taught by Dr. Andrew Misseldine 
at Southern Utah University.  In this folder we currently have files that dicuss:

- [SageMath and Latex](Misc/sage-latex.ipynb)
- How to write a program for the [Euclidean Algorithm](Misc/Euclid.ipynb)
- How to write a program for the [Repeated Squares](Misc/repeated-squares.ipynb) algorithm

We also have a few files written in `c` that implement some of the algorithms found in this project.
