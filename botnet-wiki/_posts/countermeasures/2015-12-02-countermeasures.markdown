---
layout: post
title:  "Botnet countermeasures"
excerpt:  "Main countermeasures against botnets."
date:   2015-12-03 10:00:00
categories: countermeasures
---

### Botnet countermeasures

Defense against botnets is carried out by application of certain strategies. All the Internet users are responsible for defense, starting from home or business computer users, system administrators, developers, up to web administrators and ISPs. The defense must be considered as a permanent and comprehensive process in which all the activities must be proactive. This is the only way to achieve good results and to protect computers, i.e. Web services/applications against the activities with bad intentions. 

**Countermeasures** against *botnet* can be broadly classified into two approaches: 

- Technical approaches

- Social and regulatory approaches

#### Technical Approach

Most of **botnet countermeasures** focus on the commandand-control infrastructure of botnets by *filtering botnet related traffic*, *sinkholing domains* with the assistance of DNS registrars or *obtaining the shutdown of malicious servers* in data centers. The *technical botnet defense approach* includes __*Blacklisting, Packet Filtering, Reverse Engineering and Port Blocking*__.

#### Blacklisting
A **blacklist** may provide single IP addresses of malicious hosts or whole subnets showing suspicious activities. A **blacklist** can be used to block all traffic from included addresses and also to filter websites with suspicious or proven malicious contents. 

**For example**, the *Spamhaus Project* provides various real-time lists that assist in identifying and blocking attempts by malicious activities. **Spamhaus Block List** (SBL) and the **Domain Block List** (DBL) contain a collection of IP addresses and domain names respectively from which incoming e-mail should not be accepted.

#### Packet Filtering
The **packet filtering** can be applied at a host, network and ISP level. A typical component that performs packet filtering at host level is a *desktop firewall*. Its purpose is to monitor the network activities of all active processes. As the amount of traffic at host level is usually manageable, deep-packet inspection is applicable. Often, user or administrator interaction is required to allow or deny network access for certain applications, if no suitable rules have been specified for them yet.

#### Reverse Engineering
Recovering the functionality of a program without the source code is known as **reverse engineering**. The malware reverse engineering technique helps in extracting the details of the installation and spreading of malware. The process involves static analysis and dynamic analysis. In case of static analysis, the binary is not executed. This phase deals with the reconstruction of certain aspects of the functionality. The dynamic analysis deals with the execution of the sample. The behavior of the malware can be determined by monitoring the host.

#### Port Blocking
**Port blocking** is a preventive measure that can be applied by ISPs to reducing the amount of spam mails traversing their network. The use of unauthenticated services via port 25, like direct mail exchange or open relay mail servers is almost exclusively for spam distribution purposes. Hence, blocking port 25 at ISP level has been recommended as best practice.
