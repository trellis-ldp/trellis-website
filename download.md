---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.7.2, released on August 17, 2018.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.1.1, released on August 17, 2018.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.7.2-1.noarch.rpm
    $ sudo yum install trellis-0.7.2-1.noarch.rpm

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.2-1.noarch.rpm.sha256): f58574ac075a3b6d462e64340e744f067f87805a9456ec0d39fbdc00e19f0290

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.7.2-1_all.deb
    $ sudo gdebi trellis_0.7.2-1_all.deb

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.7.2-1_all.deb.sha256): 1a2109ebb0a3bed92939fb77055c2df5f332dfe6ca2e743320e76699c38bdb65

---

## Relational database persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHad-based systems, the relational database version of Trellis can be installed with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1-1.noarch.rpm
    $ sudo yum install trellis-db-0.1.1-1.noarch.rpm

Size: 40.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1-1.noarch.rpm.sha256): d348081ca27bbc7ae3a43d03d1ddf27f9c995643009df282606ccc202c67ee27


### Ubuntu 16.04 LTS / Debian 8+

The relational database version can be installed with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.1.1-1_all.deb
    $ sudo gdebi trellis-db_0.1.1-1_all.deb

Size: 40.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db_0.1.1-1_all.deb.sha256): 940a69dd1d7c31dbf96b1e969240c30652de3c204e6fd8553caec39e6006e934

---

## Other Platforms

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.7.2.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.7.2.zip)
(Size: 35.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.2.zip.sha256): 4d22523c27e03e3201bcaf853b180ca0bb5982a6682d6209ff29b1363407e5f4

[trellis-0.7.2.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.7.2.tar)
(Size: 40.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.2.tar.sha256): 2d814b7abcd25bc4658c8a7c083c8f96883d0a81bf4e5f7a7aee4bfe9d9434f2

### Relational database packages

[trellis-db-0.1.1.zip](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1.zip)
(Size: 40.8 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1.zip.sha256): a3a61209be50efc72b44777e0cccc9b1b2332770aa078fbdba9c2553ad4c7e40

[trellis-db-0.1.1.tar](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1.tar)
(Size: 45.6 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-ext-db/trellis-db-0.1.1.tar.sha256): 24f691e3ae44200a718746fe689756b73e9f8abf44df4cf7b468dd9c9f492d87

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/Configuration-Guide)
for customizing the server.

