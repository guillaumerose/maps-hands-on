# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajout de données personnalisées (partie 5/4)
Il est bien entendu possible d'ajouter nos propres données au moteur de recherche. Pour le démontrer, nous allons intégrer les zones d'embarquements __STIF__ disponibles en OpenData. Il s'agit d'un petit bout de la donnée accessible, mais cela sera suffisant pour notre exemple.

La source de données est disponible au format CSV à l'URL suivante :  https://opendata.stif.info/explore/dataset/zde-ref-idf/.

Deux options s'offrent à vous, vous pouvez essayer de convertir la donnée STIF ou récupérer le fichier PBF généré par votre serviteur sur le support, le copier à l'endroit indiqué ci-dessous et aller directement au paragraphe __Intégration des données STIF__
```
cp DEVOXX_SUPPORT/search/data/stif/zde-ref-idf.osm.pbf ~/maps-hands-on/search/part4/zde-ref-idf.osm.pbf
```

### Conversion des données __STIF__
Pour rendre la donnée STIF compatible avec le format OpenStreetMap, il faut au préalable la convertir au moyen du programme [osmconvert](https://wiki.openstreetmap.org/wiki/Osmconvert). Une version Linux 64bits est disponible sur le support, mais si votre architecture est différente, il faut le compiler, comme indiqué sur le Wiki de l'outil.
1. Copier/coller le programme __osmconvert64__ dans le répertoire part4
```
cp DEVOXX_SUPPORT/search/osmconvert64 ~/maps-hands-on/search/part4/
```
2. Copier/coller le fichier des données __STIF/Zones d'Embarquement d'Île-de-France__ dans le répertoire part4
```
cp DEVOXX_SUPPORT/search/data/stif/zde-ref-idf.csv ~/maps-hands-on/search/part4/
```
3. Lancer la conversion du fichier STIF via l'utilitaire Python3 codé pour l'occasion
```
docker pull python

docker run -it --rm --name zde-ref-idf-converter -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python zde-ref-idf-converter.py > zde-ref-idf.osm
```
En scrutant de près le fichier généré, vous trouverez un ensemble de noeuds XML, qui représentent des arrêts STIF au format OpenStreetMap.

4. Lancer la convertion du fichier généré __OSM__ en __PBF__.
```
./osmconvert64 zde-ref-idf.osm -o=zde-ref-idf.osm.pbf
```
Nous diposons à présent d'un fichier PBF d'environ 460Ko compatible Pelias.

### Intégration des données __STIF__
1. Déplacer les données générées dans le répertoire d'ElasticSearch
```
mv ~/maps-hands-on/search/part4/zde-ref-idf.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap/
```
2. Modifier la configuration OpenStreetMap dans le fichier __pelias.json__ afin d'ajouter le fichier zde-ref-idf.osm.pbf
```
Ajouter le fichier zde-ref-idf.osm.pbf dans le noeud "imports.openstreetmap.import.filename"
```
3. Importer les données __STIF/Zones d'Embarquement d'Île-de-France__ dans __ElasticSearch__
```
docker-compose run --rm openstreetmap npm start
```
Chercher à présent les arrêts STIF via requête suivante  : arrêt stif