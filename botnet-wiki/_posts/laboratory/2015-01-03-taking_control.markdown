---
layout: post
title:  "Build and Distribute"
date:   2015-10-01 17:21:50
categories: laboratory
excerpt: Adding the bot to startup and generation executables.
---

## Linux

For adding the bot to the startup you can use this script: [add_to_startup.sh]({{ site.url }}/resources/add_to_startup.sh)

- Do not forget to give execute permissions: `chmod +x add_to_startup.sh`

## Windows 

Setting up an executable package on Windows.

1. Download [py2exe](http://sourceforge.net/projects/py2exe/files/latest/download?source=files)
	- Install it with virtualenv activated with: `pip install <path_to_download>/py2exe.exe`
	
2. Make the build script.
{% highlight python %}
from distutils.core import setup
import py2exe

setup(console=['bot.py'])
{% endhighlight %}

3. Make the build: `python setup.py install`
	- Expect to see lots and lots of output.

4. Move the folder key with the public key only inside and place it side by side with the executable.
	- Inside the created folder `/dist/`

5. Test your executable
	- Now that the package has been created it is ready to test: 

Source: [http://py2exe.org/index.cgi/Tutorial](http://py2exe.org/index.cgi/Tutorial)

**Additionally** if you want to create an installer and add to startup option you can use [NSIS (Nullsoft Scriptable Install System)](nsis.sourceforge.net/Main_Page).
