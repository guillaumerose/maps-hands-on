## Ajout des données dans Pelias (partie 2/4)
Pelias est prêt à recevoir les données __OSM/Paris__.

### Importation des données
1. Copier/coller le fichier des données __OSM/Paris__ dans le répertoire d'ElasticSearch
```
cp DEVOXX_SUPPORT/search/data/osm/paris.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap/
```
2. Modifier la configuration de __l'importer__ OpenStreetMap dans le fichier __pelias.json__ pour pouvoir utiliser la données __Paris__

Remplacer la référence au fichier `portland_oregon.osm.pbf` par `paris.osm.pbf` dans le noeud "imports.openstreetmap.import.filename". Inutile de modifier le noeud "imports.openstreetmap.download.sourceURL".

3. Importer les données __OSM/Paris__ dans __ElasticSearch__
```
docker-compose run --rm openstreetmap npm start
```
4. Tester la présence de __POI__ (_Points of Interest_)
```
curl http://localhost:4000/v1/search?text=pharmacie | jq
```
5. Tester la présence __d'une adresse__
```
curl http://localhost:4000/v1/search?text=rue%20lecourbe | jq
```
Youpi ! Notre service de recherche est prêt à s'intégrer dans notre interface. Rendez-vous à la partie 3...
