all: paris.osm.pbf

clean:
	rm -rf _osmosis *.osm.pbf

ile-de-france-latest.osm.pbf:
	wget http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf

_osmosis/bin/osmosis:
	mkdir -p _osmosis
	cd _osmosis && wget https://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip && unzip osmosis-latest.zip

paris.osm.pbf: _osmosis/bin/osmosis ile-de-france-latest.osm.pbf
	./_osmosis/bin/osmosis --read-pbf ile-de-france-latest.osm.pbf --bounding-box left=2.24 bottom=48.81 right=2.43 top=48.91 --write-pbf paris.osm.pbf
