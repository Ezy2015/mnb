#########################################################: 
# Dockerfile to run a flask-based web application# Based on an centos:7 image 
##########################################################

# Set the base image to use to centos 
FROM centos

# Set the file maintainer 
MAINTAINER Ezy

# Set env varibles used in this Dockerfile (add a unique prefix, such as DOCKYARD) 
# Local directory with project source 
ENV DOCKYARD_SRC=flask
# Directory in container for all project files 
ENV DOCKYARD_SRCHOME=/opt 
# Directory in container for project source files 
ENV DOCKYARD_SRCPROJ=/opt/toolbox

# Update the defualt application repository source list 
RUN yum -y install epel-release
RUN yum -y install python-pip 
RUN yum -y install mysql-devel
RUN yum -y install gcc python-devel
RUN yum clean all

# Copy application source code to SRCDIR 
COPY $DOCKYARD_SRC $DOCKYARD_SRCPROJ

# Create application subdirectories 
WORKDIR $DOCKYARD_SRCPROJ 
RUN mkdir log 
VOLUME ["$DOCKYARD_SRCPROJ/log/"]

# Install Python dependencies 
RUN pip install --upgrade pip
RUN pip install MySQL-python
RUN pip install flask_bootstrap
RUN pip install flask_wtf
RUN pip install wtforms
RUN pip install flask
RUN chmod 777 $DOCKYARD_SRCPROJ/start_server.sh

# Port to expose 
EXPOSE 5000

# Copy entrypoint script into the image 
ENTRYPOINT ["/bin/bash"]
