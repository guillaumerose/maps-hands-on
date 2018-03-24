# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajout des données dans Pelias (partie 3/4)
Pelias est prêt à recevoir la données __OSM/Paris__.

### Importation des données
1. Copier/coller le fichier des données __OSM/Paris__ dans le répertoire d'Elasticsearch
```
cp DEVOXX_SUPPORT/data/paris.osm.pbf ~/devoxx/search/data/openstreetmap/
```
2. Importer la donnée de __OSM/Paris__ dans __Elasticsearch__
```
docker-compose run --rm openstreetmap npm start
```
3. Tester la présence de données OSM Paris
```
curl http://localhost:4000/v1/search?text=rue%20de%20la%20pompe
```
Youpi, notre service de recherche est prêt à s'intégrer dans notre interface. Rendez-vous à la partie 4...