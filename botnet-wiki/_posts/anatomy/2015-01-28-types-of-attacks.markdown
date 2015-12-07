---
layout: post
title:  "Types of Attacks"
date:   2015-01-28 10:21:50
categories: anatomy
excerpt: A botnet is nothing more than a tool, there are as many different motives for using.
---

A botnet is nothing more than a tool, there are as many different motives for using. The most common uses are criminally motivated or for destructive purposes. The possibilities to use botnets can be categorized as listed below. And since `a botnet is nothing more than a tool`, there are most likely other potential uses that we have not listed.

> *A botnet is comparable to compulsory military service for windows boxes*
> – Stromberg

1.	**Distributed Denial-of-Service Attacks** 

	Often botnets are used for Distributed Denial-of-Service (DDoS`[1]`) attacks. A DDoS attack is an attack on a computer system or network that causes a loss of service to users, typically the loss of network connectivity and services by consuming the bandwidth of the victim network or overloading the computational resources of the victim system. In addition, the resources on the path are exhausted if the DDoS-attack causes many packets per second (pps). Most commonly implemented and also very often used are TCP SYN and UDP flood attacks. 
	
	![Attack Type DDoS Diagram]({{ site.url }}/assets/ddos.png)
	
	Note that DDoS attacks are not limited to web servers, virtually any service available on the Internet can be the target of such an attack. Higher-level protocols can be used to increase the load even more effectively by using very specific attacks, such as running exhausting search queries on bulletin boards or recursive HTTP-floods on the victim's website. Recursive HTTP-flood means that the bots start from a given HTTP link and then follows all links on the provided website in a recursive way. This is also called spidering.
	
	*Reference*: [Wiki: DDoS](http://en.wikipedia.org/wiki/Ddos)[1]

2.	**Spamming**

	Some bots offer the possibility to open a SOCKS v4/v5 proxy - a generic proxy protocol for TCP/IP-based networking applications (RFC 1928`[2]`) - on a compromised machine. After having enabled the SOCKS proxy, this machine can then be used for nefarious tasks such as spamming. With the help of a botnet and thousands of bots, an attacker is able to send massive amounts of bulk email (spam). Some bots also implement a special function to harvest email-addresses. Often that spam you are receiving was sent from, or proxied through, old Windows computers sitting at home. In addition, this can, of course, also be used to send phishing-mails since phishing is a special case of spam.
	
	*Reference*: [RFC 1928](http://rfc.net/rfc1928.html)[2]

3.	**Sniffing Traffic**

	Bots can also use a packet sniffer to watch for interesting clear-text data passing by a compromised machine. The sniffers are mostly used to retrieve sensitive information like usernames and passwords. But the sniffed data can also contain other interesting information. If a machine is compromised more than once and also a member of more than one botnet, the packet sniffing allows to gather the key information of the other botnet.
	Thus it is possible to "steal" another botnet.

4.	**Keylogging**

	If the compromised machine uses encrypted communication channels (e.g. HTTPS or POP3S), then just sniffing the network packets on the victim's computer is useless since the appropriate key to decrypt the packets is missing. But most bots also offer features to help in this situation. With the help of a keylogger it is very easy for an attacker to retrieve sensitive information. An implemented filtering mechanism (e.g. "I am only interested in key sequences near the keyword 'paypal.com'") further helps in stealing secret data. And if you imagine that this keylogger runs on thousands of compromised machines in parallel you can imagine how quickly PayPal accounts are harvested.
	
	![Keylogger]({{ site.url }}/assets/keylogger.png)

5.	**Spreading new malware**

	In most cases, botnets are used to spread new bots. This is very easy since all bots implement mechanisms to download and execute a file via HTTP or FTP. But spreading an email virus using a botnet is a very nice idea too. A botnet with 10.000 hosts which acts as the start base for the mail virus allows very fast spreading and thus causes more harm. The Witty worm, which attacked the ICQ protocol parsing implementation in Internet Security Systems (ISS) products is suspected to have been initially launched by a botnet due to the fact that the attacking hosts were not running any ISS services.

6.	**Installing Advertisement Addons and Browser Helper Objects (BHOs`[3]`)**

	Botnets can also be used to gain financial advantages. This works by setting up a fake website with some advertisements: The operator of this website negotiates a deal with some hosting companies that pay for clicks on ads. With the help of a botnet, these clicks can be "automated" so that instantly a few thousand bots click on the pop-ups. This process can be further enhanced if the bot hijacks the start-page of a compromised machine so that the "clicks" are executed each time the victim uses the browser.
	
	*Reference*: [BHO](http://msdn.microsoft.com/library/en-us/dnwebgen/html/bho.asp)[3]
	
7.	**Google AdSense abuse**
	
	A similar abuse is also possible with Google's AdSense`[4]` program: AdSense offers companies the possibility to display Google advertisements on their own website and earn money this way. The company earns money due to clicks on these ads, for example per 10.000 clicks in one month. An attacker can abuse this program by leveraging his botnet to click on these advertisements in an automated fashion and thus artificially increments the click counter. This kind of usage for botnets is relatively uncommon, but not a bad idea from an attacker's perspective.
	
	*Reference*: [AdSense](https://www.google.com/adsense/)[4]

8.	**Attacking IRC Chat Networks**
	
	Botnets are also used for attacks against Internet Relay Chat (IRC) networks. Popular among attackers is especially the so called "clone attack": In this kind of attack, the controller orders each bot to connect a large number of clones to the victim IRC network. The victim is flooded by service request from thousands of bots or thousands of channel-joins by these cloned bots. In this way, the victim IRC network is brought down - similar to a DDoS attack.

9.	**Manipulating online polls/games**
	
	Online polls/games are getting more and more attention and it is rather easy to manipulate them with botnets. Since every bot has a distinct IP address, every vote will have the same credibility as a vote cast by a real person. Online games can be manipulated in a similar way.

10.	**Mass identity theft**

	Often the combination of different functionality described above can be used for large scale identity theft, one of the fastest growing crimes on the Internet. Bogus emails ("phishing mails") that pretend to be legitimate (such as fake PayPal or banking emails) ask their intended victims to go online and submit their private information. These fake emails are generated and sent by bots via their spamming mechanism. These same bots can also host multiple fake websites pretending to be Ebay, PayPal, or a bank, and harvest personal information. Just as quickly as one of these fake sites is shut down, another one can pop up. In addition, keylogging and sniffing of traffic can also be used for identity theft.

This list demonstrates that attackers can cause a great deal of harm or criminal activity with the help of botnets. Many of these attacks – especially DDoS attacks - pose severe threats to other systems and are hard to prevent. In addition, we are sure there are many other uses we have not covered in this list.


