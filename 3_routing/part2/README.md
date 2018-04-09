## En vélo à Montmartre

![Altitudes de Paris](paris.png)

Nous allons modifier le calcul d'itinéraire pour minimiser les montées en vélo.

### Préparer les données

Copiez les données de la première partie.

```
$ cd ~/maps-hands-on/routing/part2
$ cp ~/maps-hands-on/plan/data/paris.osm.pbf .
```

Créez un graphe à partir des données d'altitude et des données OpenStreetMap.

```
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-extract -p /data/profiles/bicycle.lua /data/paris.osm.pbf
...
[info] [source loader] Loading from /data/paris.asc  ... 
...
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-partition /data/paris.osrm
...
[info] Edge-based-graph annotation:
[info]   level 1 #cells 560 bit size 10
[info]   level 2 #cells 52 bit size 6
[info]   level 3 #cells 4 bit size 3
[info]   level 4 #cells 1 bit size 1
...
$ docker run -t --rm -v $(pwd):/data osrm/osrm-backend osrm-customize /data/paris.osrm
[info] Loaded edge based graph: 672688 edges, 153809 nodes
...
```

Relancer le serveur avec les nouvelles données
---

```
$ docker stop $(docker ps -q --filter ancestor=osrm/osrm-backend)
$ docker run -d --rm -t -i -p 5000:5000 -v $(pwd):/data osrm/osrm-backend osrm-routed --algorithm mld /data/paris.osrm
```

- Rafraîchir http://localhost:8080/ dans votre navigateur.
- Zoomer sur Montmartre
- Demander un itinéraire depuis la Place de Clichy, jusqu'à la rue Azaïs, près du parvis du Sacré Coeur.

Vous devriez voir un itinéraire qui passe par le nord de Montmartre.

Modifier le calcul des pénalités
---

Le calcul des pénalités en fonction de la pente se trouve à la toute fin du fichier `~/maps-hands-on/routing/part2/profiles/bicycle.lua`.

Modifiez-le, re-créez le graphe des données (les trois instructions `docker run` ci-dessus), puis relancer le serveur (instructions `docker stop` et `docker run` ci-dessus).
