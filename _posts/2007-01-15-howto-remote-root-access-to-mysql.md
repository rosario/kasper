---
id: 11
title: 'Howto: Remote Root Access to MySql'
date: 2007-01-15T11:24:11-07:00
author: Ben
layout: post
guid: http://benrobb.com/2007/01/15/howto-remote-root-access-to-mysql/
permalink: /2007/01/15/howto-remote-root-access-to-mysql/
image: /wp-content/uploads/2007/01/GotRoot-144x90.png
excerpt_separator: <!--more-->
categories:
  - tech

---
*Update*: This post has garnered a lot of attention.  So I'd like to clarify up front: this article is not about hacking into other databases.  This is about configuring a server you own so that you can access it from a remote machine on the same network.  It is completely insecure and should never be used for production deployments.

<!--more-->

Very quickly, another thing that I typically like to do on my server boxes is allow root access to my Mysql database from remote computers. I don’t forward the port through my router and I use a very secure password (doesn’t everyone?). I don’t want to create a security risk, I just want to connect to the database from other computers around my network - particularly from my laptop.

Again (like most of my instructions) these instructions are for Ubuntu - currently Edgy Eft.

```bash
sudo apt-get install mysql-server
```

Ubuntu installs Mysql at `/etc/mysql/` by default. Now we need to set a root password.

```bash
mysql -u root
```

```sql
SET PASSWORD FOR 'ROOT'@'LOCALHOST"
> = PASSWORD('new_password');
```

Now while we’re still here, we’ll create a new HOST for root and allow root to login from anywhere.

```sql
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' > IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
exit
```

We’re almost done now. We just have to tell Mysql to allow remote logins.

```bash
sudo vi /etc/mysql/my.cnf
```

Out-of-the-box, MySQL only allows connections from the localhost identified by the IP Address of 127.0.0.1.  We need to remove that restriction, so find the line that says

```bash
bind-address = 127.0.0.1
```

and comment it out. 

```bash
# bind-address = 127.0.0.1
```

That’s all there is to it! Now get your favorite MySql client and start developing.