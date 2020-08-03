---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward. The latest version is 0.14.1, released on August 3, 2020.

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

[trellis-0.14.1.zip](https://dl.cloudsmith.io/public/trellisldp/release/raw/names/Trellis/versions/0.14.1/trellis-0.14.1.zip)
(Size: 47.0 MB)  
SHA-256: 523ff7b1c310bf86e51ab5042f06ca3ffac5576c0c6fd786b087ab845ad740f7

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

