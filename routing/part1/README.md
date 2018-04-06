Bicyle in Paris
====

Get the data
----

Download an extract of France

```
$ cd ~/maps-hands-on/plan/data
$ wget http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf
--2018-04-06 19:54:40--  http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf
Resolving download.geofabrik.de (download.geofabrik.de)... 138.201.81.20, 144.76.80.19
...
```

Extract Paris

```
$ docker run -t -v $(pwd):/data guillaumerose/osmosis --read-pbf ile-de-france-latest.osm.pbf --bounding-box left=2.24 bottom=48.81 right=2.43 top=48.91 --write-pbf paris.osm.pbf
Unable to find image 'guillaumerose/osmosis:latest' locally
...
Apr 06, 2018 5:55:48 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.46
Apr 06, 2018 5:55:48 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Apr 06, 2018 5:55:48 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Apr 06, 2018 5:55:48 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Apr 06, 2018 5:56:14 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline complete.
Apr 06, 2018 5:56:14 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Total execution time: 25897 milliseconds.
$ ls
2017-07-03_france_ile-de-france.mbtiles  ile-de-france-latest.osm.pbf  paris.osm.pbf

```

Prepare the data
---

```
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/bicycle.lua /data/paris.osm.pbf
...
[info] Constructing r-tree of 186299 segments build on-top of 165809 coordinates
[info] finished r-tree construction in 0.049351 seconds
[info] Writing edge-based-graph edges       ... 
[info] ok, after 0.036498s
[info] Processed 338073 edges
[info] Expansion: 25300 nodes/sec and 23471 edges/sec
[info] To prepare the data for routing, run: ./osrm-contract "/data/paris.osrm"
[info] RAM: peak bytes used: 179335168
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
...
[info] Edge-based-graph annotation:
[info]   level 1 #cells 558 bit size 10
[info]   level 2 #cells 52 bit size 6
[info]   level 3 #cells 4 bit size 3
[info]   level 4 #cells 1 bit size 1
[info] Renumbered data in 0.155286 seconds
[info] MultiLevelPartition constructed in 0.038314 seconds
[info] CellStorage constructed in 0.02003 seconds
[info] MLD data writing took 0.016727 seconds
[info] Bisection took 2.7206 seconds.
[info] RAM: peak bytes used: 44367872
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm
[info] Loaded edge based graph: 671008 edges, 153823 nodes
[info] Loading partition data took 0.137652 seconds
[info] Cells customization took 3.2778 seconds
[info] MLD customization writing took 0.011714 seconds
[info] Graph writing took 0.011028 seconds
[info] RAM: peak bytes used: 40161280
```

Run the server
---

```
docker run -d --rm -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/paris.osrm
```



First route
---

```
curl 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544' | jq .
curl 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544?overview=full' | jq .
curl 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544?steps=true' | jq .
```

Change the frontend
---

```html
<script src='/js/mapbox-gl-directions.js'></script>
<link rel='stylesheet' href='/js/mapbox-gl-directions.css' type='text/css' />
```

```
map.addControl(new MapboxDirections({
    api: "http://127.0.0.1:5000/route/v1/",
    profile: "driving",
    accessToken: null,
    geocoder: null,
    unit: "metric",
}), 'top-right');
```

Open a browser and go to http://127.0.0.1:9966
