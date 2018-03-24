# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajout des données dans Pelias (partie 3/4)
Pelias est prêt à recevoir les données __OSM/Paris__.

### Importation des données
1. Créer le répertoire de données __OpenStreetMap__
```
mkdir -p ~/maps-hands-on/search/installation/data/openstreetmap
```
2. Copier/coller le fichier des données __OSM/Paris__ dans le répertoire d'Elasticsearch
```
cp DEVOXX_SUPPORT/data/paris.osm.pbf ~/maps-hands-on/search/installation/data/openstreetmap
```
3. Importer les données __OSM/Paris__ dans __ElasticSearch__
```
docker-compose run --rm openstreetmap npm start
```
4. Tester la présence de __Poi__
```
curl http://localhost:4000/v1/search?text=pharmacie
```
5. Tester la présence __d'une adresse__
```
curl http://localhost:4000/v1/search?text=rue%20de%20la%20pompe
```
Youpi, notre service de recherche est prêt à s'intégrer dans notre interface. Rendez-vous à la partie 4...