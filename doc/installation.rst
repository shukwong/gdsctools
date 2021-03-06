
.. index:: installation, pip, anaconda
.. _installation:

Installation
================

**GDSCTools** is written in Python and depends on a set of established scientific libraries such as `Matplotlib <http://matplotlib.org/>`_ (visualisation) and `Pandas <http://pandas.pydata.org/>`_ (data manipulation) to cite just a few. We post releases on the `Python repository  <https://pypi.python.org/pypi/gdsctools>`_ and make use of the Python ecosystem to provide a robust software. Would you have any trouble, please see the :ref:`faqs` or fill an `issue/ticket <https://github.com/CancerRxGene/gdsctools/issues>`_ on github.


Python users and developers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Releases of **GDSCTools** are available on `Pypi <https://pypi.python.org/pypi/gdsctools/0.2.0>`_ so **GDSCTools** can be installed in a :term:`Terminal` using the **pip** command::

    pip install gdsctools

Dependencies (e.g., Pandas, Matplotlib) should be taken care of automatically.

If you are new to Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are not familiar with Python, or have issues with the previous method (e.g., compilation failure), or do not have root access, we would recommend to use the `Anaconda <https://www.continuum.io/downloads>`_ solution.

Anaconda is a free Python distribution. It includes most popular Python packages for science and data analysis. Anaconda will install the software required by  **GDSCTools**. Since it does not require root access, it should not interfere with your system.

Please, visit the `Anaconda <https://www.continuum.io/downloads>`_ website and follow the instructions. You may need to choose between 2 versions of Python (2.X or 3.5). **GDSCTools** is tested under Python 2.7 and 3.5 (as well as 3.3 and 3.4) so the version should not matter.


Once anaconda is installed, open a new :term:`Terminal` (under Windows, open the
Anaconda prompt) and type::

    conda install numpy pandas numexpr matplotlib pandas scipy jinja2 statsmodels scikit-learn

Other dependencies and **GDSCTools** itself can be installed as follows::

    pip install gdsctools

alternatively, if you prefer to get the source code (latest version), first
obtain the source code and install manually the latest code::

    # go in a working directory and type:
    git clone https://github.com/CancerRxGene/gdsctools
    cd gdsctools
    python setup.py install

Install IPython
~~~~~~~~~~~~~~~~~~~~~

This is not strictly speaking required to use **GDSCTools**, but we strongly
recommend to install IPython that provides a specialised shell for Python
users. If you have installed Anaconda, just type::

    conda install ipython

otherwise::

    pip install ipython


You have already installed GDSCTools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have already installed **GDSCTools** and want to get the latest
release, use the **pip** as follows::

    pip install gdsctools --upgrade

If you used the source code from github, then, get the lastest source code and install again. Assuming you have installed the source code from github in **github_gdsctools** directory, then type::

    cd github_gdsctools
    git pull
    python setup.py install


Testing your installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should now be ready to use **GDSCTools**. A good test is to check
that the following executable is available. In a shell, type::

    gdsctools_anova --test

or ::

    gdsctools_anova --help

or for developers, start an IPython shell, and type for example::

    from gdsctools import *
    an = ANOVA(ic50_test)

Please, go to the next section for a :ref:`quickstart` session.

Open an IPython shell
~~~~~~~~~~~~~~~~~~~~~~~~~

Under Windows, got to All Programs-->Anaconda -->Anaconda Prompt.

A shell will be opened where you can type **ipython** command.

Or alternatively, under Windows, got to All Programs-->Anaconda -->IPython

Notes for windows/mac/linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Anaconda method was tested successfully on the following systems: MAC,
Windows 7 Pack1, Fedora 19 (Nov 2015) with version 0.16.5 of GDSCTools.

Under Windows, an error was raised due to scipy. This was fixed by typing::

    conda remove scipy scikit-learn -y
    conda install scipy scikit-learn -y

https://github.com/scikit-learn/scikit-learn/issues/4830
