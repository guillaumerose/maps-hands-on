## Récupération de la donnée et préparation des images Docker
La création des fichiers MBTiles (tuiles composant une carte) est gourmande en puissance de calcul et nécessite une machine robuste.
Nous allons donc partir des images mises à disposition par OpenMapTiles.org.

### Récupération de la data
Vous pouvez récupérer le fichier __mbtiles__ de l'Île-de-France sur le support USB ou via le site __openmaptiles__.

1. Préparation du répertoire de données
```
$ mkdir -p ~/maps-hands-on/1_plan/data
$ cd ~/maps-hands-on/1_plan/data
```
2. Copier le fichier mbtiles du support USB
```
$ cp DEVOXX_SUPPORT/plan/data/2017-07-03_france_ile-de-france.mbtiles ~/maps-hands-on/1_plan/data
```
2. (bis) Télécharger le fichier mbtiles de chez OpenMapTiles
- se rendre sur https://openmaptiles.com/downloads/tileset/osm/europe/france/ile-de-france/
- cliquer sur "open-source or open-data project website"
- cliquer sur _Free download_ et se créer un compte
- copiez et exécutez la commande `wget` sous le bouton Free download
```
La sortie devrait être comme suit...
...
2017-07-03_france_ile-de-france.mbtile 100%[============================================================================>] 167.45M  16.2MB/s    in 11s     

2018-04-06 19:13:47 (15.8 MB/s) - ‘2017-07-03_france_ile-de-france.mbtiles’ saved [175587328/175587328]
```

### Lancement du serveur
3. Lancer l'image Docker
```
$ cd ~/maps-hands-on/1_plan/part0
$ docker-compose up
...
tiles_1  | No MBTiles specified, using 2017-07-03_france_ile-de-france.mbtiles
tiles_1  | Automatically creating config file for 2017-07-03_france_ile-de-france.mbtiles
...
```

### Tester le site
Ouvrez votre navigateur sur http://localhost:8080/

Vous devriez pouvoir vous déplacer sur la carte, zoomer, etc. Notez que le champ de recherche en haut à gauche __n'est pas encore opérationnel__.