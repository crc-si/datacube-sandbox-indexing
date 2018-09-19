FROM opendatacube/datacube-core

ADD indexing /opt/odc/indexing

WORKDIR /opt/odc/indexing

RUN pip3 install ruamel.yaml
