## Préparation des images Docker
La construction des images Docker de Pelias doit se faire sur une machine robuste. Deux solutions s'offrent à vous : utilisez les images Docker fournies pour le hands-on (conseillé) ou si vous le souhaitez, construisez vous-même les images (voir ci-dessous).

### Construction des images Docker
```
$ cp DEVOXX_SUPPORT/search/docker/devoxx_search_docker_images.tar.gz ~/maps-hands-on/search/installation/docker
$ cd ~/maps-hands-on/search/installation/docker
$ gunzip devoxx_search_docker_images.tar.gz
$ docker load --input devoxx_search_docker_images.tar
```

Nous sommes prêts à configurer Pelias. Rendez-vous à la partie 1.
