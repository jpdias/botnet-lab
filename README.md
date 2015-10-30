# Botnets

A botnet laboratory for learning and testing proposes.

# ToDo List

## Coding

 - IRC or other server for Command and Control (plus geolocation/timezone)
 	 - Control one-by-one or all at once
 - Simple bot framework with already built-in add-ons:
 	 - Keylogger/Screenlogger funcionalities
	 - Webcam capture funcionalities
	 - Spam / DDoS / Private data scrapping
 - Encrypt all traffic between C&C and Bots
 - Explore a pre-known exploit as a way of propagation (in some old software or tool for example)
 - Camouflage: make the bot run as a part of something that usually runs on the system
 - Code Obfuscation
 - Bot self-propagation (Point-Of-Distribution - Worm)

### Possible Coding ToDo
 
 - Functionality bots to securely update the bot code.
 - Multiple Control points 
 - Detect Virtualization
 - Self Morphing (Change the bot hash over time)
 - Auto-destructive bot
 
## Educational ToDo
 
 - Website/Wiki with information and labs about botnets:
 	- Botnet concepts and structures
 	- Detailed how-to setup a botnet lab for testing proposals and to use the built tool
	- Good uses of botnets
	- History and impact of botnet
	- Preventing and dectecting
	- Operations and task-forces dedicated to botnets
	
#Working with [venv](https://docs.python.org/3/library/venv.html)

```
$ pip install virtualenv
$ cd my_project_folder
```

###Windows Activate

```
./venv/Scripts/activate
```

###Linux Activate

```
./venv/bin/activate
```

###Install dependencies

```
pip install -r requirements.txt
```

Install manual dependencies

```
pip install dep/dep.whl
```

In venv mode afer add a new dependency  please do 
```
pip freeze > requirements.txt
```


