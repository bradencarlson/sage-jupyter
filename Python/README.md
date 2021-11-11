# Python Files

## Sage Cell

If no local installation of SageMath or Jupyter Notebooks are available, each of these files may be copied and pasted in the 
[Sage Cell](https://sagecell.sagemath.org/) webpage, and ran there online.  This is a good alternative for people who have encountered troubles installing SageMath 
onto their machines.  

## Sage and the Command Prompt

This section of the Sage-Jupyter Project is not meant for the beginning student, as some familiarity with a command line or a terminal is recommended. 
If the user is a beginning student, I would highly recommend using either Jupyter Notebooks or the [Sage Cell](https://sagecell.sagemath.org/) webpage to explore 
this Project.

These Python files may be used with SageMath without the need for a local installation of Jupyter Notebooks.

While working with a SageMath document in Jupyter Notebooks, we have the option of downloading the document as a Python file.  We need to be very careful when 
doing this, since some of the functions that we are using in SageMath are not readily available in Python.  Thus, if we download any one of our documents 
as a Python file, we will still need to run it as a SageMath document.  For example, if I would like to run the file AlgebraicCoding.py, I would open a sage
terminal (typing `sage` in linux, selecting the SageMath icon in Windows), and navigating to the directory in which the python file is saved.  After I have
navegated to the correct directory, I can run the Python file with SageMath by typing the command `load('AlgebraicCoding.py')` to run the file containing the 
information about algebraic coding theory.

Also note that in some of the documents that have been prepared and uploaded as part of this project, there are intentional mistakes in the code to 
demonstrate to the the user how SageMath reports these errors.  When downloading these files as python files, even while running them as a SageMath document,
once the error is encountered, execution of the file will stop.  For the majority of the documents in this project this will not be a problem, as they all
run without runtime errors.  

Files listed here that do have intentional errors:

* [Basic Introduction](Introduction/basic-introduction.py)
