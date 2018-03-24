# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Préparation des images Docker (partie 1/4)
La construction des assets Pelias doit se faire sur une machine robuste, disposant d'une bonne connection Internet. Deux solutions s'offent à vous : utilisez les images Docker fournies pour le hands-on (conseillé) ou si vous le souhaitez, construisez vous même les images.

### Restauration des images Docker
1. Créer le répertoire contenant les conteneurs
```
mkdir -p ~/devoxx/search/docker
```
2. Copier/coller l'archive devoxx_search_docker_images.tar dans le répertoir docker
```
cp DEVOXX_SUPPORT/docker/devoxx_search_docker_images.tar.gz ~/devoxx/search/docker
```
3. Décompresser l'archive
```
gunzip devoxx_search_docker_images.tar.gz
```
4. Restaurer les images docker
```
docker load --input devoxx_search_docker_images.tar
```
Nous sommes prêts à configurer Pelias, rendez-vous à la partie 2...

### Création des images Docker 
1. Créer le répertoire contenant les conteneurs
```
mkdir -p ~/devoxx/search/docker
```
...