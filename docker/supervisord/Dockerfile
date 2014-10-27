FROM fedora:20
MAINTAINER Timothy M. Shead <tshead@sandia.gov>

# Setup the supervisor service.
RUN yum install -y supervisor
ADD supervisord.conf /etc/supervisord.conf

# Default startup command.
CMD ["supervisord", "-c", "/etc/supervisord.conf"]

