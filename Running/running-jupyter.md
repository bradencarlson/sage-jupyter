# Running Jupyter Notebooks

## Linux

To run Jupyter Notebooks in Linux after it has been [installed](../Installation/jupyter-installation.md), we have a few options.  To start Jupyter Notebooks at your home directory, type the command

>`jupyter notebook`

There are a few options we can use at the command prompt when using this command, see 

>`man jupyter notebooks` 

for more information.  Alternatively, assuming that SageMath has been [installed](../Installation/sage-installation.md) correctly, we can use the command 

>`sage -n jupyter`

which will start Jupyter Notebooks at our home directory. Once again, there are many options to use while doing this at the command propmt, see the manual pages for
more details on using this command.  

To quit the Jupyter Notebook Server, we can navigate to the main page (in which we can see all our documents), and in the top right corner, select Quit.  This will 
shutdown the server.  Alternatively, we can navigate to the terminal from which we started the server from, and interupt it using the command `ctrl c`, Jupyter 
Notebooks will then confirm that we wish to shut down the server, to which we will respond `y`, then Jupyter will be shut down.  

## Windows

To run Jupyter Notebooks on Windows after it has been [installed](../Installation/jupyter-installation.md), Search Jupyter at the search bar in the bottom left, and select run.  This will launch Jupyter Notebooks in a browser for you 
to use.  To quit Jupyter Notebooks, go to the browser in which it is running, and in the Jupyter Notebooks main page (where you can see all your documents),
in the top right corner select Quit.  This will shut down the Jupyter Notebook Server.

Alternatively, if during the SageMath [installation](../Installation/sage-installation.md) process, you selected the option to create desktop icons, there may 
(depending on whether or not Jupyter Notebooks was installed at the time of the SageMath installation) be an icon that is labeled "SageMath Server", selecting this 
will start a Jupyter Notebook Server in which we can use SageMath.

## MacOS

This section coming soon.
