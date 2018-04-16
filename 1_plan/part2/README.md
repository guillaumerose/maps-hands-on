## Personnalisation du thème

### Lancement du serveur
Lancer l'image Docker
```shell
$ cd ~/maps-hands-on/1_plan/part2
$ docker-compose up
...
tiles_1  | No MBTiles specified, using 2017-07-03_france_ile-de-france.mbtiles
tiles_1  | Automatically creating config file for 2017-07-03_france_ile-de-france.mbtiles
...
```

### Une carte pour tous, tous sa propre carte !
Ouvrez votre navigateur sur http://127.0.0.1:8080/ (_pas_ localhost)

Vous pouvez éditer le fichier `style.json`, modifier les valeurs et rafraîchir votre navigateur afin d'avoir votre propre thème graphique.