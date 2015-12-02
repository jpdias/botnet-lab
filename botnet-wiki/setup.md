---
layout: page
title: Setup
permalink: /setup/
---

#*Botnet Lab* setup

##Minimal requirements

###Operative System

Any Windows or Linux system will be capable of building and running the project.

###Dependencies

- [Python 2.7.x](https://www.python.org/downloads/)
- [pip 7.x.x]()
	- Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)
	- `python get-pip.py`
- [venv - Virtual Environments](https://docs.python.org/3/library/venv.html)
	- Windows: `pip install virtualenv`
	- Linux: `sudo pip install virtualenv`
- [git](https://git-scm.com/)
	- [Install instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
	
##Setup guide

Almost everyone of this steps are commands.

###Cloning the repository

- `git clone https://github.com/jpdias/botnet-lab.git`
- `cd botnet-lab/botnet-lab`

###Setting up the virtual environment

- `virtualenv venv`
- Starting the created virtual envoirnemnt
	- Linux: `. venv/bin/activate`
	- Windows: `venv\scripts\activate` 
	
###Installing project dependencies

- `pip install -r requirements.txt`
	 - This probably will fail at some point, because some of the used librarys are no longer supported or they stoped the development.

So, for each line of the requirements.txt do:

- `pip install <requirement>`

If some of this fails try:
- `sudo apt-get install python2.7-dev`
- `pip install <requirement> --allow-external <requirement> --allow-unverified <requirement>`
	
If it fails to the best workaround is to search for a valid package. For example the dependency `pygame==1.9.2a0` will fail to install. 

**Windows**

To make it install on Windows simple go to the [Unofficial Windows Binaries for Python Extension Packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/) from the [Univeristy of California](http://www.uci.edu/) and use the respective wheel.
For example wiht `pygame==1.9.2a0` for Windows 64bit:
- `pip install <path_to_download_folder>/pygame‑1.9.2a0‑cp33‑none‑win_amd64.whl`

**Linux**

In Linux there is no generic way of installing all the missing packages. For that we will go throught everyone that may cause problems and present a workaround.

- *pygame*:
For installing `pygame` you can use this shell script: [install_pygame.sh](https://gist.github.com/brousch/6395214#file-install_pygame-sh).
Remember to do this with the `venv` activated.

- *python-xlib*: `sudo pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/`
	- You can have to install svn  with `sudo apt-get install svn`
		
- *autopy*: `sudo apt-get install libxtst-dev`

Some of the libraries like `pyHook` and `pypiwin32` are Windows-only dependencies, so if you are on a Linux machine don't worry about them.