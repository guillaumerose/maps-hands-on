## Configuration de Pelias
Pour fonctionner a minima, Pelias a besoin d'allumer deux conteneurs : le conteneur ElasticSearch et le conteneur API, qui a en charge d'orchestrer les requêtes utilisateurs.

### Préparation des assets et lancement des services
1. Cloner le projet Pelias Dockerfiles dans ~/maps-hands-on/search/
```
git clone https://github.com/pelias/dockerfiles.git ~/maps-hands-on/search/installation/pelias
```
2. Faire pointer la variable __DATA_DIR__ dans le fichier __.env__ sur le répertoire de données
```
$ cd ~/maps-hands-on/search/installation/pelias
$ vi .env
...
$ cat .env
DATA_DIR=~/maps-hands-on/search/installation/data
```
3. Allumer le conteneur __ElasticSearch__
```
docker-compose up -d elasticsearch
```
4. Créer le schéma __ElasticSearch__ qui va contenir les points d'intérêt, rues, etc.
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
curl http://localhost:4000/v1/search?text=pharmacie | jq
```
Cool, nous avons un serveur opérationnel mais pas encore de données ! Rendez-vous à la partie 2.
