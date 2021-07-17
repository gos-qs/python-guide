
## Apple M1 chipset, python installation for ARM and for X86

Programs compiled for Apple X86 chipsets will only work on Apple M1 chipsets if they are:

- not too complicated
- run using the Rosetta2 machine code translator tool.

Though complex programs may still not work through Rosetta2, such as VMWare and Tensorflow.

The unofficial package manager for MacOS Homebrew is now fully supported for Apple M1 chipsets, but be aware many packages hosted aren't but will usually run through Rosetta2. Python3 for Apple M1 chipsets can be installed using Homebrew in the normal way as described in [python-installation](python-installation.md).

Many python packages on the Python Package Index  aren't yet ported to the M1 chipset, so the only way to run these is by running a python environment through Rosetta2 and installing the X86 versions of these packages. After giving this some thought I decided that I didn't want 2 versions of Homebrew on my system, one for M1 and one for X86, this seemed like it would become horribly messy. So instead I decided to have the M1 Homebrew and manually download and install the X86 python3 versions I need.

First, we need to set up a version of the 'Terminal' application which identifies itself as X86 and uses Rosetta2 by default. This is described in a lot of places such as in [this guide](https://medium.com/swlh/run-x86-terminal-apps-like-homebrew-on-your-new-m1-mac-73bdc9b0f343), essentially you're simply duplicating the 'Terminal' application, renaming as something like 'Terminal-Rosetta' and then in the 'Get Info' option for 'Terminal-Rosetta' you check the 'Open using Rosetta' checkbox and you're good to go. For good measure I also added both the Terminal and Terminal-Rosetta to my shortcut bar. When I set this up it required a little bit of juggling of permissions using chmod in order to rename the duplicated application but it wasn't anything too difficult. You can test the chipset type in either terminal version using the command:

```bash
uname -m
# returns 'arm64' in regular Terminal, and 'x86_64' when running through Rosetta
```

Once at this point, you're ready to install your X86 version of python3.

To do this, simply go to the [downloads](https://www.python.org/downloads/mac-osx/) section of the python.org website and download the version of the X86 MacOS that you want. I'm going to download and install the Python3.6 version for demonstration purposes. I'm going to install using the X86 universal installer in the .pkg format.

In order to ensure that the Rosetta translator is used, we'll install this .pkg file using the 'Terminal-Rosetta' application that we created in the previous step. Open 'Terminal-Rosetta' and check that it identifies as X86 as expected by issuing the 'uname -m' command. Then change directory to your Downloads folder and install the python .pkg file such as:

```bash
sudo installer -pkg python-3.6.8-macosx10.9.pkg -target /Applications/
```

Which installs the package to the global (root) Applications directory and installs the python interpreter in /Library/Frameworks/Python.framework/Versions. This new directory is just a few fancy wrappers, config files and a symlink which points to the actual python interpreter installed usually in '/Library/Frameworks/'. The fullfile of my python installation is /Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python. sudo seems to be required here to a) install something to the global applications directory and b) install the python interpreter into /Library/Frameworks. I prefer to have my path names without spaces using underscores or hyphens where necessary, so I rename my install to 'Python3.6' using the command 'mv "Python 3.6" "Python3.6"'. Inside the 'Python3.6' directory there should be an object called 'IDLE.app', nested inside this is a simlink to the python interpreter, you can find the path for this by using the 'find' command, such as:

```bash
cd /Applications/Python3.6
find ./ -name 'Python'
```

Which returns the path to the symlink, something like this: './IDLE.app/Contents/MacOS/Python'. If you execute that symlink in your shell:

```bash
./IDLE.app/Contents/MacOS/Python
```

Then you should enter a python interpreter shell. We're nearly there! Now we just need to circle back to the magic of venv to control which python interpreter we want to use at any given time. Version control can get complicated on just multiple environments on intel-X86 only machines, but now we're dealing with version control for X86 as well as M1-ARM so good practices are of great importance.

The new virtual environment can be created using the following command, still in 'Terminal-Rosetta':

```bash
# path/to/your/new/python/installation -m venv path/to/your/new/venv
/Library/Frameworks/Python.framework/Versions/3.6/Resources/Python.app/Contents/MacOS/Python -m venv py36_x86
```

And voila, you can use this new virtual environment the same as any other, by running:

```bash
source py36_x86/bin/activate
```

Which will point to your X86 installation of python3.X as well as the X86 installation of pip3 for this python3 installation, and maintain the path to valid package installs. Activate the venv and go ahead and try it by installing numpy, if you look at the download status messages you can see it fetches the X86 builds and installs them, and as long as you're using the 'Terminal-Rosetta' application to activate the venv and use the packages you should be fine. I like to use Spyder as my IDE, and I've not had any issues yet using this method to install as at the tie of writing I don't think they have an M1 build yet since it relies on so many external GUI libraries.

Don't forget, make sure you have the correct terminal open when using the virtual envs. I've accidentally installed things to an X86 environment from the ARM terminal, it was solved by a simple 'pip uninstall <package>'' but there might be complex packages which wouldn't be such an easy blunder to fix.

Closing notes, this Rosetta X86 emulation will work for most packages. The only package I've found to not work so far is Tensorflow, it won't even import it'll just crash the kernel every time. For projects where you need to have Tensorflow working as well as packages which don't have an M1 build, I'm not sure of a solution.

Tensorflow-GPU can be enabled on the M1 by installing using mini-conda and the tensorflow-macos github repository, following the instructions in issue [#153](https://github.com/apple/tensorflow_macos/issues/153). You can confirm that your machine is using the GPU during training by monitoring the Activity Monitor whilst training a simple test script such as from
[this question/answer](https://stackoverflow.com/questions/67352841/tensorflow-is-not-using-my-m1-macbook-gpu-during-training/67953428#67953428).
