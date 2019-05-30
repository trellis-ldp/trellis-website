---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.8.3, released on May 29, 2019.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.2.3, released on May 29, 2019.

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

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.8.3-1.noarch.rpm
    $ sudo yum install trellis-0.8.3-1.noarch.rpm

Size: 31.6 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.3-1.noarch.rpm.sha256): e6ba15f5b732add8771e81478854f5579beab5888c669971cca5653a8e1d4384

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.8.3-1_all.deb
    $ sudo gdebi trellis_0.8.3-1_all.deb

Size: 31.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.8.3-1_all.deb.sha256): 9ccd76cbc545f33f271eb5b3c7b37f72ee2d01c5397739435ed2c29d9236d987

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3-1.noarch.rpm
    $ sudo yum install trellis-db-0.2.3-1.noarch.rpm

Size: 42.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3-1.noarch.rpm.sha256): c608b9e1410440ea1b446909ac7d84e77ddf22c98e995500255a3154f6a346d4


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.3-1_all.deb
    $ sudo gdebi trellis-db_0.2.3-1_all.deb

Size: 42.1 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.2.3-1_all.deb.sha256): 8fe80dd746306f91b5bfe7336b27544471ea910eb87b6784e55f37f4c93b05a4

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.8.3.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.8.3.zip)
(Size: 31.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.3.zip.sha256): c7e7612a207f8abc75e01b0254a5a57a8e2701ee94da7d1cc84511a8d21bb595

[trellis-0.8.3.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.8.3.tar)
(Size: 35.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.8.3.tar.sha256): 81bb53b5f9dd466834792f3a708cdb4e8b1b77c00aa5f3ef69a11a2e1877de1a

### Relational database packages

[trellis-db-0.2.3.zip](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3.zip)
(Size: 42.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3.zip.sha256): ab77da77792f928ac31f6cb9eaca2e05c68ef90bc87a956efd127141b19822da

[trellis-db-0.2.3.tar](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3.tar)
(Size: 46.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.2.3.tar.sha256): 304180a31bdfea1b0306ba92072a1185d16697ff2d7601eb8bad4585600233b8

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

