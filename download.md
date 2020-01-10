---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.9.4, released on January 10, 2020.

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

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.9.4-1.noarch.rpm
    $ sudo yum install trellis-0.9.4-1.noarch.rpm

Size: 38.9 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.4-1.noarch.rpm.sha256): b845c054c4cabfcb8aafccaa215ba2097808cca168dd0a2569db94edccd3c262

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.9.4-1_all.deb
    $ sudo gdebi trellis_0.9.4-1_all.deb

Size: 39.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.9.4-1_all.deb.sha256): 4ca8f5718036a137fd7c54da4ed021568dcea4083e0c659c01164859ab5f06c8

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4-1.noarch.rpm
    $ sudo yum install trellis-db-0.9.4-1.noarch.rpm

Size: 46.4 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4-1.noarch.rpm.sha256): 2f6825b143536a50c32f5dc65564fe6becd5ed0443a5029a5c889037f33e25fe


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.4-1_all.deb
    $ sudo gdebi trellis-db_0.9.4-1_all.deb

Size: 46.5 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.4-1_all.deb.sha256): 82a3bb42b0e2f46a282d7cd3bd0f86b25ac9e81a2956ee527ff88e342111edc4

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.9.4.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.9.4.zip)
(Size: 39.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.4.zip.sha256): d5642a52dfa2e54d95800a721060cdb2ba57d84cc2c5f1fe964766d08515a7ba

[trellis-0.9.4.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.9.4.tar)
(Size: 43.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.4.tar.sha256): 05d7fbe72183c946dc19eab5e47a626010fbe0d86c399b802d7fa17975e7b0c7

### Relational database packages

[trellis-db-0.9.4.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4.zip)
(Size: 46.6 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4.zip.sha256): fb4843270c53a0c05746179c561bbb81b7e9618a4b35b1391f24c068324a13cd

[trellis-db-0.9.4.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4.tar)
(Size: 51.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.4.tar.sha256): 6118a8d34b6cab8c109efda15f9160d0b2eb5a8011c8532aa7c3d91b19aa6c57

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

