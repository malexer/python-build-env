"""Create Docker image for Python build environment and run it."""

import os

from fabric.api import lcd, local, task


IMAGE_NAME = 'python-buildenv:0.1'
DEBS_BUILD_LOCATION = 'debs'  # Directory for storing DEBs


@task
def build():
    debs_location = os.path.abspath(DEBS_BUILD_LOCATION)

    local('rm -f "%s"*' % os.path.join(debs_location, ''))
    local('mkdir -p "%s"' % debs_location)

    with lcd('docker'):
        commands = [
            'docker build -t {image} .',
            'docker run --rm -v {debs_dir}:/tmp/debs {image}'
        ]

        for cmd in commands:
            local(cmd.format(debs_dir=debs_location, image=IMAGE_NAME))
