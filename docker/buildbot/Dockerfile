FROM toyplot/sshd
MAINTAINER Timothy M. Shead <tshead@sandia.gov>

# Install yum packages.
RUN yum install -y buildbot-master buildbot-slave

# Setup the root user.
RUN echo 'root:toyplot' | chpasswd

# Setup the toyplot user.
RUN /usr/sbin/useradd --create-home --home-dir /home/toyplot --shell /bin/bash -G wheel toyplot
RUN echo 'toyplot:toyplot' | chpasswd
USER toyplot
RUN cd /home/toyplot; buildbot create-master master; mv master/master.cfg.sample master/master.cfg
#ADD buildbot.conf /etc/supervisord.d/buildbot.conf

# Don't remove this, as it controls the user used to start supervisord in the base image.
USER root

RUN mkdir -p /var/log/buildbot
