---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.8.0, released on January 31, 2019.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.2.0, released on January 31, 2019.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Docker containers

Trellis is available as a container from Docker Hub and can be retrieved (for the triplestore
version):

    $ docker pull trellisldp/trellis

or, for the relational database version:

    $ docker pull trellisldp/trellis-ext-db

All of the Trellis docker containers are available from [Docker Hub](https://hub.docker.com/u/trellisldp).

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.8.0-1.noarch.rpm
    $ sudo yum install trellis-0.8.0-1.noarch.rpm

Size: 31.3 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.0-1.noarch.rpm.sha256): 5340bc0ec30a29a502cf87499cc6d28a1592ffe23647ff79e96e0a9c9437c7e8

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.8.0-1_all.deb
    $ sudo gdebi trellis_0.8.0-1_all.deb

Size: 31.4 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.8.0-1_all.deb.sha256): 1a3b2c8574f7ce77676dfb7ba9902ee9e6df1499dc3af67b0d3e97df10645dca

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0-1.noarch.rpm
    $ sudo yum install trellis-db-0.2.0-1.noarch.rpm

Size: 42.0 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0-1.noarch.rpm.sha256): 187a7dafaa0a26e4802b49f87118fb61b46ef080a3a51772cbc35235a3eab718


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.0-1_all.deb
    $ sudo gdebi trellis-db_0.2.0-1_all.deb

Size: 42.0 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.0-1_all.deb.sha256): 16114f666564fa63a52d3dca1ab949699aaaf41684e31653c01d524737ece23c

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.8.0.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.8.0.zip)
(Size: 31.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.0.zip.sha256): 337da4bcde3440275c20107a7c6edef5ce57644ad383b0c668f07116541a0894

[trellis-0.8.0.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.8.0.tar)
(Size: 35.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.0.tar.sha256): 164784846dab2237b2de1faf894230bc9dcfb264cd9a5e9ff434dddd30aacc38

### Relational database packages

[trellis-db-0.2.0.zip](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0.zip)
(Size: 44.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0.zip.sha256): 73d39881c1ffbdb67c6656dbedf6c534ac232e81db0986333961061a54c98c8b

[trellis-db-0.2.0.tar](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0.tar)
(Size: 46.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.0.tar.sha256): adfdd15fbf18a4d0a42a8d7aa79252d67aeee0772fc5480519d63f50363886f1

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/Configuration-Guide)
for customizing the server.

