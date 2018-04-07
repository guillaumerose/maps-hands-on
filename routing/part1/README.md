## Calcul d'itinéraire à Paris

### Obtenir les données

Téléchargez un extrait des données pour l'Île-de-France.

```
$ cd ~/maps-hands-on/plan/data
$ wget http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf
--2018-04-06 19:54:40--  http://download.geofabrik.de/europe/france/ile-de-france-latest.osm.pbf
Resolving download.geofabrik.de (download.geofabrik.de)... 138.201.81.20, 144.76.80.19
...
```
Extrayez-en uniquement les données pour Paris.

```
$ docker run -t -v $(pwd):/data guillaumerose/osmosis --read-pbf ile-de-france-latest.osm.pbf --bounding-box left=2.24 bottom=48.81 right=2.43 top=48.91 --write-pbf paris.osm.pbf
...
Apr 06, 2018 5:56:14 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline complete.
Apr 06, 2018 5:56:14 PM org.openstreetmap.osmosis.core.Osmosis run
INFO: Total execution time: 25897 milliseconds.
$ ls
2017-07-03_france_ile-de-france.mbtiles  ile-de-france-latest.osm.pbf  paris.osm.pbf

```

### Préparer les données

```
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-extract -p /opt/bicycle.lua /data/paris.osm.pbf
...
[info] Expansion: 25300 nodes/sec and 23471 edges/sec
[info] To prepare the data for routing, run: ./osrm-contract "/data/paris.osrm"
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
...
[info] Renumbered data in 0.155286 seconds
[info] MultiLevelPartition constructed in 0.038314 seconds
[info] CellStorage constructed in 0.02003 seconds
[info] MLD data writing took 0.016727 seconds
[info] Bisection took 2.7206 seconds.
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm
...
[info] Cells customization took 3.2778 seconds
[info] MLD customization writing took 0.011714 seconds
[info] Graph writing took 0.011028 seconds
```

### Lancer le serveur d'itinéraire

```
$ docker run -d --rm -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/paris.osrm
$ docker ps  | grep osrm
f0b7ba501a43        osrm/osrm-backend          "osrm-routed --algor…"   28 seconds ago      Up 27 seconds       0.0.0.0:5000->5000/tcp   upbeat_newton
```

### Vérifier le serveur d'itinéraire

```
$ curl -s 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544' | jq .
{
  "code": "Ok",
  "routes": [
    {
      "geometry": "ahfiHwxfMk@aD_GiEuIrCwWuJuO}@c[aJB{@_[mGkHpCgPSE}BsEw@jAaGiAWYgE",
      "legs": [
        {
          "steps": [],
          "distance": 3134.2,
          "duration": 1117.7,
          "summary": "",
          "weight": 1117.7
        }
      ],
      "distance": 3134.2,
      "duration": 1117.7,
      "weight_name": "duration",
      "weight": 1117.7
    }
  ],
  "waypoints": [
    {
      "hint": "fj0AgN47AIAPAAAAEwAAAGoAAADDAQAADwAAABMAAABqAAAAwwEAAA0AAAAZnCMAqJHpAlOcIwCNkekCBQBvDaJpB3I=",
      "name": "Place du Carrousel",
      "location": [
        2.333721,
        48.861608
      ]
    },
    {
      "hint": "nTQAgHg1AIAWAAAAEwAAALUAAAAAAAAAFgAAABMAAAC1AAAAAAAAAA0AAACwwCMAfPDpArTAIwBg8OkCCQBPBaJpB3I=",
      "name": "Rue du Cardinal Dubois",
      "location": [
        2.343088,
        48.885884
      ]
    }
  ]
}
$ curl -s 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544?overview=full' | jq .
...
$ curl -s 'http://localhost:5000/route/v1/driving/2.3337793350219727,48.86158097877283;2.3430919647216797,48.885855610021544?steps=true' | jq .
...
```

Changer le frontend
---

Modifier le fichier `index.html` du serveur lancé à l'étape précédente.
```
$ cd ~/maps-hands-on/plan/part0/static
$ vi index.html
```

Y ajouter les instructions suivantes.

```html
<script src='/js/mapbox-gl-directions.js'></script>
<link rel='stylesheet' href='/js/mapbox-gl-directions.css' type='text/css' />
```

```
map.addControl(new MapboxDirections({
    api: "http://127.0.0.1:5000/route/v1/", // adresse du serveur d'itinéraire
    profile: "driving",
    accessToken: null,
    geocoder: null,
    unit: "metric",
}), 'top-right');
```

Ouvrez un navigateur à l'adresse http://localhost:8080/.

Le premier clic sur la carte donne le point de départ de l'itinéraire. Le deuxième donne le point d'arrivée.

Les clics suivants changent les points de départ et d'arrivée.
