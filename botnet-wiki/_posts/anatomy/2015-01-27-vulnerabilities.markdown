---
layout: post
title:  "Vulnerabilities"
date:   2015-01-27 21:21:50
categories: anatomy
---


In computer security, a vulnerability is defined as: a weakness that allows an attacker to reduce a system's information assurance. 

Vulnerability is a intersection of three elements: **a system susceptibility or flaw**, attacker **access to the flaw**, and attacker capability to **exploit the flaw**.

![Vulnerability]({{ site.url }}/assets/vulnerability.png)

Due to their immense size - botnets can consist of several ten thousand compromised machines - botnets pose serious threats. Distributed denial-of-service (DDoS) attacks are one such threat. Even a relatively small botnet with only 1000 bots can cause a great deal of damage. These 1000 bots have a combined bandwidth (1000 home PCs with an average upstream of 128KBit/s can offer more than 100MBit/s) that is probably higher than the Internet connection of most corporate systems. In addition, the IP distribution of the bots makes ingress filter construction, maintenance, and deployment difficult. In addition, incident response is hampered by the large number of separate organizations involved. 

Another use for botnets is stealing sensitive information or identity theft: Searching some thousands home PCs for password.txt, or sniffing their traffic, can be effective.
The spreading mechanisms used by bots is a leading cause for "background noise" on the Internet, especially on TCP ports 445 and 135. In this context, the term spreading describes the propagation methods used by the bots. These malware scan large network ranges for new vulnerable computers and infect them, thus acting similar to a worm or virus.


**Vulnerability-specific ports:**

* 42 - WINS (Host Name Server)
* 80 - www (vulnerabilities in Internet Information Server 4 / 5 or Apache)
* 903 - NetDevil Backdoor
* 1025 - Microsoft Remote Procedure Call (RPC) service and Windows Messenger port
* 1433 - ms-sql-s (Microsoft-SQL-Server)
* 2745 - backdoor of Bagle worm (mass-mailing worm)
* 3127 - backdoor of MyDoom worm (mass-mailing worm)
* 3306 - MySQL UDF Weakness
* 3410 - vulnerability in Optix Pro remote access trojan (Optix Backdoor)
* 5000 - upnp (Universal Plug and Play: MS01-059 - Unchecked Buffer in Universal Plug and Play can Lead to System Compromise)
* 6129 - dameware (Dameware Remote Admin - DameWare Mini Remote Control Client Agent Service Pre-Authentication Buffer Overflow Vulnerability)


**The vulnerabilities behind some of these exploits can be found with the help of a search on Microsoft's Security bulletins (sample):**

* MS03-007 Unchecked Buffer In Windows Component Could Cause Server Compromise
* MS03-026 Buffer Overrun In RPC Interface Could Allow Code Execution
* MS04-011 Security Update for Microsoft Windows
* MS04-045 Vulnerability in WINS Could Allow Remote Code Execution
