---
layout: post
title:  "Botnet countermeasures"
excerpt:  "Main defenses and countermeasures agains botnets"
date:   2015-12-03 10:00:00
categories: countermeasures
---


Botnet Detection
===================


**Botnet detection** deals with the identification of bots in the machine or network so that some sort of remedy can be done. 

In recent years *botnet detection* has been a hot topic in the research community due to increase in the malicious activity. According to the majority of the common characteristic of a **bot malwareare related to network activities** since the bots require some sort of *interaction with the command and control servers*. Some of the *common activities* one could monitor to detect botnets are:
> -  *opening of specific ports*
> -  *establishing a number of unwanted network connections*
> -  *downloading and executing files and programs*
> -  *creating new processes with well-known names*
> -  *disabling antivirus software*

### Detection techniques
**Intrusion Detection System** (IDS) is an approach for *botnet detection* that can be either a **signature** or **anomaly-based** technique. 
#### Signature-Based
A **signature-based** *Botnet detection* technique uses the signatures of current *Botnets* for its detection. This method has several advantages, such as very low false alarm rate, immediate detection, easier to implement and there is better information about the type of detected attack. **Signature based** detection method can only able to detect well known botnets. 

Thus, unknown Botnets can’t be detected by this method. **Anomaly-based** detection techniques are introduced to
overcome this drawback.

#### Anomaly-Based
The idea behind **anomaly-based** detection approach is to perform botnet detection by considering several different network traffic anomalies, including *high network latency*, *high traffic volume*, *traffic on unusual ports*, and *unusual system behavior* that could indicate the presence of malicious bots in the network. 

**Anomaly-based** detection techniques are further divided into **host-based detection** and **network-based detection**.

A **host-based technique** is a detection strategy which *monitors* and *analyzes* the internals of a computer system *instead of network traffics* on its external interfaces. In this approach the individual machine is monitored to find any suspicious behavior, including its *processing overhead*, and *access to suspicious files*. If suspicious activity is detected the *Host Intrusion Detection Systems* will alert the user or administrator. It takes a snapshot of existing system files and matches it to the previous snapshot. If the critical system files were modified or deleted, an alert is sent to the administrator to investigate.

A **network-based technique** is a detection strategy which tries to detect Botnets by monitoring network traffics. Network-based techniques can be classified into two categories: 
> -  **Active monitoring** -- based on the ability to inject test packets into the network, servers or application for measuring the reactions of network. Hence, it can produce extra traffics on the network. The injected packets can determine whether a human or bot is managing that session. It works in a cause-effect correlation because for a large portion of Botnet command-and-control channels, a command-and-control interaction has a deterministic command response pattern. This technique shows effectiveness on real-world IRC-based Botnet detection.

> -  **Passive monitoring** -- observe data traffic in the network and look for suspicious communications that may be provided by bots or command-and-control servers. It does not increase the traffics on the network for inspection.

To access the command-and-control server, bots perform DNS queries to locate the particular server that a DDNS (Dynamic DNS) provider typically hosts. It is thus possible to create a detection mechanism that monitors DNS traffic and searches for some DNS anomalies. Botnets frequently use DNS to rally infected hosts, launch attacks and update their codes.

List of tool to detect botnets....


### Botnet countermeasures

Defense against Bots and Botnets is carried out by application of certain strategies. All the Internet users are responsible for defense, starting from home or business computer users, system administrators, developers, up to web administrators and ISPs. The defense must be considered as a permanent and comprehensive process in which all the activities must be proactive. This is the only way to achieve good results and to protect computers, i.e. Web services/applications against the activities with bad intentions. 

**Countermeasures** against *botnet treats* can be broadly classified into two approaches: 
\item technical approaches
\item social and regulatory approaches

#### Technical Approach

Most of **Botnet countermeasures** focus on the commandand-control infrastructure of botnets by *filtering botnetrelated traffic*, *sinkholing domains* with the assistance of DNS registrars or *obtaining the shutdown of malicious servers* in data centers. The *technical botnet defense approach* includes __*Blacklisting, Packet Filtering, Reverse Engineering and Port Blocking*__.

#### Blacklisting
A **blacklist** may provide single IP addresses of malicious hosts or whole subnets showing suspicious activities. A **blacklist** can be used to block all traffic from included addresses and also to filter websites with suspicious or proven malicious contents. 

**For exemple**, the *Spamhaus Project* provides various real-time lists that assist in identifying and blocking attempts by malicious activities. **Spamhaus Block List** (SBL) and the **Domain Block List** (DBL) contain a collection of IP addresses and domain names respectively from which incoming e-mail should not be accepted.

##### Packet Filtering
The **packet filtering** can be applied at a host, network and ISP level. A typical component that performs packet filtering at host level is a *desktop firewall*. Its purpose is to monitor the network activities of all active processes. As the amount of traffic at host level is usually manageable, deep-packet inspection is applicable. Often, user or administrator interaction is required to allow or deny network access for certain applications, if no suitable rules have been specified for them yet.

##### Reverse Engineering
Recovering the functionality of a program without the source code is known as **reverse engineering**. The
malware reverse engineering technique helps in extracting the details of the installation and spreading of malware. The process involves static analysis and dynamic analysis. In case of static analysis, the binary is not executed. This phase deals with the reconstruction of certain aspects of the functionality. The dynamic analysis deals with the execution of the sample. The behavior of the malware can be determined by monitoring the host.

##### Port Blocking
**Port blocking** is a preventive measure that can be applied by ISPs to reducing the amount of spam mails traversing their network. The use of unauthenticated services via port 25, like direct mail exchange or open relay mail servers is almost exclusively for spam distribution purposes. Hence, blocking port 25 at ISP level has been recommended as best practice.