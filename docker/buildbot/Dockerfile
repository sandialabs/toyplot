FROM toyplot/supervisord
MAINTAINER Timothy M. Shead <tshead@sandia.gov>

# Configure yum.
RUN yum install -y --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

# Install yum packages.
RUN yum install -y buildbot-master buildbot-slave ffmpeg git numpy python3-numpy pygtk2 python-coverage python-mock python-nose python-pip python-sphinx python-sphinx_rtd_theme python3-coverage python3-mock python3-nose python3-pip python3-sphinx python3-sphinx_rtd_theme vim

# Install pip packages.
RUN pip install colormath multipledispatch git+https://github.com/behave/behave
RUN python3-pip install colormath multipledispatch git+https://github.com/behave/behave

# Setup the toyplot user.
RUN /usr/sbin/useradd --create-home --home-dir /home/toyplot --shell /bin/bash -G wheel toyplot
RUN echo 'toyplot:toyplot' | chpasswd
USER toyplot
RUN echo "alias vi=vim" >> /home/toyplot/.bashrc
RUN echo "alias ls='ls --color=auto'" >> /home/toyplot/.bashrc
RUN echo "export TERM=xterm-256color" >> /home/toyplot/.bash_profile
RUN cd /home/toyplot; buildbot create-master buildmaster
RUN cd /home/toyplot; buildslave create-slave python27-worker localhost:9989 python27-worker pass
RUN cd /home/toyplot; buildslave create-slave python33-worker localhost:9989 python33-worker pass
RUN touch /home/toyplot/.gitconfig
RUN HOME=/home/toyplot git config --global push.default simple
RUN HOME=/home/toyplot git config --global color.ui true
ADD .vimrc /home/toyplot/.vimrc
ADD master.cfg /home/toyplot/buildmaster/master.cfg

# Expose the buildmaster directory as a volume, so configuration and build results
# can be retained between upgrades.
VOLUME /home/toyplot/buildmaster

# Don't remove this, as it controls the user used to start supervisord in the base image.
USER root
ADD buildbot.conf /etc/supervisord.d/buildbot.conf
RUN mkdir -p /var/log/buildbot
