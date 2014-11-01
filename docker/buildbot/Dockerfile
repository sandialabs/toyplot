FROM toyplot/sshd
MAINTAINER Timothy M. Shead <tshead@sandia.gov>

# Configure yum.
RUN yum install -y --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Install yum packages.
RUN yum install -y buildbot-master buildbot-slave ffmpeg git numpy pygtk2 python-coverage python-nose python-pip python-sphinx python-sphinx_rtd_theme vim

# Install pip packages.
RUN pip install colormath multipledispatch

# Setup the root user.
RUN echo 'root:toyplot' | chpasswd

# Setup the toyplot user.
RUN /usr/sbin/useradd --create-home --home-dir /home/toyplot --shell /bin/bash -G wheel toyplot
RUN echo 'toyplot:toyplot' | chpasswd
USER toyplot
RUN echo "alias vi=vim" >> /home/toyplot/.bash_profile
RUN cd /home/toyplot; buildbot create-master buildmaster
RUN cd /home/toyplot; buildslave create-slave buildworker localhost:9989 basic-worker pass
RUN touch /home/toyplot/.gitconfig
RUN HOME=/home/toyplot git config --global push.default simple
RUN HOME=/home/toyplot git config --global color.ui true
ADD .vimrc /home/toyplot/.vimrc

# Don't remove this, as it controls the user used to start supervisord in the base image.
USER root

ADD master.cfg /home/toyplot/buildmaster/master.cfg
RUN chown toyplot:toyplot /home/toyplot/buildmaster/master.cfg

ADD buildbot.conf /etc/supervisord.d/buildbot.conf
RUN mkdir -p /var/log/buildbot
