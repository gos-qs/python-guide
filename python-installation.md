## Python3 install instructions

Guide for installing a stable and maintainable python3 environment in Windows. There are lots of way to download it, but most result in improperly managed packages which can lead to version-control nightmares. Eg, if programA requires programC-v1, but programB requires programC-v2 you will have no end of trouble if not properly segregating environments.

This guide can be used to install python3 for MacOS, Linux/UNIX-like and Windows, some commands between operating systems differ and the PATH setup also differs a little. I use MacOS and Linux myself. Windows is truly the worst. Windows doesn't have any dependencies on python2 so it's really difficult to brake anything, however there are lots of legacy programs on MacOS, Linux and UNIX-like systems which require that the command 'python' -> python2 rather than python3, so a little more care must be taken when fiddling with the PATH.

I reference Debian based linux in this guide, but there exists many flavours of linux with their own package managers so use the commands and syntax as appropriate to your package manager.

|Command        | Windows                 | Debian-based linux, UNIX-like |
|---------------|-------------------------|-------------------------------|
|list directory |DIR                      |ls                             |
|change direc   |CD $dirname              |cd $dirname                    |
|activate a venv|env1\Scripts\activate.bat|source env1/bin/activate       |

### Download

Quick note before we dive into this, python2 is a legacy version of python which reached end of life support on Jan 1st 2020 meaning no new updates will be made. It was superseded by better syntax, speed improvements and a whole host of other improvements into python3 but the two are NOT interchangeable. The last version of python2 is python2.7.

The differences between python versions after python3.5 are mostly subtle, a few built-in classes which have gained or lost a method/function or attribute. For example the datetime module after version 3.6 includes a few extra methods for ISO format support.

Since you're new, there's no reason to bind yourself to old versions, however, if you want to use python for a specific tool such as Tensorflow then check their github page to make sure they support the latest python version otherwise download the latest one they do support.

#### Windows

[First, download python](https://www.python.org/downloads/windows/)

The "latest release" is the version currently being developed by the open source dev community, it might have some bugs so go for the "stable release".

Most machines are 64-bit these days, so download the "Windows installer (64-bit)" of whichever python version you want, and follow whatever instructions. In the install wizard first page there is a checkbox to "add Python 3.X to PATH", if you have no other python versions then this is a good option. The PATH is a list of locations that the operating system searches when you type a command into CMD/Powershell/terminal, eg, if you typed "shutdown -r now" the the operating system would search the directories in PATH for the command "shutdown" and when found execute it with the arguments "-r now". You can view your PATH as a colon delimited list by typing into CMD/Powershell:

```Powershell
echo %PATH%
```

or for Unix:

```bash
echo $PATH
```

 For python, it means that from CMD/Powershell/terminal you can type "python" or "python3" and enter a simple python scripting shell to run python commands. You can quit from this by executing 'quit()'. Python is really just an alternative shell script engine for converting high level text into low level machine instructions. Any IDE (Interactive Development Environment) like Jupyter, PyCharm, or Spyder that you use isn't necessary to run or write python code it just makes it easier.

#### Debian based linux

Use the apt repository. DO NOT link 'python' -> 'python3', because lots of legacy linux systems require that 'python' -> 'python2.7'. Either rely on venv (described later) to get the right python you intend or use the alternative command 'python3' everywhere. You can install older versions of python3.X using the [deadsnakes](https://github.com/deadsnakes) repository via github or by adding the apt repo with the command: 'sudo add-apt-repository ppa:deadsnakes/ppa'.

```shell
sudo apt install python3
```

#### MacOS / OSX

Use Homebrew. May require some linking after installing. DO NOT link 'python' -> 'python3', because lots of legacy OSX systems require that 'python' -> 'python2.7'.

```shell
brew install python@3.X
```

#### Apple M1

This is a bit more involved. If you require installation instructions for the Apple M1 chipset, see this [guide](m1-installation.md) before proceeding.

<br>

**Pure python is just a text interpreter; it requires no special compilation or IDE to write or distribute code. To execute valid commands/code all that is required is a copy of the python interpreter**

<br>

Once installed, you should be able to open CMD (usually easiest to find by searching "cmd" in the programs) and run simple python commands such as:

```python
python3 -c "my_varname = 'hello world!'; print(my_varname)"
```

"python" is the command, -c means you're giving it a string directly to parse and execute, and if in PATH the string that follows is the argument sent to python to be executed. Python treats the string as python encoded text, the first instruction is to assign the variable name 'my_varname' with the string value 'hello world!', the semicolon signifies the end of that instruction and is necessary if you have multiple commands on one line. The next instruction is to 'print' the value of the variable 'my_varname', internally the print command sends the value of 'my_varname' to the system standard output which is usually the console itself, hence you see the message returned. Another slightly longer example is:

```python
python3 -c "my_greeting = 'Hi there!'; my_name = 'Bob'; my_output = '{0}, {1}'.format(my_greeting, my_name); print(my_output)"
```

It does basically the same thing, but with a few more variables and using the builtin method .format() for string types.

You can also execute the contents of a file using the python command. Try this by navigating the CMD to the working directory using "cd" (change directory) and "dir" (list directory) commands and then issuing the following command in CMD to compute a factorial:

```python
python3 test_prog.py 5
```

You can open the file with notepad to view the actual python code.

### Package Managers and Virtual Environments

The biggest benefit of python3, closely followed by the vast amounts of open source libraries and examples, is the package management system. Packages are third party software that holds the true power of python, if you want to run complex mathematical functions you would make life much easier by using numpy, which ships with low level binaries compiled from C and C++, making it hundreds of times faster than performing similar computations in pure python. It also ships with model fitting methods and is a dependency of virtually every scientific computing library in python, such as scikit-learn, scipy, tensorflow, and pandas.


This seems easy enough so far, surely every programming language has that, what makes this so special? The problem that arises with having hundreds of thousands of open source libraries is that sometimes decisions are made in early development that affects a projects ability to make updates later when certain dependencies change their function syntaxes. This doesn't happen very often, but when it does it's a life saver to know that you can have one python environment segregated from another and the changes you make to dependency versions wont affect the execution of programs executed from other virtual environments. Similar useful cases are when a dependency is being updated faster than the package is being maintained, so even though an updated dependency may work fine it may not have been tested and updated in the package version configs.


The official python package manager is the Python Package Index, PyPI, which is a remote repository of open source projects written in python and sometimes using high-speed compiled binaries as is the case for numpy, tensorflow and others. This uses a program called 'pip' to install and maintain packages installed from PyPI. Python doesn't alway come with pip installed, sometimes you have to download and run a small python script called get-pip.py, this can be found easily online. Your version of pip can be checked using the CMD command:

```Powershell
pip --version
```

If this throws an error, you'll need to download and run get-pip.py, if it returns a version below 18 you'll need to upgrade, which can be done using

```Powershell
pip install --upgrade pip
```

or if you know which version you want,

```Powershell
pip install --upgrade pip==X.Y
```

Before installing packages, we need to set up a Virtual Environment. This is really just a folder that separates your globally installed packages from your locally installed packages, and when you run python commands instead of searching the global packages location it first searches the location defined by the active virtual environment. This means that you can install specific versions of programs in one virtual environment without affecting the build of other virtual environments. Most of these venv-like programs work the same way, but one of the most common is called venv and comes with python.

You can create a venv called 'my_venv' by issuing the command in CMD:

```Powershell
python3 -m venv my_venv
```

which takes a few seconds. You can see the venv by then typing 'dir', you can see that the directory 'my_venv' is in that output list of directories, you can explore this if you like using 'cd' and 'dir'. You can create as many of these as you like, they will all run the python version you downloaded and the pip version you have by default. It's possible to change these venv to venv, but i'm not going to get into that. To activate your venv, simply make sure your CMD session is above where you created 'my_venv' (eg, 'my_venv' is shown when you type 'dir'), then type:

```Powershell
my_venv\Scripts\activate.bat
```

or in unix:

```bash
source ~/my_venv/bin/activate
```

Which sets your PATH to point to the python version specified in this venv as well as to the versions of packages that are installed by this venv. You can see all the different options that can be passed to the 'python' command by typing:

```Powershell
python3 -h
```

which lists all the possible arguments and what they mean, more information can be found online. You can experiment with using multiple venvs by creating two different venvs, in one of them install the latest version of some package such as:

```Powershell
env1\Scripts\activate.bat
pip install numpy
deactivate
env2\Scripts\activate.bat
pip install numpy==1.18
deactivate
```

then you can enter a python shell in each env by activating the env and typing 'python' in CMD and then execute the following:

```python
import numpy
print(numpy.__version__)
```

and you should see the version output to console. It may seem like this problem of version control wouldn't come up often, but when it does you'll be glad that you've properly prepared for it.

Virtual environments rely on environment variables, these are great for many things relating to a project as they're common for storing password, usernames, directory strings to important folders etc which are necessary to make a program run but for security and flexibility reasons would be a blunder to store hardcoded in the program. These are easily accessible/edited in python programs using the os.environ attribute. Note, the search path 'PATH' has its own attribute at sys.path.

There are a handful of package managers, one of the more popular is anaconda. Personally I avoid using anaconda distributions because my last experience a couple of years ago was of a deathly slow package manager and no end of problems with version control between the packages downloaded from pip (python package index, PyPI, note, NOT PyPy) and those downloaded from conda. The conda index is usually a few months behind the PyPI which can cause a lot of frustration and the virtual environments are less supported throughout other programs that rely on them, such as in linux supervisord and Celery i've seen threads of frustration over them not working as expected. That said, I do like the Spyder IDE they've produced, I think especially for a beginner or data scientist the variable explorer is worth more than any other IDE's benefits. Spyder3.3 was my preferred version as it works better for exploring custom objects than in Spyder4 even though Spyder4 is much faster, but Spyder3 support post-python3.6 outside of conda is bad, so it's a bit of a tradeoff of what you want - that's most of the reason as to why I still use python3.6.


### Interactive Development Environments - IDEs

An IDE is just a program that helps a developer write code, variable explorer, directory explorer, code completion, hints and syntax analysis etc are all nice little time savers, but the code itself doesn't require an IDE to run.

This part gets very opinionated, there are many IDEs to choose from for python, from Spyder, PyCharm, Atom, Jupyter Notebooks, and others.

For a beginner I think seeing the shape and effects of commands on data is very important, so I recommend Spyder very highly. Jupyter is good for docs but crap for day-to-day dev work. I only recently tried Atom but there are a lot of areas it just doesn't come even close to Spyder (though it's great for rust, javascript, html and loads of others, its a project to watch). PyCharm is one of the most popular, it has a "distribution" feel about it but looks more suited to deployment projects like web server backends over data science roles.

Spyder can be installed from pip into a specific venv same as any other package,

```Powershell
pip install spyder==3.3
OR
pip install spyder==4.*
```

I'm not sure how well Spyder3 will work on py38, there are so many improvements that make Spyder4 much better but i've got one project where I need the variable explorer to check things at the minute and it doesn't work the same in Spyder4 for exploring objects, once i've got that finished I'll probably migrate up a few versions. Spyder also has a very useful IPython console for manipulating data on the go.


### Code Structure

Reusable code is important, this [PEP style guide](https://www.python.org/dev/peps/pep-0008/) indicates how python code should look. There's something about lines not exceeding 130 characters, but there are millions of cases where this restriction is taken so literally that it makes the code difficult to read, I have a 27" monitor and have to read of a thin column at the edge of the screen which is infuriating, so I tend to just go with what I feel is most readable in these cases.

I'm not going to go on about package structure here, because there are dozens of examples and tutorials of that online and they're all the same. This closely relates to import statements, these are well defined but can appear erratic if you don't read about them first, and how they relate to \_\_init\_\_.py files. The first thing you should really get into the hang of is properly using import statements, and having a proper entry point to your code. eg, a directory structure like the following:

```script
my_proj/
 src/
  __init__.py
  utils.py
  models.py
  api.py
 main.py
 README.md
```

where main.py is the obvious entry point, and for some project to do with maps it may look like this:

```python
# main entry point for my_proj

from src.api import get_map, post_map, add_marker # line 1

if __name__ == "__main__": # line 2 - just python notation for "is this file being run as main"
  map_ = get_map()
  add_marker({'x': 73.193755, 'y': -3.51735})

```

when line 1 is executed, python navigates to the src directory and searches for an \_\_init\_\_.py file to execute, if one is found it executes it, this can be used to initialise anything for the direc, such as environment variables, locations in the PATH, whatever, it's just python code so it can do anything python does. After that, python goes to src/api.py and executes that within its own namespace, after it has run python searches that new namespace for the handles (get_map, post_map, add_marker) which can be functions names, class names, variables, anything. In this case they're probably functions because after line 2 get_map() is called and add_marker() is called.

Structuring code like this makes it much easier to refactor, maintain and deploy and is also required if you ever want to add anything to PyPI. That said, if you're working on something like a [kaggle](https://www.kaggle.com/) competition they usually make you use the Jupyter-style notebook for a submission, you can still split the parts of the module up into the file structure tree and import them but I think it's more common to see all the steps and definitions in the one document in a chronological order of use since it's basically a lesson and someone has to follow that and redeploy the data preprocessing and model inference to a production environment at some point.


### Alternative Python Interpreters/Compilers

The last thing I want to mention is the existence of alternative interpreters. Python is an interpreted language, and because of reasons i'm not going to go into it makes it relatively slow to execute, but if you're interested you can find a cool article [here](https://www.aosabook.org/en/500L/a-python-interpreter-written-in-python.html). The main interpreter is called CPython, because the user's code is written in python and the interpreter is written in C. This meant lots of devs spent time on alternative python implementations to speed it up. Using these often has intricate subtleties and limitations and can cause problems if you're not careful.

Probably the easiest one to get started with is PyPy which is a JIT compiled version of python code, similar to C-Sharp and Java, so called because the user's code is written in python and the initial compiler is also written in python. Don't confuse PyPy and PyPI, the former is software for compiling and executing python encoded text and the latter is the acronym for the python package index. It is mostly a drop-in replacement for the standard python interpreter but executes in as little as just 20% of the time. This is because before the program is executed a compiler written in python parses the code into an intermediary code doing most of the work before runtime, at runtime when all the states of the variables are known the compilation is completed and executed. This is called Just In Time compilation. Most python code executes faster using this but projects that make heavy use of C binaries do not and sometimes run slower. A more complete list of what class of problems benefit is available on the PyPy website.

Another interpreter is the Cython project, python with C data types. This is a very cool project to generate and compile super high speed C code from pure python code and can see programs execute in as little as 5% of the time of a standard pure-python interpreted program. But, there's some conditions. You can get good speed improvements out of the box, but to get the most you have to alter the python syntax which is not backwards compatible with the original python interpreter which is quite a big drawback.

There are many more such as IronPython (for C-Sharp compatibility), Jython (for Java compatibility), PythonNet (presumably for .NET, Windows native code), don't use stackless this is pretty much dead since the introduction of asyncio into the python standard library.


### Final Notes:

- python debugger, pdb, is super useful. if something throws an error and you can't figure out why, import pdb; pdb.pm() (pm for post-mortem) and you can explore the variable values from just before the error.
- In Spyder, go to preferences and set the variable explorer to show all variables, all caps all leading underscores and everything and you'll get a better sense as to what information the python interpreter has access to about each file by default.
- use numpy as much as you can for numerical-heavy modules, those C speed ups are massive, but don't switch back and forth because the python and numpy data types are slightly different and require "marshalling" between them which eats into any speed improvements.
- be explicit with file paths, use os.path.join(), os.path.split(), os.path.splitext() etc to keep programs cross-platform. To get the current fullfile of a file that python is currently executing you can use os.path.abspath(os.path.dirname(\_\_file\_\_)) which comes in very handy all the time when referencing resources.
- document your functions as per examples seen everywhere in large github projects, triple quotes are multiline strings and can be used to give lots of detail about the functions. You can add extra detail to functions by declaring the variable types and outputs with the notation:

```python
def test_func(a:int, b:str = None, c:datetime = None) -> float or None:
  """
  Function to do something
  Inputs:
    a: int, number of weeks until Xmas
    b: str, day of the week, if given
    c: datetime, my birthday
  Outputs:
    output: float or None, number of seconds until Xmas and birthday or something
  """
  output = None
  if b is not None and c is not None:
    # do something
    pass
  elif b is not None:
    # do something else
    pass
  else
    # do final possibility
    pass
  return output
```

BUT using this can cause issues with other python interpreters, because it's fairly new notation. It's for information only, there's no type checking at runtime or anything. It just helps in dialogue boxes if you can't remember what you're supposed to give a function, and pops up when you type:

```python
help(test_func)
```

into the python console.
