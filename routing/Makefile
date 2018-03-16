all: run

.PHONY: clean
clean:
	rm -rf _osmosis *.osm.pbf *.osrm*

ile-de-france-latest.osm.pbf:
	wget http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf

_osmosis/bin/osmosis:
	mkdir -p _osmosis
	cd _osmosis && wget https://bretth.dev.openstreetmap.org/osmosis-build/osmosis-latest.zip && unzip osmosis-latest.zip

paris.osm.pbf: _osmosis/bin/osmosis ile-de-france-latest.osm.pbf
	./_osmosis/bin/osmosis --read-pbf ile-de-france-latest.osm.pbf --bounding-box left=2.24 bottom=48.81 right=2.43 top=48.91 --write-pbf paris.osm.pbf

paris.osrm: paris.osm.pbf
	docker run -t -v $(shell pwd):/data osrm/osrm-backend osrm-extract -p /data/profiles/bicycle.lua /data/paris.osm.pbf
	docker run -t -v $(shell pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
	docker run -t -v $(shell pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm

.PHONY: run
run: paris.osrm
	docker run -d -p 9966:9966 osrm/osrm-frontend
	docker run -d -t -i -p 5000:5000 -v $(shell pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/paris.osrm
	open http://127.0.0.1:9966
