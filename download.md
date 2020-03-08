---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.10.2, released on March 8, 2020.

  * The current [triplestore-based version](https://github.com/trellis-ldp/trellis/releases/latest)
  * The current [relational database version](https://github.com/trellis-ldp/trellis-extensions/releases/latest)

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Docker containers

Trellis is available as a container from Docker Hub and can be retrieved (for the triplestore
version) with:

    $ docker pull trellisldp/trellis-triplestore

or, for the relational database version:

    $ docker pull trellisldp/trellis-database

Additional Trellis-based docker containers can be found at [Docker Hub](https://hub.docker.com/u/trellisldp).
Information about configuring a [dockerized Trellis
server](https://github.com/trellis-ldp/trellis/wiki/Dockerized-Trellis) can be found on the project wiki.

---

## Manual Installation

Trellis can be run on any system with Java 8 or higher, and it is regularly
tested on Windows, Mac OS and generic Linux machines. To install Trellis
manually, download the software as a Zip or Tar archive and follow the
[manual installation instructions](https://github.com/trellis-ldp/trellis/wiki/Manual-Installation).

### Triplestore-based packages

[trellis-0.10.2.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.10.2.zip)
(Size: 39.0 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.2.zip.sha256): 92bda069bcd7b1784ae1a6be3441c767a5caa849693adb3391771212094ee97f

[trellis-0.10.2.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.10.2.tar)
(Size: 43.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.2.tar.sha256): 5351a0a0f6197ea8339f82de4639166331e7e8c1b6d6f0a82857618b733dab30

### Relational database packages

[trellis-db-0.10.2.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.2.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.2.zip.sha256): 170a2750c51a2bc20e5f50d8c2104198021ec3f3849f176fa2a061392f49a6dd

[trellis-db-0.10.2.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.2.tar)
(Size: 51.6 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.2.tar.sha256): 9c603d6c4386b0731440250afb88cb8add8adb77bf760281856ab66bc4d21ac1

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

