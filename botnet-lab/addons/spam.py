import os
import urllib2
# mail->http://pastebin.com/raw.php?i=qzCh8DCe-http://pastebin.com/raw.php?i=yCVQS3gx

def spam(to_url, msg_url):
    if os.name != "nt":
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
                SENDMAIL = "/usr/sbin/sendmail" # sendmail location
                FROM = "spam@example.com"
                TO = to_list
                SUBJECT = sub
                TEXT = msg
                # Prepare actual message
                message = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

                p = os.popen("%s -t -i" % SENDMAIL, "w")
                p.write(message)
                status = p.close()
                if status:
                    return "Sendmail exit status", status
            except:
                raise
                return "500 NOT OK"
