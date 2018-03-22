FROM openjdk:jre-alpine

WORKDIR /opt/osmosis
RUN wget http://bretth.dev.openstreetmap.org/osmosis-build/osmosis-0.46.tgz
RUN tar -xzvf osmosis-0.46.tgz

WORKDIR /data
ENTRYPOINT ["/opt/osmosis/bin/osmosis"]
