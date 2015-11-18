from twisted.internet import defer
from twisted.mail import smtp, relaymanager
from twisted.internet import reactor
from cStringIO import StringIO


# mail->http://pastebin.com/raw.php?i=qzCh8DCe-http://pastebin.com/raw.php?i=yCVQS3gx

def spam(to_url, msg_url, sub):
    import urllib2
    to_data = urllib2.urlopen(to_url)
    msg_data = urllib2.urlopen(msg_url)
    to_list = []
    msg = ""
    for mail in to_data:
        to_list.append(mail)
    for txt in msg_data:
        if txt.find('SUBJECT') != -1:
            sub = txt.split(":")[1]
        else:
            msg += txt
        try:
            sendEmail('YOU@localhost', to_list, msg, sub)
            return "200 OK"
        except:
            raise
            return "500 NOT OK"


MXCALCULATOR = relaymanager.MXCalculator()


def getMailExchange(host):
    def cbMX(mxRecord):
        return str(mxRecord.name)

    return MXCALCULATOR.getMX(host).addCallback(cbMX)


def sendEmail(mailFrom, mailTo, msg, subject=""):
    def dosend(host):
        print "emailing %s (using host %s) from %s" % (mailTo, host, mailFrom)
        mstring = "From: %s\nTo: %s\nSubject: %s\n\n%s\n"
        msgfile = StringIO(mstring % (mailFrom, mailTo, subject, msg))
        d = defer.Deferred()
        factory = smtp.ESMTPSenderFactory(None, None, mailFrom, mailTo, msgfile, d,
                                          requireAuthentication=False,
                                          requireTransportSecurity=False)
        reactor.connectTCP(host, 25, factory)
        return d

    return getMailExchange(mailTo.split("@")[1]).addCallback(dosend)
