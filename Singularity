Bootstrap: docker
From: glotzerlab/software:cuda8-openmpi3.0

%labels
	MAINTAINER csadorf

%post
	ln -s /usr/bin/python3 /usr/bin/python
	apt-get update && apt-get install -y \
		python3-mpi4py \
		python3-scipy \
		python3-matplotlib
