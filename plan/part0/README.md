# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Préparation des images Docker (partie 1/4)
La création des fichiers de mbtiles est gourmande en puissance de calul et necessite une machine robuste.
Nous allons donc partir des images mise à disposition par openmaptiles.

### récupération de la data
1. Téléchargement
```
mkdir -p ~/maps-hands-on/plan/installation/docker/data
```
il faut télécharger le fichier depuis: 
https://openmaptiles.com/downloads/tileset/osm/europe/france/ile-de-france/

click sur "open-source or open-data project website"
copier le lien free download

```	
wget -O ~/maps-hands-on/plan/installation/docker/data/idf.mbtiles https://openmaptiles.os.zhdk.cloud.switch.ch/v3.6.1/extracts/europe/{TOKEN}/2017-07-03_france_ile-de-france.mbtiles
```

2. Lancer l'image docker
```
docker run --rm -it -v ~/maps-hands-on/plan/installation/docker/data:/data -p 8080:80 klokantech/openmaptiles-server
```