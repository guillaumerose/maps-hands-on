## Ajout de données personnalisées (partie 4/4)
Il est bien entendu possible d'ajouter nos propres données au moteur de recherche. Pour le démontrer, nous allons intégrer les zones d'embarquement __STIF__ disponibles en OpenData. Il s'agit d'un petit bout de la donnée accessible, mais cela sera suffisant pour notre exemple.

La source de données est disponible au format CSV à l'URL suivante : https://opendata.stif.info/explore/dataset/zde-ref-idf/.

Nous l'avons convertie au format PBF.

### Intégration des données __STIF__
1. Déplacer les données générées dans le répertoire d'ElasticSearch
```
$ cp DEVOXX_SUPPORT/search/data/stif/zde-ref-idf.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap/
```
2. Modifier la configuration OpenStreetMap dans le fichier __pelias.json__ afin d'y ajouter le fichier zde-ref-idf.osm.pbf
```
$ cd ~/maps-hands-on/search/installation/pelias
$ vi pelias.json
```
Ajouter une structure pour le fichier zde-ref-idf.osm.pbf dans le tableau "imports.openstreetmap.import".

3. Importer les données __STIF/Zones d'Embarquement d'Île-de-France__ dans __ElasticSearch__
```
$ docker-compose run --rm openstreetmap npm start
...
info: [openstreetmap] Creating read stream for: /data/openstreetmap/zde-ref-idf.osm.pbf
...
```
A la fin de l'exécution, relancez le serveur HTTP.
```
$ cd ~/maps-hands-on/search/part3
$ python -m SimpleHTTPServer 8000
Serving HTTP on 0.0.0.0 port 8000 ...
```
Chercher à présent les arrêts STIF via requête suivante par exemple : `arrêt stif`.
