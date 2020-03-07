---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.10.1, released on March 6, 2020.

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

[trellis-0.10.1.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.10.1.zip)
(Size: 39.0 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.1.zip.sha256): a93b8757e77500a3930d9396a18fc62cce95e152b0426a85ed6099b9c4d045f7

[trellis-0.10.1.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.10.1.tar)
(Size: 43.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.1.tar.sha256): f4e45385df0695972796a8a1ca8a290e151ddceadc83c264fa272fe158700b64

### Relational database packages

[trellis-db-0.10.1.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.1.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.1.zip.sha256): 192087735aa1b727f8e52ba809ddbb5122e17edacf73d59f94f9fea605ee7ce5

[trellis-db-0.10.1.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.1.tar)
(Size: 51.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.1.tar.sha256): 63659de34ef0ba967dbc85d6841858a760bb11196a8de5c9f2893944bac0f4e5

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

