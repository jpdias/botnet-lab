#!/bin/sh
sudo apt-get install git
sudo apt-get install python2.7 python-dev build-essential 
sudo apt-get install python-pip
pip install virtualenv
git clone https://github.com/jpdias/botnet-lab.git
cd botnet-lab/botnet-lab/
virtualenv venv
. venv/bin/activate
BASE_PATH=`pwd`
pip install pycrypto
pip install requests
sudo apt-get install libxtst-dev
pip install autopy
sudo apt-get install svn
pip install svn+https://svn.code.sf.net/p/python-xlib/code/trunk/
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
