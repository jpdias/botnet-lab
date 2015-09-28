import time
import socket, os

def ParseUserCommands(irc, messageSender, messageChannel, messageSent):
	parseMessage = messageSent.split(" ")
	if len(parseMessage) > 1 and parseMessage[0] == (settings_commandprefix + "echo"):
		echoMessage = messageSent.split(" ", 1)[1]
		irc.send("PRIVMSG " + messageChannel + " :" + echoMessage + "\r\n")
		#print "--> PRIVMSG " + messageChannel + " :" + echoMessage

def connect(settings_server,settings_port,settings_botnick,settings_botpass,settings_channel,settings_owner):
	try:
		irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		irc.connect((settings_server, settings_port))
		irc.send("USER " + settings_botnick + " " + settings_botnick + " " + settings_botnick  + " :IRC " + settings_owner + "\r\n")
		irc.send("NICK " + settings_botnick + "\r\n")
		irc.send("PRIVMSG NickServ :identify " + settings_botpass + "\r\n")
		irc.send("JOIN " + settings_channel + "\r\n")
		#irc.send("PRIVMSG " + channel + " :Hi\r\n")
		return irc
	except:
		print "Fail to connect"
		time.sleep(100)
		connect(settings_server,settings_port,settings_botnick,settings_botpass,settings_channel,settings_owner)