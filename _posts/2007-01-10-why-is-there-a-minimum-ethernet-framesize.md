---
id: 9
title: Why is There a Minimum Ethernet Framesize?
date: 2007-01-10T11:21:09-07:00
author: Ben
layout: post
guid: http://benrobb.com/2007/01/10/why-is-there-a-minimum-ethernet-framesize/
permalink: /2007/01/10/why-is-there-a-minimum-ethernet-framesize/
image: /assets/post_images/billiards_balls.jpg
categories:
  - tech
---
An ethernet frame has a minimum size of 64 bytes and a maximum size of 1500 bytes. Anything shorter than the 64 byte minimum is interpreted by receiving stations as a collision.

![Billiard balls are make a different type of collision](/assets/post_images/billiards_balls.jpg)

A station that wants to transmit will begin its transmission when it can sense that there are no other transmitting stations (carrier sense) on the network. Multiple stations can sense this at the same time, and both can begin transmitting at the same time.

The collision is detected when a receiving station receives both transmissions at the same time.  The receiving station will then transmit a jam sequence and the transmitting stations will receive this and break off the transmission before it has actually transmitted the first 64 bytes of the packet it was sending.

This allows all receiving stations to interpret any transmission that is less than 64 bytes as a collision, and thus ignore it.

More details can be found on Techfest at <a title="Techfest" href="http://www.techfest.com/networking/lan/ethernet3.htm">http://www.techfest.com/networking/lan/ethernet3.htm</a>.