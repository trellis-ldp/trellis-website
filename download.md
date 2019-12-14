---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version if 0.9.1, released on December 13, 2019.

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

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.9.1-1.noarch.rpm
    $ sudo yum install trellis-0.9.1-1.noarch.rpm

Size: 38.4 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.1-1.noarch.rpm.sha256): 778f3c112941fb61e911e96cc81cdd088ad170692c83e9fffc66bae1ea515c07

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.9.1-1_all.deb
    $ sudo gdebi trellis_0.9.1-1_all.deb

Size: 38.5 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.9.1-1_all.deb.sha256): 13804321e214d9d8c01b361e9f9c461d22b353e78a966ff89d21bacbf5dc46a3

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1-1.noarch.rpm
    $ sudo yum install trellis-db-0.9.1-1.noarch.rpm

Size: 45.8 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1-1.noarch.rpm.sha256): d87277ff2ad83bb5f7320e5469c29c14c52e7a86dcecbcb4ae7a2abed4bd8293


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.1-1_all.deb
    $ sudo gdebi trellis-db_0.9.1-1_all.deb

Size: 45.9 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db_0.9.1-1_all.deb.sha256): 4098c296305cd70893685b55d0c986cae115809b42c4d73a74b26a9bdb42b843

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.9.1.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.9.1.zip)
(Size: 38.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.1.zip.sha256): 1550a006680b157afe735bb968a417812ef51d97c6b0d9a8024deed667dea390

[trellis-0.9.1.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.9.1.tar)
(Size: 42.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.9.1.tar.sha256): 5e35f6e8d68760a284ac8c21b8db4f2d7c97dd79539718a9cd863fe219fabeeb

### Relational database packages

[trellis-db-0.9.1.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1.zip)
(Size: 46.0 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1.zip.sha256): 0c9534014567f4189ecc6035dd9108041f352bc03621e4ac5505d94c3d9a92a2

[trellis-db-0.9.1.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1.tar)
(Size: 50.8 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.9.1.tar.sha256): 0ac34c5bf890f39f8d4092f48760896d6406ebd1e98c6c30142a8f2bc9f5a362

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

