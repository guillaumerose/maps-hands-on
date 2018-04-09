## Préparation des images Docker
La création des fichiers MBTiles (tuiles composant une carte) est gourmande en puissance de calcul et nécessite une machine robuste.
Nous allons donc partir des images mises à disposition par OpenMapTiles.org.

### Récupération de la data
Les fichiers devraient être disponibles sur une clef USB. Dans le cas contraire, suivez les instructions ici.

Pour télécharger le fichier :
- se rendre sur https://openmaptiles.com/downloads/tileset/osm/europe/france/ile-de-france/
- cliquer sur "open-source or open-data project website"
- cliquer sur Free download et se créer un compte
- copier la commande `wget` sous le bouton Free download
- exécuter la commande dans le répertoire `~/maps-hands-on/plan/data`

```
$ mkdir -p ~/maps-hands-on/plan/data
$ cd ~/maps-hands-on/plan/data
$ wget -c https://openmaptiles.os.zhdk.cloud.switch.ch/v3.6.1/extracts/europe/{TOKEN}/2017-07-03_france_ile-de-france.mbtiles
...
2017-07-03_france_ile-de-france.mbtile 100%[============================================================================>] 167.45M  16.2MB/s    in 11s     

2018-04-06 19:13:47 (15.8 MB/s) - ‘2017-07-03_france_ile-de-france.mbtiles’ saved [175587328/175587328]
```

### Lancer l'image docker
```
$ cd ~/maps-hands-on/plan/part0
$ docker-compose up
...
tiles_1  | No MBTiles specified, using 2017-07-03_france_ile-de-france.mbtiles
tiles_1  | Automatically creating config file for 2017-07-03_france_ile-de-france.mbtiles
...
```

### Tester le site

Ouvrez votre navigateur sur http://localhost:8080/.

Vous devriez pouvoir vous déplacer sur la carte, zoomer, etc. Notez que le champ de recherche en haut à gauche n'est pas opérationnel.
