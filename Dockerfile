FROM opendatacube/datacube-core

ADD indexing /opt/odc/indexing

WORKDIR /opt/odc/indexing

RUN git clone https://github.com/opendatacube/datacube-dataset-config.git \
    && mv datacube-dataset-config/scripts ./scripts \
    && rm -rf datacube-datset-config \
    && ls

RUN pip3 install ruamel.yaml
