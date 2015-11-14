# Requirements #

  * [Python](http://python.org/download/) (if using the RPM/DEB packages, Python **2.6**, and Python 2.5 should work if installing from source)
  * [PyGTK](http://pygtk.org/downloads.html) (2.12 or above)
  * [GTK+](http://www.gtk.org/download.html) (2.12 or above)
  * [setuptools](http://pypi.python.org/pypi/setuptools)

# Installation instructions #

## Deb or RPM packages ##

  1. Ensure that you have Python, PyGTK, GTK+ and setuptools installed
  1. [Download](http://code.google.com/p/lorem-ipsum-generator/downloads/list) an install either the .deb or .rpm file
  1. A shortcut can be found in your Application menu in the "Other" category. Alternatively the program can be started with the command `lorem-ipsum-generator`.

**Note:** If the shortcut fails to launch the application, this may indicate that one of the dependencies has not been installed correctly, or it is of the wrong version.

**Also:** If you are running a version of Python other than Python 2.6, it is recommended that you install from source, as below.

## Source package installation ##

  1. Ensure that you have Python, PyGTK, GTK+ and setuptools installed
  1. [Download](http://code.google.com/p/lorem-ipsum-generator/downloads/list) and extract the source package (the .tar.gz file).
  1. Open up a terminal and navigate to the extracted directory.
  1. Run the command `python setup.py install` with super-user priveledges (i.e. use su or sudo)
  1. A shortcut can be found in your Application menu in the "Other" category. Alternatively the program can be started with the command `lorem-ipsum-generator`.

**Note:** If the shortcut fails to launch the application, this may indicate that one of the dependencies has not been installed correctly, or it is of the wrong version.

## Source package, without installing ##

  1. Ensure that you have Python, PyGTK, GTK+ and setuptools installed
  1. [Download](http://code.google.com/p/lorem-ipsum-generator/downloads/list) and extract the source package (the .tar.gz file).
  1. Locate the `lorem-ipsum-generator` executable under the `src/` directory of the extracted directory.
  1. Ensure that the `lorem-ipsum-generator` file is executable (`chmod +x lorem-ipsum-generator`), and then run it

**Note:** If the application fails to launch, this may indicate that one of the dependencies has not been installed correctly, or it is of the wrong version.