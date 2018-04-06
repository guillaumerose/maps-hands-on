# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Préparation des images Docker (partie 1/4)
La création des fichiers `mbtiles` est gourmande en puissance de calcul et nécessite une machine robuste.
Nous allons donc partir des images mises à disposition par OpenMapTiles.org.

### Récupération de la data
Pour télécharger le fichier :
- se rendre sur https://openmaptiles.com/downloads/tileset/osm/europe/france/ile-de-france/
- cliquer sur "open-source or open-data project website"
- cliquer sur Free download et se créer un compte
- copier la commande `wget` sous le bouton Free download
- exécuter la commande dans le répertoire `~/maps-hands-on/plan/installation/docker/data`

```
$ ls ~/maps-hands-on/ # devrait afficher le contenu de ce repository
$ mkdir -p ~/maps-hands-on/plan/installation/docker/data
$ cd ~/maps-hands-on/plan/installation/docker/data
$ wget -c https://openmaptiles.os.zhdk.cloud.switch.ch/v3.6.1/extracts/europe/{TOKEN}/2017-07-03_france_ile-de-france.mbtiles
--2018-04-06 19:13:36--  https://openmaptiles.os.zhdk.cloud.switch.ch/v3.6.1/extracts/europe/{TOKEN}/2017-07-03_france_ile-de-france.mbtiles
Resolving openmaptiles.os.zhdk.cloud.switch.ch (openmaptiles.os.zhdk.cloud.switch.ch)... 86.119.32.13, 2001:620:5ca1:1ff::ce53
Connecting to openmaptiles.os.zhdk.cloud.switch.ch (openmaptiles.os.zhdk.cloud.switch.ch)|86.119.32.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 175587328 (167M) [application/octet-stream]
Saving to: ‘2017-07-03_france_ile-de-france.mbtiles’

2017-07-03_france_ile-de-france.mbtile 100%[============================================================================>] 167.45M  16.2MB/s    in 11s     

2018-04-06 19:13:47 (15.8 MB/s) - ‘2017-07-03_france_ile-de-france.mbtiles’ saved [175587328/175587328]

$
```

### Lancer l'image docker
```
$ cd ~/maps-hands-on/plan/part0
$ docker-compose up
```
