---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward. The latest version is 0.12.1, released on May 27, 2020.

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

### Downloads

[trellis-0.12.1.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.12.1.zip)
(Size: 46.8 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.12.1.zip.sha256): d8c392721d207cb4aed74cdf05f1455aa20a380e08107ddfeebd84bb8d8a775f

[trellis-0.12.1.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.12.1.tar)
(Size: 51.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.12.1.tar.sha256): b4b7f506c9916574aaea85bdcef1fda411892ecb01d3ffa33ec50d33bb334fc4

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

