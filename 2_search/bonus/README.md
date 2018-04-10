## Ajout de données personnalisées
Il est bien entendu possible d'ajouter nos propres données au moteur de recherche. Pour le démontrer, nous allons intégrer les zones d'embarquement __STIF__ disponibles en OpenData. Il s'agit d'un petit bout de la donnée accessible, mais cela sera suffisant pour notre exemple.

Nous l'avons convertie au format PBF, mais il est possible de la reconstruire à partir du CSV à l'URL suivante : https://opendata.stif.info/explore/dataset/zde-ref-idf/.

### Intégration des données STIF
1. Copier/coller les données STIF dans le répertoire d'ElasticSearch
```
$ cp DEVOXX_SUPPORT/search/data/stif/zde-ref-idf.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap/
```
2. Déplacez-vous dans le répertoire Pelias
```
$ cd ~/maps-hands-on/search/installation/pelias
```
3. Modifiez la configuration OpenStreetMap dans le fichier __pelias.json__, afin d'y ajouter le fichier zde-ref-idf.osm.pbf
```
$ vi pelias.json
```
Ajoutez une structure pour le fichier zde-ref-idf.osm.pbf dans le tableau "imports.openstreetmap.import".

4. Importez de nouveau les données __STIF/Zones d'Embarquement d'Île-de-France__ dans ElasticSearch
```
$ docker-compose run --rm openstreetmap npm start
...
info: [openstreetmap] Creating read stream for: /data/openstreetmap/zde-ref-idf.osm.pbf
...
```
5. Relancez le serveur HTTP de test de la partie 3 et cherchez les arrêts STIF. Par exemple, la requête `arrêt stif` affichera les premier arrêts rencontrés par Pelias. Essayez aussi des requêtes plus ciblées comme `arret louise michel`.

Si les résultats ne sont pas pertinents, ajustez le slider à la fin de la [partie 3](../part3).

### Pour intégrer d'autres données
Il existe beaucoup de fournisseurs offrant des données riches en contenu, bien souvent vous aurez besoin de transformer cette donnée en format OSM. Il existe des outils adaptés à cela comme par exemple ___osmconvert___, qui convertit en plusieurs formats.

N'hésitez pas à vous inspirer d'un outil Python, que Ulrich a codé pour l'occasion et qui m'a permis de convertir la donnée STIF/CSV en STIF/OSM, [disponible ici](https://github.com/ulrich/osm-stif_to_osm).
