## Ajout de données personnalisées
Il est bien entendu possible d'ajouter nos propres données au moteur de recherche. Pour le démontrer, nous allons intégrer les zones d'embarquement __STIF__ disponibles en OpenData. Il s'agit d'un petit bout de la donnée accessible, mais cela sera suffisant pour notre exemple.

Nous l'avons convertie au format PBF, mais il est possible de la reconstruire à partir du CSV à l'URL suivante : https://opendata.stif.info/explore/dataset/zde-ref-idf/.

### Intégration des données STIF
1. Copier/coller les données STIF dans le répertoire d'ElasticSearch
```shell
$ cp ~/DEVOXX_SUPPORT/search/data/stif/zde-ref-idf.osm.pbf ~/maps-hands-on/2_search/installation/data/openstreetmap/
```
2. Déplacez-vous dans le répertoire Pelias
```shell
$ cd ~/maps-hands-on/2_search/installation/pelias
```
3. Modifiez la configuration OpenStreetMap dans le fichier __pelias.json__, afin d'y ajouter le fichier zde-ref-idf.osm.pbf
```shell
$ vi pelias.json
```
Ajoutez une structure pour le fichier zde-ref-idf.osm.pbf dans le tableau "imports.openstreetmap.import".

4. Importez de nouveau les données __STIF/Zones d'Embarquement d'Île-de-France__ dans ElasticSearch
```shell
$ docker-compose run --rm openstreetmap npm start
...
info: [openstreetmap] Creating read stream for: /data/openstreetmap/zde-ref-idf.osm.pbf
info: [dbclient]  paused=false, transient=2, current_length=147, indexed=187500, batch_ok=375, batch_retries=0, failed_records=0, venue=75390, address=112110, persec=2950
info: [dbclient]  paused=false, transient=0, current_length=0, indexed=202801, batch_ok=406, batch_retries=0, failed_records=0, venue=90691, address=112110, persec=1530.1
info: [dbclient]  paused=false, transient=0, current_length=0, indexed=202801, batch_ok=406, batch_retries=0, failed_records=0, venue=90691, address=112110, persec=1530.1
...
```
5. Cherchez des arrêts STIF comme par exemple avec la requête `arrêt bastille`, `arrêt métro créteil université`... 
A noter que dans le flux STIF d'origine, il n'y a pas de préfixe "arrêt", nous les avons ajouté pour faciliter la recherche d'éléments STIF.

### Pour intégrer d'autres données
Il existe beaucoup de fournisseurs offrant des données riches en contenu, bien souvent vous aurez besoin de transformer cette donnée en format OSM. Il existe des outils adaptés à cela comme par exemple ___osmconvert___, qui convertit en plusieurs formats.

N'hésitez pas à vous inspirer d'un outil Python, que Ulrich a codé pour l'occasion et qui m'a permis de convertir la donnée STIF/CSV en STIF/OSM, [disponible ici](https://github.com/ulrich/osm-stif_to_osm).