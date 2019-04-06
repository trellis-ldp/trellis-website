---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.8.1, released on April 6, 2019.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.2.1, released on April 6, 2019.

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

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.8.1-1.noarch.rpm
    $ sudo yum install trellis-0.8.1-1.noarch.rpm

Size: 31.6 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.1-1.noarch.rpm.sha256): 7f6587a1c16d6b66c3f18ecd5c734320afb7f7eb6a69c88682b86fc3d751500b

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.8.1-1_all.deb
    $ sudo gdebi trellis_0.8.1-1_all.deb

Size: 31.6 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.8.1-1_all.deb.sha256): 723dc0f7d78bde8c4fad8b58a124ac3e67da2a08dbe3f7f57fdc8c917b24312d

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1-1.noarch.rpm
    $ sudo yum install trellis-db-0.2.1-1.noarch.rpm

Size: 42.2 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1-1.noarch.rpm.sha256): a58c79f2191cef9ac2ea4ef8b0c2515ea30061ba3547002ed135ea25ce6dd869


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.1-1_all.deb
    $ sudo gdebi trellis-db_0.2.1-1_all.deb

Size: 42.3 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.1-1_all.deb.sha256): b19ab15b5e6aed16a33f1cc97544ce8a76e527075c16bf1a12f8c3bf659d1dcb

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.8.1.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.8.1.zip)
(Size: 31.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.1.zip.sha256): e6a4fa1f744077c2f98f8a0f1644a6521bb4f02bebd0eba2f6ebae01290cf88f

[trellis-0.8.1.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.8.1.tar)
(Size: 35.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.1.tar.sha256): e743e893199c710a754db4f8c1c1a556f7b262f968b85bb50a2b7fab9f5d5cad

### Relational database packages

[trellis-db-0.2.1.zip](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1.zip)
(Size: 42.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1.zip.sha256): 51d81885aeac06dff3331464f1c47d83ab55c320a7549dd3ae04911652d4077f

[trellis-db-0.2.1.tar](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1.tar)
(Size: 46.6 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.1.tar.sha256): 62fc406a598d6d6ddfd0d2c395b2012c929b5edd24336a874d919b6327805c7d

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

