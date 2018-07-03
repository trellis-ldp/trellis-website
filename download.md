---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

The [current version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.7.1, released on July 2, 2018.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

## CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-0.7.1-1.noarch.rpm
    $ sudo yum install trellis-0.7.1-1.noarch.rpm

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1-1.noarch.rpm.sha256): be483252525c125d414958a58a46041b2911c323a617e5b5af6ca6643e1212cf

## Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis_0.7.1-1_all.deb
    $ sudo gdebi trellis_0.7.1-1_all.deb

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis_0.7.1-1_all.deb.sha256): 4fc1a0b5f2643de55601d36918defc45d2810852c65a04225b65fe0e72413913

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

[trellis-0.7.1.zip](https://www.trellisldp.org/downloads/trellis-0.7.1.zip)
(Size: 35.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1.zip.sha256): 508030b2df50ae1611d7db26de24631a377620309446194d7af1356f4fad17d1

[trellis-0.7.1.tar](https://www.trellisldp.org/downloads/trellis-0.7.1.tar)
(Size: 40.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1.tar.sha256): 88d60e334a6afbc94a7aecccbcbc39e50d833482c70c3ffdb7eeb69dd3abc1a6

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/Configuration-Guide)
for customizing the server.

