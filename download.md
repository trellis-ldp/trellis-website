---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.11.2, released on April 23, 2020.

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

[trellis-0.11.2.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.11.2.zip)
(Size: 39.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.11.2.zip.sha256): e5e2c77b6e96aae5038dc835b96a5946ca96681362ff5d08e4e4e97305a748bc

[trellis-0.11.2.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.11.2.tar)
(Size: 43.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.11.2.tar.sha256): c870e23674e69df8d96675e9c30498a172cb67ae52ea5a9ce44a12cb9796bf36

### Relational database packages

[trellis-db-0.11.2.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.2.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.2.zip.sha256): 8e4a66bbdc63934322bfab0b7484402613e5fc768ee00b2d19f42869e03a7b48

[trellis-db-0.11.2.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.2.tar)
(Size: 51.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.2.tar.sha256): 3eb662ea8d47e0833f231f20d410a7b10f1125ade3085eb5a389d6700e86ce9a

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

