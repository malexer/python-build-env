# python-build-env

Python build environment as a Docker image.


## Overview

Deploying python applications as a Docker containers stimulate you to minimize
the image size and keep only required stuff inside running container.

At the same time we need some flexible way to deliver specific versions of
python packages with minimum overhead.

Pip is a great tool to solve the first part but we don't really want to have
it in a running container.

One of the options is to create debs for required packages.

[Fabric](http://www.fabfile.org) will be used for automation of the whole workflow.


## Quick-start

1. Install Docker and Fabric.
2. Update `docker/requirements.txt` with your list of python packages.
3. Run `fab build`
4. Check `debs/` directory for all required deb files (including extra
   dependencies).
5. Use this repo as an example to build your own deployment workflow:
   * `*.deb` can be used in Dockerfile: `RUN dpkg -Ri /path/to/debs`
   * use it to automate building you own base images
