Ctshed - Container Toolshed
===========================
![Travis (.org)](https://img.shields.io/travis/kkarolis/ctshed.svg)
![Coveralls github](https://img.shields.io/coveralls/github/kkarolis/ctshed.svg)
![GitHub](https://img.shields.io/github/license/kkarolis/ctshed.svg)
[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)


Container Toolshed. A CLI tool manager for creating container centric
namespaces with specific tools installed. This could possibly help to easier
manage cli tools for users (multiple tool versions, no screw-up with os level
package executables)

Example
-------

```sh
# a single tool executable, debian:stable implicit source
ctshed install --packages=curl --cmd=curl mycurl
# downloads the P04156.fasta file and saves it in the current directory
ctshed-mycurl -LO https://www.uniprot.org/uniprot/P04156.fasta

# a tool namespace 
ctshed install --source=biocontainers/blast:2.2.31 myblast
ctshed-myblast curl -LO https://www.uniprot.org/uniprot/P04156.fasta
ctshed-myblast curl -LO ftp://ftp.ncbi.nih.gov/refseq/D_rerio/mRNA_Prot/zebrafish.1.protein.faa.gz
ctshed-myblast gunzip zebrafish.1.protein.faa.gz
ctshed-myblast makeblastdb -in zebrafish.1.protein.faa -dbtype prot
ctshed-myblast blastp -query P04156.fasta -db zebrafish.1.protein.faa -out results.txt
```

Installation
------------

The tool places binaries to `~/bin` directory blindly without checking if it
exists or if theres a nameclash. Make sure `~/bin` exists in your path. E.g.
place something like this in `~/.bash_rc`:

```sh
#~/.bash_rc file
export PATH="$HOME/bin:$PATH"
```

The tool depends on `docker` binary existing on the host system. You have to
install it if you don't have it. Installation of docker on `ubuntu` systems is described [docker-ce/ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/)


Features
--------

* Create a docker based tool namespace
* Create an executable with specific tool installation


Principles of working
---------------------

1. An image is created during the install step and some name is automatically given to it.
2. An executable is created in executable directory of the users workspace.
3. Executable contains a container run command with stdin/stdout/stderr
   attached and /home directory mounted.

Testing
-------

```sh
python -m unittest discover tests
```

Limitations
-----------

There are limitations with using container as a wrapper for command line.
* Configuration might not be picked up by the tool.
* Input/Output works correctly only under /home directory
* Security, because /home is mounted
* More will come. 
