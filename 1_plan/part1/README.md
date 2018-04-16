## Vérification de l'ensemble

### Lancement du serveur
Lancer l'image Docker
```shell
$ cd ~/maps-hands-on/1_plan/part1

$ docker-compose up
...
tiles_1  | No MBTiles specified, using 2017-07-03_france_ile-de-france.mbtiles
tiles_1  | Automatically creating config file for 2017-07-03_france_ile-de-france.mbtiles
...
```

### Ajouter du javascript
Copier le code Javascript suivant dans la balise script dans le fichier index.html
```js
        map.on('load', function () { map.addLayer(lbc) });
        map.on('click', 'leboncoin', function (e) {
          var coordinates = e.features[0].geometry.coordinates.slice();
          var description = e.features[0].properties.description;
        
          while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
          }

          new mapboxgl.Popup()
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
        });
```

### Tester le site
Ouvrez votre navigateur sur http://127.0.0.1:8080/ (_pas_ locahost)

Vous devriez voir des POIs (points of interest) persos en zoomant sur Paris, etc.