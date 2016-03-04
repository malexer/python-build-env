#!/bin/sh

set -x

pip install -d . --no-use-wheel -r requirements.txt

for SOURCE in *.tar.gz; do
    py2dsc-deb $SOURCE
    mv -f deb_dist/*.deb debs/
    rm -rf ./deb_dist
done;
