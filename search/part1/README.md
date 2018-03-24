# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Configuration de Pelias (partie 2/4)
Pour fonctionner à minimum, Pelias a besoin d'allumer deux conteneurs : le conteneur ElasticSearch et le conteneur API, qui a en charge d'orchestrer les requêtes utilisateurs.

### Restauration des images Docker

1. Créer le répertoire contenant la donnée __Paris__
```
mkdir -p ~/devoxx/search/data
```
2. Faire pointer la variable d'environnement dans le fichier __.env__
```
DATA_DIR=~/devoxx/search/data
```
3. Copier/coller le fichier __paris.osm.pbf__
```
cp DEVOXX_SUPPORT/data/paris.osm.pbf ~/devoxx/search/data
```
4. Allumer le conteneur __Elasticsearch__
```
docker-compose up -d elasticsearch
```
5. Créer le schéma __Elasticsearch__
```
docker-compose run --rm schema npm run create_index
```
5. Allumer le conteneur __API__
```
docker-compose up -d api
```
6. Tester la présence de Pelias
```
curl http://localhost:4000/v1/search?text=pharmacie
```
Cool, nous avons un serveur opérationnel mais sans données ! Rendez-vous à la partie 3...