# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Préparation des images Docker (partie 1/4)
La construction des images Docker de Pelias doit se faire sur une machine robuste, disposant d'une bonne connexion Internet. Deux solutions s'offent à vous : utilisez les images Docker fournies pour le hands-on (conseillé) ou si vous le souhaitez, construisez vous même les images.

### Restauration des images Docker
1. Copier/coller l'archive __devoxx_search_docker_images.tar.gz__ dans le répertoire ~/maps-hands-on/search/installation/docker
```
cp DEVOXX_SUPPORT/search/docker/devoxx_search_docker_images.tar.gz ~/maps-hands-on/search/installation/docker
```
2. Décompresser l'archive
```
gunzip devoxx_search_docker_images.tar.gz
```
3. Restaurer les images docker
```
docker load --input devoxx_search_docker_images.tar
```
Nous sommes prêts à configurer Pelias. Rendez-vous à la partie 2...