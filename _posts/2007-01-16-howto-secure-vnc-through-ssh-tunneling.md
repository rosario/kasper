---
id: 13
title: 'Howto: Secure VNC through SSH Tunneling'
date: 2007-01-16T11:26:18-07:00
author: Ben
layout: post
guid: http://benrobb.com/2007/01/16/howto-secure-vnc-through-ssh-tunneling/
permalink: /2007/01/16/howto-secure-vnc-through-ssh-tunneling/
categories:
  - tech
---
My web server sits in the baby’s room at my house. It sits in the corner, and the only thing plugged into it is power and network. This is fine for just about everything that I do, but every once in awhile, I have a problem that requires a user interface. VNC to the rescue. Ubuntu comes with Vino, a little VNC Server, pre-installed. You can go to System > Preferences > Remote Desktop to set a password, turn off local user verification, and turn on desktop sharing (as opposed to just viewing).

Then you find your favorite VNC viewer, and type in the network address of your server. This works fine as long as you’re on the local network, but what happens when you’re not on your local network? You could always forward the VNC port through your firewall (port 5900 by default), but VNC is not a secure protocol. Any password typed in would be transmitted in plain-text, and anyone in the world could intercept, and then control your computer, no hack attack needed.

This is where SSH comes to the rescue. SecureSHell (or SSH) creates an encrypted tunnel between two end-points over the network, and gives you a shell (command prompt for you Windows folks) to the remote computer. It’s been around for years, it’s secure, and it continues to prove it’s worth as people come up with more and more uses for it. Tunneling is an example of this.

You can set SSH to accept traffic from a certain port on your computer, send it through an encrypted tunnel, and then end up at a certain port once it gets to the other side of the tunnel - SSH Tunneling.

So when I want to get a graphical interface to my server at home in my office, I can simply open my own shell (Windows users can use Putty) and type

```bash
ssh -L 5900:localhost:5900 username@remote.server.address
```

where the first “5900” represents the local port number and the second represents the remote port number.

You are then prompted for a password like any other SSH connection, and then logged in. Then you simply open your favorite VNC Viewer (I use VNCViewer on my Mac, Chicken of the VNC had serious speed issues) and connect to localhost. Your traffic which would normally be destined for port 5900 is forwarded through the tunnel and instead goes to port 5900 at the other end of the tunnel.

You’ve now got secure VNC.