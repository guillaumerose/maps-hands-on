## Préparation des images Docker
La construction des images Docker de Pelias doit se faire sur une machine robuste. Ainsi, deux solutions s'offrent à vous : utilisez les images Docker fournies pour le hands-on et les importer sur votre machine (conseillé) ou si vous le souhaitez, construisez vous-même les images ([Pelias how to guide](https://pelias.io/install.html)).

### Importer les images Docker
```
$ cp DEVOXX_SUPPORT/search/docker/devoxx_search_docker_images.tar.gz ~/maps-hands-on/search/installation/docker
```
```
$ cd ~/maps-hands-on/search/installation/docker
```
```
$ gunzip devoxx_search_docker_images.tar.gz
```
```
$ docker load --input devoxx_search_docker_images.tar
```

Nous sommes prêts à configurer Pelias. Rendez-vous à la [partie 1](https://github.com/guillaumerose/maps-hands-on/tree/master/search/part1).
