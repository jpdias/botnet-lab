# How to contribute

This is a community-driven project and we happily accept contributions from anyone interested in helping. To keep things well-organized and flowing smoothly, here are a few guidelines.

## Getting Started

### *Botnet Lab* setup

#### Dependencies

- [Python 2.7.x](https://www.python.org/downloads/)
- [pip 7.x.x]()
	- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
	- `python get-pip.py`
- [venv - Virtual Environments](https://docs.python.org/3/library/venv.html)
	- Windows: `pip install virtualenv`
	- Linux: `sudo pip install virtualenv`
- [git](https://git-scm.com/)
	- [Install instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
	
## Setup guide

Almost everyone of this steps are commands.

#### Cloning the repository

- `git clone https://github.com/jpdias/botnet-lab.git`
- `cd botnet-lab/botnet-lab`

#### Setting up the virtual environment

- `virtualenv venv`
- Starting the created virtual envoirnemnt
	- Linux: `. venv/bin/activate`
	- Windows: `venv\scripts\activate` 
	
### Installing project dependencies

- `pip install -r requirements.txt`
	 - This probably will fail at some point, because some of the used librarys are no longer supported or they stoped the development.

So, for each line of the requirements.txt do:

- `pip install <requirement>`

If some of this fails try:
- `sudo apt-get install python2.7-dev`
- `pip install <requirement> --allow-external <requirement> --allow-unverified <requirement>`
	
If it fails to the best workaround is to search for a valid package. For example the dependency `pygame==1.9.2a0` will fail to install. 

**Linux**

In Linux there is no generic way of installing all the missing packages. For that we will go throught everyone that may cause problems and present a workaround.

- *pygame*:
For installing `pygame` you can use the shell script below.
Remember to do this with the `venv` activated.

```
#!/bin/sh
BASE_PATH=`pwd`
sudo apt-get build-dep python-pygame
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libv4l-dev
cd /usr/include/linux
sudo ln -s ../libv4l1-videodev.h videodev.h
cd $BASE_PATH
wget http://www.pygame.org/ftp/pygame-1.9.1release.tar.gz
tar -xzf pygame-1.9.1release.tar.gz
cd pygame-1.9.1release
python config.py
sudo python setup.py install
cd $BASE_PATH
rm pygame-1.9.1release.tar.gz
sudo rm -rf pygame-1.9.1release
ln -s /usr/local/lib/python2.7/dist-packages/pygame venv/lib/python2.7/site-packages/pygame
```

- *python-xlib*: `sudo pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/`
	- You can have to install svn  with `sudo apt-get install svn`
		
- *autopy*: `sudo apt-get install libxtst-dev`

Some of the libraries like `pyHook` and `pypiwin32` are Windows-only dependencies, so if you are on a Linux machine don't worry about them.

## GitHub

You need a [GitHub](https://github.com) account for most everything like opening or commenting on issues, or submitting code patches (the GitHub parlance here is "pull request").

## Bug reporting

Yes, we have some bugs. Some of them we know about (and are working on), others we need somebody to tell us about. If you submit a bug report (issue), please be sure to include the actual program output and let us know anything relevant about the environment (OS and Python version, for example, or if you have made any changes to the code).

## Pull requests

The easiest and best way to do this is to [fork our repository](https://help.github.com/articles/fork-a-repo) and then [send a pull request](https://help.github.com/articles/using-pull-requests). In your description, please be sure to note any related issues (for example, if your PR fixes a previously-reported bug or implements an existing enhancement request).

We will review and possibly request additional changes before merging. The best patches will be those that conform to [PEP8](http://legacy.python.org/dev/peps/pep-0008/) and refrain from introducing new dependencies as much as possible. Sometimes that will be okay, of course, if it does something new and awesome! Also please keep in mind that Utility Belt is released under the [MIT license](LICENSE) and this will include all code sent back to us.

__Note:__ _This CONTRIBUTING.md was shamelessly ripped off of [technoskald's](https://github.com/technoskald) epic [Maltrieve project](https://github.com/technoskald/maltrieve)._
