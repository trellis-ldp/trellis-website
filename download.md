---
layout: page
title: Download
permalink: /download.html
---

Trellis is an enterprise-ready Linked Data server that makes it possible to build and publish linked data applications on the Web.
Installing Trellis is simple and straight-forward.

There are two flavors of Trellis available. One makes use of a [Triplestore](https://en.wikipedia.org/wiki/Triplestore), and another uses a relational database such as PostgreSQL or MySQL. The latest version is 0.10.0, released on February 21, 2020.

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

[trellis-0.10.0.zip](https://www.trellisldp.org/downloads/trellis/trellis-0.10.0.zip)
(Size: 39.0 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.0.zip.sha256): 44e9c23bcc0fd63843f03e06927c903a51761c688036381fe433c3da4712c3d7

[trellis-0.10.0.tar](https://www.trellisldp.org/downloads/trellis/trellis-0.10.0.tar)
(Size: 43.3 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis/trellis-0.10.0.tar.sha256): 124d4a0b4e40a281f269e4195769ae9d0f2abee48131fa89c5eb04d9665bb925

### Relational database packages

[trellis-db-0.10.0.zip](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.0.zip)
(Size: 46.7 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.0.zip.sha256): 504b85c9474cd21fddc11503de8a17ad66ab55ea4073fc0bd5b3032967f245b3

[trellis-db-0.10.0.tar](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.0.tar)
(Size: 51.5 MB)  
[SHA-256](https://www.trellisldp.org/downloads/trellis-db/trellis-db-0.10.0.tar.sha256): 78068e63d609a8b3b131f440371951ba456ccefe287a06fc7e94fd4c650f7820

---

## Next Steps

After installing Trellis, please refer to the [configuration guide](https://github.com/trellis-ldp/trellis/wiki/App-Configuration-Guide)
for customizing the server.

