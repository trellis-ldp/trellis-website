---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.8.2, released on May 11, 2019.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.2.2, released on May 11, 2019.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Docker containers

Trellis is available as a container from Docker Hub and can be retrieved (for the triplestore
version):

    $ docker pull trellisldp/trellis

or, for the relational database version:

    $ docker pull trellisldp/trellis-ext-db

Additional Trellis-based docker containers can be found at [Docker Hub](https://hub.docker.com/u/trellisldp).
Information about configuring a [dockerized Trellis
server](https://github.com/trellis-ldp/trellis/wiki/Dockerized-Trellis) can be found on the project wiki.

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.8.2-1.noarch.rpm
    $ sudo yum install trellis-0.8.2-1.noarch.rpm

Size: 33.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.2-1.noarch.rpm.sha256): e222b7372eaadc6e58d498eb39eb221372727845007357221b2fd941eb1c36d8

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.8.2-1_all.deb
    $ sudo gdebi trellis_0.8.2-1_all.deb

Size: 33.2 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.8.2-1_all.deb.sha256): f217ee88fd0e8b6bf2b4c46f79912101654d61563bf635afa19dd0e4795cbce2

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2-1.noarch.rpm
    $ sudo yum install trellis-db-0.2.2-1.noarch.rpm

Size: 44.4 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2-1.noarch.rpm.sha256): ba89426fcf5c685ec619e1071b1e87e8fa5e2ddb494c56721fd4e4858aaee5ed


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.2-1_all.deb
    $ sudo gdebi trellis-db_0.2.2-1_all.deb

Size: 44.5 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.2-1_all.deb.sha256): 7a2ecf28c6c033add7fd6a4bb73c49fbaf4785e0472cc4114a8263f18d7c59fe

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.8.2.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.8.2.zip)
(Size: 33.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.2.zip.sha256): cacb80491a3c756a5ba8fd108983dc3c2557bab625973562b107f2f347997271

[trellis-0.8.2.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.8.2.tar)
(Size: 37.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.2.tar.sha256): 80f7b07047e93cd1370f2d9597d44a272e8952b64eed244a6bbb431269682a1b

### Relational database packages

[trellis-db-0.2.2.zip](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2.zip)
(Size: 44.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2.zip.sha256): 1a671617408b0f0bbb4242ef384f534cd4027ada9238ce63261acb95bf136c6e

[trellis-db-0.2.2.tar](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2.tar)
(Size: 49.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.2.tar.sha256): 76b2b0269e5d1df3c41dd2ecb6b532b73deafd1a41ad023d948ea4a6ef4dd75b

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

