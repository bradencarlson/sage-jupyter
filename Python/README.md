# Python Files

This section of the Sage-Jupyter project is not meant for the beginning student, as some familiarity with a command line or a terminal is recommended.  If the user is a beginning student, I would highly recommend using Jupyter Notebooks to explore this project.

These Python files may be used with SageMath without the need for a local installation of Jupyter Notebooks.

In Jupyter Notebooks, when working with any type of document we have that option to export that document as a text file, as markdown, and a number
of other options.  While working with a SageMath document, we have the option of downloading the document as a Python file.  We need to be very careful when 
doing this, since some of the functions that we are using in SageMath in our documents are not available in Python.  Thus if we download any one of our documents 
as a Python document, we will still need to run it as a SageMath document.  For example, if I would like to run the file AlgebraicCoding.py, I would open a sage
terminal (typing `sage` in linux, selecting the SageMath icon in Windows), and navigating to the directory in which the python file is saved.  After I have
navegated to the correct directory, I can run the Python file with SageMath by typing the command `load('AlgebraicCoding.py')` to run the file containing the 
information about algebraic coding theory.

Also note that in some of the documents that have been prepared and uploaded as part of this project, there are intentional mistakes in the code to 
demonstrate to the the user how SageMath reports these errors.  When downloading these files as python files, even while running them as a SageMath document,
once the error is encountered, execution of the file will stop.  For the majority of the documents in this project this will not be a problem, as they all
run without runtime errors.  

Files listed here that do have intentional errors:

* [Basic Introduction](Introduction/basic-introduction.py)
