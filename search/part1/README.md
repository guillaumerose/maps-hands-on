# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Configuration de Pelias (partie 2/4)
Pour fonctionner à minimum, Pelias a besoin d'allumer deux conteneurs : le conteneur ElasticSearch et le conteneur API, qui a en charge d'orchestrer les requêtes utilisateurs.

### Préparation des assets et lancement des services
1. Créer le répertoire des données
```
mkdir -p ~/maps-hands-on/search/data
```
2. Faire pointer la variable __DATA_DIR__ dans le fichier __.env__ sur le répertoire de données
```
DATA_DIR=~/maps-hands-on/search/data
```
3. Allumer le conteneur __ElasticSearch__
```
docker-compose up -d elasticsearch
```
4. Créer le schéma __ElasticSearch__
```
docker-compose run --rm schema npm run create_index
```
5. Allumer le conteneur __API__
```
docker-compose up -d api
```
6. Faire un état des lieux des conteneurs en cours
```
docker-compose ps
```
7. Tester la présence de Pelias
```
curl http://localhost:4000/v1/search?text=pharmacie
```
Cool, nous avons un serveur opérationnel mais sans données ! Rendez-vous à la partie 3...