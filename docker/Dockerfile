FROM ubuntu:14.04
MAINTAINER Oleksii Markov (alex@markovs.me)
LABEL description="Build environment to create debs for external python dependencies"

RUN apt-get install -y software-properties-common && \
    apt-get update && apt-get install -y \
        python-all-dev \
        python-pip \
        python-setuptools \
        python-stdeb && \
    pip install stdeb --upgrade

WORKDIR /tmp/

COPY build.sh /usr/local/bin/build.sh
COPY requirements.txt /tmp/requirements.txt

CMD ["/usr/local/bin/build.sh"]
