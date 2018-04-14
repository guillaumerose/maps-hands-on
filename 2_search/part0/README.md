## Configuration de Docker
La construction des images Docker de Pelias doit se faire sur une machine robuste. Ainsi, deux solutions s'offrent à vous : utilisez les images Docker fournies pour le hands-on et les importer sur votre machine (conseillé) ou si vous le souhaitez, construisez vous-même les images ([Pelias how to guide](https://pelias.io/install.html)).

### Importer les images Docker
```
$ cp DEVOXX_SUPPORT/search/docker/devoxx_search_docker_images.tar.gz ~/maps-hands-on/search/installation/docker
```
```
$ cd ~/maps-hands-on/search/installation/docker
```
```
$ docker load --input devoxx_search_docker_images.tar.gz
```

## Configuration de Pelias
Pour fonctionner a minima, Pelias a besoin d'allumer deux conteneurs : le conteneur ElasticSearch et le conteneur API, qui a en charge d'orchestrer les requêtes utilisateurs.

### Préparation des assets et lancement des services
1. Cloner le projet Pelias Dockerfiles dans ~/maps-hands-on/search/
```
git clone https://github.com/pelias/dockerfiles.git ~/maps-hands-on/search/installation/pelias
```
2. Déplacez-vous dans le répertoire de Pelias
```
$ cd ~/maps-hands-on/search/installation/pelias
```
3. Faire pointer la variable __DATA_DIR__ dans le fichier __.env__ sur le répertoire de données
```
$ echo DATA_DIR=~/maps-hands-on/search/installation/data > .env
```
4. Allumer le conteneur __ElasticSearch__
```
docker-compose up -d elasticsearch
```
5. Créer le schéma __ElasticSearch__ qui va contenir les points d'intérêt, rues, etc.
```
docker-compose run --rm schema npm run create_index
```
6. Allumer le conteneur __API__
```
docker-compose up -d api
```
7. Faire un état des lieux des conteneurs en cours
```
docker-compose ps
```
8. Tester la présence de Pelias
```
curl http://localhost:4000/v1/search?text=pharmacie | jq
```
Nous avons un serveur opérationnel, mais pas encore de données ! Rendez-vous à la [partie 1](../part1).