FROM stilliard/pure-ftpd

MAINTAINER Theotime Leveque <theotime.leveque@gmail.com>

RUN (echo test; echo test) | pure-pw useradd john -d /tmp/john -u ftpuser
RUN pure-pw mkdb
