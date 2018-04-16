## Ajout des données dans Pelias
Pelias est prêt à recevoir les données OSM/Paris.

### Importation des données
1. Copier/coller le fichier des données OSM/Paris dans le répertoire d'ElasticSearch
```shell
cp ~/DEVOXX_SUPPORT/search/data/osm/paris.osm.pbf ~/maps-hands-on/2_search/installation/data/openstreetmap/
```
2. Modifier la configuration de _l'importer_ OpenStreetMap dans le fichier __pelias.json__ pour pouvoir utiliser la donnée Paris
```shell
sed -i -e 's/portland_oregon.osm.pbf/paris.osm.pbf/g' pelias.json
```
3. Importer les données OSM/Paris dans ElasticSearch.
Cette étape nécessite un minimum de RAM, si vous rencontrez des erreurs pendant l'importation des données, n'hésitez pas à augmenter la mémoire allouée. Dans le cas contraire, laisser _l'importer_ terminer son traitement. Ce dernier relancera un traitement tout seul en cas d'echec.
```shell
docker-compose run --rm openstreetmap npm start
```
Certains logs d'erreurs indiquent que _l'importer_ ne peut importer la données [Who's On First](https://github.com/whosonfirst-data/whosonfirst-data), ce qui est normal, car nous ne l'avons pas prévu dans cet atelier. De plus, _l'importer_ indique qu'il rencontre des difficultés lors de l'analyse de certaines adresses, il ne faudra pas en tenir compte sachant que cela représente une part infime des rue (ways) intégrées (142 échecs pour 112 110 importations).

4. Tester la présence d'un POI (_Points of Interest_)
```shell
curl http://localhost:4000/v1/search?text=pharmacie | jq
```
5. Tester la présence d'une adresse
```shell
curl http://localhost:4000/v1/search?text=rue%20lecourbe | jq
```
Notre service de recherche est prêt à s'intégrer dans notre interface. Rendez-vous à la [partie 2](../part2).