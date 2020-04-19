---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.11.1, released on April 18, 2020.

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

[trellis-0.11.1.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.11.1.zip)
(Size: 39.1 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.11.1.zip.sha256): dca3f9610f51c4d17ff4a3b8ccad1652b90433c39d0929b349e69f57e05799f0

[trellis-0.11.1.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.11.1.tar)
(Size: 43.4 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.11.1.tar.sha256): 76874ed1f478bb8fd0c311d6d4b1b538becd7c4661f0bedc014aca81086c0f2e

### Relational database packages

[trellis-db-0.11.1.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.1.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.1.zip.sha256): fa2fd1d4b0aa9476b089ba9d99be36dc05c34ed004ceb426a5e203b5979ad346

[trellis-db-0.11.1.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.1.tar)
(Size: 51.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.11.1.tar.sha256): 9b05eddfed8979d3d3a435c29c7242b94b74d232c07e89f4adae1fba7ce6a856

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

