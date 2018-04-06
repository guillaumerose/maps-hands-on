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
docker run -t -v $(pwd):/data guillaumerose/osmosis --read-pbf ile-de-france-latest.osm.pbf --bounding-box left=2.24 bottom=48.81 right=2.43 top=48.91 --write-pbf paris.osm.pbf
```

Prepare the data
---

```
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/bicycle.lua /data/paris.osm.pbf
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm
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
