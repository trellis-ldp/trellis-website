---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

The [current version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.7, released on May 25, 2018.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

## CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-0.7.0-1.noarch.rpm
    $ sudo yum install trellis-0.7.0-1.noarch.rpm

Size: 42.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.0-1.noarch.rpm.sha256): 5833df6f7a216e2f0f3e1bbc3a6ad2e0d0f39e8003620fd0b74d219dfebb1df5

## Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis_0.7.0-1_all.deb
    $ sudo gdebi trellis_0.7.0-1_all.deb

Size: 42.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis_0.7.0-1_all.deb.sha256): a86c6022982a78248035ac3134a3c7df03c57a644887dbbb3d2ea995f3b2a251

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

[trellis-0.7.0.zip](https://www.trellisldp.org/downloads/trellis-0.7.0.zip)
(Size: 42.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.0.zip.sha256): 3ee85c62e26c496dc9dca946ae97ae620fac6183c3b1bb0203ec8c4797aac169

[trellis-0.7.0.tar](https://www.trellisldp.org/downloads/trellis-0.7.0.tar)
(Size: 47.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.0.tar.sha256): 5b6d46f67a3d1622136dc2dd113c7a693d0b1ba6e630ebf31161f47c2cbea1d1

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/Configuration-Guide)
for customizing the server.

