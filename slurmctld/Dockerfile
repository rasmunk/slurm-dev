FROM centos:7

ARG SLURM_VERSION=18.08.4
ARG SLURM_DOWNLOAD_MD5=75c76328159def203133505def7a99a6
ARG SLURM_DOWNLOAD_URL="https://download.schedmd.com/slurm/slurm-$SLURM_VERSION.tar.bz2"

RUN groupadd -r slurm --gid=990 && useradd -r -g slurm --uid=990 slurm \
    && groupadd -r munge --gid=993 && useradd -r -g munge --uid=997 munge

RUN yum update -y && yum upgrade -y

RUN yum makecache fast \
    && yum -y install epel-release \
    && yum -y install \
           wget \
           bzip2 \
           perl \
           gcc \
           gcc-c++ \
           make \
           munge \
           munge-devel \
           nano \
           openmpi \
           mailx \
           sudo

RUN set -x \
    && wget -O slurm.tar.bz2 "$SLURM_DOWNLOAD_URL" \
    && echo "$SLURM_DOWNLOAD_MD5" slurm.tar.bz2 | md5sum -c - \
    && mkdir /usr/local/src/slurm \
    && tar jxf slurm.tar.bz2 -C /usr/local/src/slurm --strip-components=1 \
    && rm slurm.tar.bz2 \
    && cd /usr/local/src/slurm \
    && ./configure --enable-debug --prefix=/usr --sysconfdir=/etc/slurm \
        --with-mysql_config=/usr/bin  --libdir=/usr/lib64 \
    && make install \
    && cd \
    && rm -rf /usr/local/src/slurm

RUN mkdir -p /etc/slurm \
        /var/spool/slurmd \
        /var/run/slurmctld \
        /var/lib/slurmd \
        /var/log/slurm \
    && touch /var/lib/slurmd/node_state \
        /var/log/slurm_jobacct.log \
        /var/lib/slurmd/front_end_state \
        /var/lib/slurmd/job_state \
        /var/lib/slurmd/resv_state \
        /var/lib/slurmd/trigger_state \
        /var/lib/slurmd/assoc_mgr_state \
        /var/lib/slurmd/assoc_usage \
        /var/lib/slurmd/qos_usage \
        /var/lib/slurmd/fed_mgr_state \
    && chown -R slurm:slurm /var/*/slurm* \
    && /sbin/create-munge-key

RUN mkdir -p /var/run/munge \
    &&  mkdir -p /var/log/munge \
    && chown -R munge:munge /var/run/munge \
    && chown -R munge:munge /var/log/munge \
    && chmod -R 700 /var/log/munge

COPY ./config/slurm.conf /etc/slurm/slurm.conf

RUN groupadd user && useradd -d /home/user -g user user
RUN usermod -aG wheel user
RUN echo "user ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER user

ENTRYPOINT sudo -u munge munged && sudo -u slurm slurmctld -D
