# Installing Jupyter Notebooks

**Note that on most systems SageMath will install Jupyter Notebooks alongside it.  In linux 
try the command** `sage -n jupyter` **or in windows look for the Sage 
Notebook icon to open SageMath in a Notebook.  If this fails, try installing Jupyter Notebooks with the 
instructions below.**

Jupyter Notebooks is a convenient way of veiwing, editing, and dealing with files in general, not just 
Sage files.  Although we will focus on using Sage in 
Jupyter Notebooks, it can be used for many other things.  

To install Jupyter Notebooks on Linux, search your package manager for jupyter.

To install Jupyter Notebooks on Windows and MacOS, go to [Project Jupyter](https://jupyter.org/install), 
and follow the instructions to install Jupyter
Notebooks onto your machine.

## Linking SageMath and Jupyter Notebooks

**Continue with these steps only if you have encountered the error message** 

> kernel not found

**While opening the SageMath files with Jupyter Notebooks.**

Note that on some systems, it may be neccessary to link the sagemath kernel to the installation of Jupyter 
Notebooks so that Jupyter Notebooks knows the commands 
that we will be using in SageMath.  This can be done in the following way.  

### Linux

Run the command `sudo jupyter kernelspec install $SAGEMATH$/jupyter/kernels/sagemath` where `$SAGEMATH
$` is the home folder of your SageMath installation.  

### Windows

A typical installation of SageMath in Windows includes a desktop icon labeled `SageMath Notebook`, that 
will open a Jupyter Notebook running the SageMath kernel. 
Use this option if wanting to run SageMath inside of Jupyter Notebooks.  See 
[SageWindows](https://wiki.sagemath.org/SageWindows) for more details.

### MacOS

This section coming soon.
