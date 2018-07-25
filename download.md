---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.7.1, released on July 2, 2018.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.1.0, released on July 25, 2018.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-0.7.1-1.noarch.rpm
    $ sudo yum install trellis-0.7.1-1.noarch.rpm

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1-1.noarch.rpm.sha256): be483252525c125d414958a58a46041b2911c323a617e5b5af6ca6643e1212cf

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis_0.7.1-1_all.deb
    $ sudo gdebi trellis_0.7.1-1_all.deb

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis_0.7.1-1_all.deb.sha256): 4fc1a0b5f2643de55601d36918defc45d2810852c65a04225b65fe0e72413913

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-db-0.1.0-1.noarch.rpm
    $ sudo yum install trellis-db-0.1.0-1.noarch.rpm

Size: 40.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db-0.1.0-1.noarch.rpm.sha256): 16af434815df3db1b7f4dcc894bfb95783c60f4c0dcf242101cd61407d6a4092


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-db_0.1.0-1_all.deb
    $ sudo gdebi trellis-db_0.1.0-1_all.deb

Size: 40.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db_0.1.0-1_all.deb.sha256): 6030006e3599c688144f0c8c606885a87408f789a728876954ce17883a38a58c

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.7.1.zip](https://www.trellisldp.org/downloads/trellis-0.7.1.zip)
(Size: 35.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1.zip.sha256): 508030b2df50ae1611d7db26de24631a377620309446194d7af1356f4fad17d1

[trellis-0.7.1.tar](https://www.trellisldp.org/downloads/trellis-0.7.1.tar)
(Size: 40.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-0.7.1.tar.sha256): 88d60e334a6afbc94a7aecccbcbc39e50d833482c70c3ffdb7eeb69dd3abc1a6

### Relational database packages

[trellis-db-0.1.0.zip](https://www.trellisldp.org/downloads/trellis-db-0.1.0.zip)
(Size: 40.8 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db-0.1.0.zip.sha256): b430814732720c263e9999e279b0f1aa4b15c87c90c688f788db34fd8df49cba

[trellis-db-0.1.0.tar](https://www.trellisldp.org/downloads/trellis-db-0.1.0.tar)
(Size: 45.6 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db-0.1.0.tar.sha256): 6519b9660e67d682b850944f9accf59a3edcd316e72a452b1ba25c5be8a5c1c3

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/Configuration-Guide)
for customizing the server.

