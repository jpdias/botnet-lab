---
layout: post
title:  "Types of Bots"
date:   2015-01-29 21:21:50
categories: anatomy
---

During our research, we found many different types of bots. Here we present some of the more widespread and well-known bots. We introduce the basic concepts of each piece of malware and furthermore describe some of the features in more detail. In addition, we show several examples of source code from bots and list parts of their command set.

![Botnet Ilustration]({{ site.url }}/assets/botnet.png)

* **Agobot (parent of Phatbot/Forbot/XtremBot)**

	This is probably the best known bot. There are more than 500 known different versions of Agobot and this number is increasing. The bot itself is written in C++ with cross-platform capabilities and the source code is put under the GPL.
	The latest available versions of Agobot are written in tidy C++ and show a really high abstract design. The bot is structured in a very modular way, and it is very easy to add commands or scanners for other vulnerabilities. Agobot uses libpcap (a packet sniffing library) and Perl Compatible Regular Expressions (PCRE) to sniff and sort traffic. Agobot can use NTFS Alternate Data Stream (ADS) and offers Rootkit capabilities like file and process hiding to hide its own presence on a compromised host.
	Furthermore, reverse engineering this malware is harder since it includes functions to detect debuggers (e.g. SoftICE and OllyDbg) and virtual machines (e.g. VMWare and Virtual PC). In addition, Agobot is the only bot that utilized a control protocol other than IRC. Furthermore, the Linux version is able to detect the Linux distribution used on the compromised host and sets up a correct init script.

* **SDBot (parent of RBot/UrBot/UrXBot/etc.)**

	This family of malware is at the moment the most active one. SDBot is written in very poor C and also published under the GPL. It is the father of RBot, RxBot, UrBot, UrXBot, JrBot,.. and probably many more. The source code of this bot is not very well designed or written. Nevertheless, attackers like it, and it is very often used in the wild. It offers similar features to Agobot, although the command set is not as large, nor the implementation as sophisticated.

* **mIRC-based Bots - GT-Bots**
	
	We subsume all mIRC-based bots as GT-bots[1], since there are so many different versions of them that it is hard to get an overview of all forks. mIRC itself is a popular IRC client for Windows. GT is an abbreviation for Global Threat and this is the common name used for all mIRC-scripted bots. These bots launch an instance of the mIRC chat-client with a set of scripts and other binaries. One binary you will never miss is a HideWindow executable used to make the mIRC instance unseen by the user. The other binaries are mainly Dynamic Link Libraries (DLLs) linked to mIRC that add some new features the mIRC scripts can use. The mIRC-scripts, often having the extension ".mrc", are used to control the bot. They can access the scanners in the DLLs and take care of further spreading. GT-Bots spread by exploiting weaknesses on remote computers and uploading themselves to compromised hosts.

	*Reference*: [GT-Bot Definition](http://www.nohack.net/gtbot-removal)[1]

These three last examples of bots are probably the most common ones, in terms of usage and also que more capable ones as for their features and implementation. There are however other types of bots which given their very interesting features are worthy of mentioning in this topic.

* **DSNX Bots**
	
	The Dataspy Network X (DSNX) bot is written in C++ and has a convenient plugin interface. An attacker can easily write scanners and spreaders as plugins and extend the bot's features. Again, the code is published under the GPL. This bot has one major disadvantage: the default version does not come with any spreaders. But plugins are available to overcome this gap. Furthermore, plugins that offer services like DDoS-attacks, portscan-interface or hidden HTTP-server are available.

* **Q8 Bots**

	Q8bot is a very small bot, consisting of only 926 lines of C-code. And it has one additional noteworthiness: It's written for Unix/Linux systems. It implements all common features of a bot: Dynamic updating via HTTP-downloads, various DDoS-attacks (e.g. SYN-flood and UDP-flood), execution of arbitrary commands, and many more. In the version we have captured, spreaders are missing. But presumably versions of this bot exist which also include spreaders.

* **kaiten**

	This bot lacks a spreader too, and is also written for Unix/Linux systems. The weak user authentication makes it very easy to hijack a botnet running with kaiten. The bot itself consists of just one file. Thus it is very easy to fetch the source code using wget, and compile it on a vulnerable box using a script. Kaiten offers an easy remote shell, so checking for further vulnerabilities to gain privileged access can be done via IRC.

* **Perl-based bots**

	There are many different version of very simple based on the programming language Perl. These bots are very small and contain in most cases only a few hundred lines of code. They offer only a rudimentary set of commands (most often DDoS-attacks) and are used on Unix-based systems.
	
	![Swiss Army Knife]({{ site.url }}/assets/swiss-army-knife.png)

> *A botnet is the equivalente of an army of swiss army knives... But for malware.*
> – a student of SSIN @ FEUP