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

- *win32api - pywin32* 
	- `pip install pypiwin32`

**Linux**

In Linux there is no generic way of installing all the missing packages. For that we will go throught everyone that may cause problems and present a workaround.

- *pygame*:
For installing `pygame` you can use the shell script below.
Remember to do this with the `venv` activated.

{% highlight bash %}
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
{% endhighlight %}

- *python-xlib*: `sudo pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/`
	- You can have to install svn  with `sudo apt-get install svn`
		
- *autopy*: `sudo apt-get install libxtst-dev`

Some of the libraries like `pyHook` and `pypiwin32` are Windows-only dependencies, so if you are on a Linux machine don't worry about them.