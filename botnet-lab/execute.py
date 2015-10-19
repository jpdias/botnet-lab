def ExecCmd(cmd):
	try :
		output =  subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0]
		irc.send ( 'PRIVMSG ' + messageChannel + ' :'+ output.replace("\r"," - ").replace("\n"," - ") +'\r\n' )
	except :
		output = "FAILED"
		irc.send ( 'PRIVMSG ' + messageChannel + ' :'+ output +'\r\n' )