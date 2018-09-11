---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest) is 0.7.3, released on September 11, 2018.
  * The current [relational database version](https://github.com/trellis-ldp/trellis-ext-db/releases/latest) is 0.1.1, released on August 17, 2018.

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Triplestore persistence

### CentOS 7+ / RedHat 7+ / Amazon Linux 2 LTS

For RedHat-based systems, install Trellis (triplestore) with these commands:

    $ wget https://www.trellisldp.org/downloads/trellis/trellis-0.7.3-1.noarch.rpm
    $ sudo yum install trellis-0.7.3-1.noarch.rpm

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.3-1.noarch.rpm.sha256): 602eeb5cdead8935f492a69497f98c359b8a20ceeb791a88a82b46a84bc69873

### Ubuntu 16.04 LTS / Debian 8+

For Debian-based systems, install Trellis (triplestore) with these commands:

    $ sudo apt-get install gdebi-core
    $ wget https://www.trellisldp.org/downloads/trellis/trellis_0.7.3-1_all.deb
    $ sudo gdebi trellis_0.7.3-1_all.deb

Size: 35.7 MB  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis_0.7.3-1_all.deb.sha256): 00cdcb7e420a0e6eb18868884f2b19eefc3cfba2a69c44b94c294001f1d37173

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

[trellis-0.7.3.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.7.3.zip)
(Size: 35.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.3.zip.sha256): 78e7770179005e17a82de5aced94789428d9eeb50af46ed88a50c2c8739cb5a9

[trellis-0.7.3.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.7.3.tar)
(Size: 40.2 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.7.3.tar.sha256): 45cba33f39e907daa1c1984dc82cea5736e70474e31fde1848d020f7044759eb

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

