## Ajout des données dans Pelias
Pelias est prêt à recevoir les données OSM/Paris.

### Importation des données
1. Copier/coller le fichier des données OSM/Paris dans le répertoire d'ElasticSearch
```
cp DEVOXX_SUPPORT/search/data/osm/paris.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap/
```
2. Modifier la configuration de _l'importer_ OpenStreetMap dans le fichier __pelias.json__ pour pouvoir utiliser la données Paris
```
sed -i -e 's/portland_oregon.osm.pbf/paris.osm.pbf/g' pelias.json
```
3. Importer les données OSM/Paris dans ElasticSearch. Cette étape nécessite un minum de RAM, si vous rencontrer des erreurs pendant l'importation des données, n'hésitez pas à augmenter la mémoire allouée. Dans le cas contraire, laisser _l'importer_ terminer son traitement. Ce dernier se relancera tout seul en cas d'echec.
```
docker-compose run --rm openstreetmap npm start
```
4. Tester la présence d'un POI (_Points of Interest_)
```
curl http://localhost:4000/v1/search?text=pharmacie | jq
```
5. Tester la présence d'une adresse
```
curl http://localhost:4000/v1/search?text=rue%20lecourbe | jq
```
Notre service de recherche est prêt à s'intégrer dans notre interface. Rendez-vous à la [partie 3](https://github.com/guillaumerose/maps-hands-on/tree/master/search/part3).