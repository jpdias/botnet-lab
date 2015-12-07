---
layout: post
title:  "Botnet detection"
excerpt:  "Botnet detection deals with the identification of bots in the machine or network so that some sort of remedy can be done."
date:   2015-12-03 10:00:00
categories: countermeasures
---


## Botnet detection

**Botnet detection** deals with the identification of bots in the machine or network so that some sort of remedy can be done. 

In recent years *botnet detection* has been a hot topic in the research community due to increase in the malicious activity. According to the majority of the common characteristic of a **bot malwareare related to network activities** the bots require some sort of *interaction with the command and control servers*. Some of the *common activities* one could monitor to detect botnets are:

- *opening of specific ports*

- *establishing a number of unwanted network connections*

- *downloading and executing files and programs*

- *creating new processes with well-known names*

- *disabling antivirus software*

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

-  **Active monitoring** -- based on the ability to inject test packets into the network, servers or application for measuring the reactions of network. Hence, it can produce extra traffics on the network. The injected packets can determine whether a human or bot is managing that session. It works in a cause-effect correlation because for a large portion of Botnet command-and-control channels, a command-and-control interaction has a deterministic command response pattern. This technique shows effectiveness on real-world IRC-based Botnet detection.

-  **Passive monitoring** -- observe data traffic in the network and look for suspicious communications that may be provided by bots or command-and-control servers. It does not increase the traffics on the network for inspection.

To access the command-and-control server, bots perform DNS queries to locate the particular server that a DDNS (Dynamic DNS) provider typically hosts. It is thus possible to create a detection mechanism that monitors DNS traffic and searches for some DNS anomalies. Botnets frequently use DNS to rally infected hosts, launch attacks and update their codes.
