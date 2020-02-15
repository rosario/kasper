---
id: 9
title: Why is There a Minimum Ethernet Framesize?
date: 2007-01-10T11:21:09-07:00
author: Ben
layout: post
guid: http://benrobb.com/2007/01/10/why-is-there-a-minimum-ethernet-framesize/
permalink: /2007/01/10/why-is-there-a-minimum-ethernet-framesize/
dsq_thread_id:
  - "3055758761"
categories:
  - Old Stuff
---
An ethernet frame has a minimum size of 64 bytes and a maximum size of 1500 bytes. But why is there a minimum?

An ethernet frame has a minimum size because anything that is shorter than the 64 byte minimum is interpreted by receiving stations as a collision.

A transmitting station will begin transmission when it can sense that there is no other transmitting stations (carrier sense). The transmitting station will not know of a collision in transmission until the collision is detected by another receiving station. This receiving station will then transmit a jam sequence and the transmitting station will receive this and break off transmission before it has actually transmitted the first 64 bytes of its ethernet packet.

This allows all receiving stations to interpret any transmission that is less than 64 bytes as a collision, and thus ignore it.

More details can be found on Techfest at <a title="Techfest" href="http://www.techfest.com/networking/lan/ethernet3.htm">http://www.techfest.com/networking/lan/ethernet3.htm</a>.