Bootstrap: docker
From: glotzerlab/software

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	apt-get update
	apt-get install python3-mpi4py
	apt-get install python3-scipy
	apt-get install python3-matplotlib
