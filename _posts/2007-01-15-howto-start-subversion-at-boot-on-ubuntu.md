---
id: 12
title: 'Howto: Start Subversion at Boot on Ubuntu'
date: 2007-01-15T11:25:19-07:00
author: Ben
layout: post
guid: http://benrobb.com/2007/01/15/howto-start-subversion-at-boot-on-ubuntu/
permalink: /2007/01/15/howto-start-subversion-at-boot-on-ubuntu/
image: /wp-content/uploads/2007/01/Ubuntu-87x90.png
excerpt_separator: <!--more-->
categories:
  - tech

---

*Update*: This post was written more than 13 years ago, but for some reason it is still getting a decent amount of views.  At this point, you should all stop using Subversion and move to Git.

<!--more-->

I don’t know if I’ve extolled the virtues of Ubuntu on this blog yet, but they are many. They are, however, not the topic of this post. Every once in a while, I like to try different operating systems on my server, and at the moment, I’m just coming back to an Ubuntu server after a brief fling with Windows Server 2003.

On the list of things to do after install was to get Ubuntu to start the svnserve daemon at boot. I’ve taken the time to look this up enough times that I figured I’d just add it here. This procedure holds for anything you’d like to do at boot, I’m simply running my svn daemon.

## Step 1 - Create your script

Simply create a new file (I called mine svnserve) and type the command you’d like to run

```bash
cd /etc/init.d/ # (thanks Alfonso)
sudo touch svnserve
sudo vi svnserve
svnserve -d -r /usr/local/svn/repository_name
```

## Step 2 - Save the script

Put your script in the `/etc/init.d/` folder.

## Step 3 - Make the script executable

```bash
sudo chmod +x svnserve
```

## Step 4 - Add the script to the boot sequence


```bash
sudo update-rc.d svnserve defaults
```

That’s it. When you’re done you should see some output similar to

```bash
Adding system startup for /etc/init.d/svnserve ...
/etc/rc0.d/K20svnserve -> ../init.d/svnserve
/etc/rc1.d/K20svnserve -> ../init.d/svnserve
/etc/rc6.d/K20svnserve -> ../init.d/svnserve
/etc/rc2.d/S20svnserve -> ../init.d/svnserve
/etc/rc3.d/S20svnserve -> ../init.d/svnserve
/etc/rc4.d/S20svnserve -> ../init.d/svnserve
/etc/rc5.d/S20svnserve -> ../init.d/svnserve
```