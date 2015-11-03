
#mail->http://pastebin.com/raw.php?i=qzCh8DCe-http://pastebin.com/raw.php?i=yCVQS3gx
	
def sendmail(to, msg, sub):
	return True
	
def sendmail_web(to_url, msg_url):
	import urllib2
	to_data = urllib2.urlopen(to_url)
	msg_data = urllib2.urlopen(msg_url)
	to_list = []
	msg = ""
	for mail in to_data:
		to_list.append(mail)
	for txt in msg_data:
		if txt.find ( 'SUBJECT' ) != -1:
			sub = txt.split(":")[1]
		else:
			msg+=txt
	try:
		sendmail(to_list,msg,sub)
		return "200 OK"
	except:
		raise
		return "500 NOT OK"