FROM centos:latest
LABEL MAINTAINER "Rasmus Munk <rasmus.munk@nbi.ku.dk>"

USER root

RUN yum update -y \
    && yum install -y \
    epel-release \
    nfs-utils \
    net-tools

RUN yum install -y \
    supervisor

ARG SHARE_HOME=/var/nfsshare

RUN mkdir -p $SHARE_HOME \
    && chmod -R 755 $SHARE_HOME \
    && chown nfsnobody:nfsnobody $SHARE_HOME

COPY start-nfs-server.sh /usr/local/bin/
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN chmod +x /usr/local/bin/start-nfs-server.sh

# NFS ports

EXPOSE 111/tcp
EXPOSE 1039/tcp
EXPOSE 1047/tcp
EXPOSE 1048/tcp
EXPOSE 2049/tcp

EXPOSE 111/udp
EXPOSE 1039/udp
EXPOSE 1047/udp
EXPOSE 1048/udp
EXPOSE 2049/udp

ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

