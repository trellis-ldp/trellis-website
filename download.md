---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.9.3, released on December 18, 2019.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest)
  * The current [relational database version](https://github.com/trellis-ldp/trellis-extensions/releases/latest)

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Docker containers

Trellis is available as a container from Docker Hub and can be retrieved (for the triplestore
version):

    $ docker pull trellisldp/trellis-triplestore

or, for the relational database version:

    $ docker pull trellisldp/trellis-database

Additional Trellis-based docker containers can be found at [Docker Hub](https://hub.docker.com/u/trellisldp).
Information about configuring a [dockerized Trellis
server](https://github.com/trellis-ldp/trellis/wiki/Dockerized-Trellis) can be found on the project wiki.

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.9.3-1.noarch.rpm
    $ sudo yum install trellis-0.9.3-1.noarch.rpm

Size: 38.9 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.3-1.noarch.rpm.sha256): b6a15685bbcc3202ca2600880b4ea6e97aa9243f66a9c70693c08f456c744747

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.9.3-1_all.deb
    $ sudo gdebi trellis_0.9.3-1_all.deb

Size: 39.0 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.9.3-1_all.deb.sha256): eebdcbafa360327f1f648a7e1884ff60e746e04d0f599dfac1f7bc07267e19cc

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3-1.noarch.rpm
    $ sudo yum install trellis-db-0.9.3-1.noarch.rpm

Size: 46.4 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3-1.noarch.rpm.sha256): 37a9bafb6aa06c3ef669f5092f8a2276669f7ad6d959adfaff86add3cbbe7743


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.3-1_all.deb
    $ sudo gdebi trellis-db_0.9.3-1_all.deb

Size: 46.5 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.3-1_all.deb.sha256): e29bbd0ecd8185df2ae179997c136755f4f6723d45c32334aa816cea19a6faf7

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.9.3.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.9.3.zip)
(Size: 39.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.3.zip.sha256): 1122357f8f921cc441fb5826d448de8ef1d2ab4c6b0844f847a06e2ef6d9ffa9

[trellis-0.9.3.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.9.3.tar)
(Size: 43.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.3.tar.sha256): f83c763d1dac4afd4e7de4c81579d32f3fcdb50a34875b7b3cf7b7877b07c8b5

### Relational database packages

[trellis-db-0.9.3.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3.zip)
(Size: 46.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3.zip.sha256): cf0911fcfc6a61c659b7a028e3ddd0bf2c159c282f9a9d0e5c0e4a5471c42fb4

[trellis-db-0.9.3.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3.tar)
(Size: 51.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.3.tar.sha256): 7d61e1ce6dd82ee381efde901480c236f001b1c0c031b1191b0e1ca9d83937ce

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

