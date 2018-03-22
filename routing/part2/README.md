Bike to Montmartre
===

![GitHub Logo](paris.png)

Get the data
----

Copy it from the part 1.

```
cp ../part1/paris.osm.pbf .
```

Prepare the data
---

```
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-extract -p /data/profiles/bicycle.lua /data/paris.osm.pbf
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm
```

Run the server
---

```
docker stop $(docker ps -q --filter ancestor=osrm/osrm-backend)
docker run -d --rm -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/paris.osrm
```

Go to http://127.0.0.1:9966 and try to bike to Montmartre
