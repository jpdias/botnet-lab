---
layout: post
title:  "Botnet Lab Architecture"
date:   2015-10-19 17:21:50
categories: laboratory
excerpt: Architecture and structure of the botnet laboratory.
---

##Summary

The botnet built using this laboratory will match the general architecture for any botnet based on a Command-and-Control (C&C) architecture.
Our actor is the *Bot Herder* or *Bot Master*, it operates using the a special IRC client (that is part of this laboratory), connects to a IRC-Server (in this case a IRCD-Hybrid based one) where all the bots are connected.

Whenever the *Bot Herder* sends a message to the IRC Server it broadcast it to all the connected bots that executes the requested job.

Special cases are the Spam request and the Screenshot/Webcam request. 
In the first case, the Spam, to avoid the trouble of setting up a SMTP server on all the bots we use the [Mandrill API](https://www.mandrill.com/) for sending the e-mail. While this can appear strange, 
because of centralizing all the traffic on one e-mail sender API with low free quotas and with the risk of the account being blocked, we send the API Key in the request sended to bots in a way that if a Key it's blocked we can simple send a different API Key on the request sended to the bots. 
Additionally it's used the [PasteBin Service](http://pastebin.com/) and it's "anonymous and hidden file" hability for hosting relevant data like the the *e-mail sending list*, *API Key* and *Message* and the *Bot Herder* just needs to send to the bots the files URL. 

In the second case, the Screenshot/Webcam, the bots uses the [Imgur API](https://api.imgur.com/) for storage the images and just send the URL of that images back to the *Bot Herder*.

Also, it's used RSA encryption so the *Bot Herder* it's the only one capable of decrypt the messages sended by the bots because it's the *Private Key* owner. The bots encrypts the messages using the *Public Key* defined by the *Bot Herder*.

##Network Diagram

![Network Diagram]({{ site.url }}/diagrams/network_diagram.png)

##Message Exchange Diagram

![Sequencial Diagram]({{ site.url }}/diagrams/sequencial_diagram.png)

##Message Exchange Diagram on Spam Request

![Sequencial Diagram]({{ site.url }}/diagrams/sequencial_spam_diagram.png)

##Message Exchange Diagram on Webcam or Screenlogger Request

![Sequencial Diagram]({{ site.url }}/diagrams/sequencial_spam_diagram.png)