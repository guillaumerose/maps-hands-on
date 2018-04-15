### Lancement du serveur
1. Lancer l'image Docker
```
$ cd ~/maps-hands-on/1_plan/part1
$ docker-compose up
...
tiles_1  | No MBTiles specified, using 2017-07-03_france_ile-de-france.mbtiles
tiles_1  | Automatically creating config file for 2017-07-03_france_ile-de-france.mbtiles
...
```

### Tester le site
Ouvrez votre navigateur sur http://127.0.0.1:8080/

Vous devriez voir des pois perso en zoomant sur Paris ,  etc...
