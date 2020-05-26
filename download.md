---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward. The latest version is 0.12.0, released on May 24, 2020.

  * Source code for the [current version](https://github.com/trellis-ldp/trellis/releases/latest)

_Prerequisites_: before installing Trellis, be sure to have a Java 8 (or newer) runtime installed.

---

## Docker containers

Trellis is available as a container from Docker Hub and can be retrieved (for the triplestore
version) with:

    $ docker pull trellisldp/trellis-triplestore

or, for the PostgreSQL database version:

    $ docker pull trellisldp/trellis-postgresql

In addition, there is a container that includes support for a triplestore backend as well as various relational
database systems (H2, PostgreSQL, MariaDB/MySQL). This container tends not to be as performant:

    $ docker pull trellisldp/trellis

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

[trellis-0.12.0.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.12.0.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.12.0.zip.sha256): af59b1833f3dba9c4de3918f286f36d691e484a8ff24176c92c416533cff6b27

[trellis-0.12.0.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.12.0.tar)
(Size: 51.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.12.0.tar.sha256): a834cd14e743e6a5fdb2d56e12461a80dbe5dca3d139619e4e9fb9704f196a5f

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

