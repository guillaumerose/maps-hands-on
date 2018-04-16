# Mise en place du plan
Placez-vous dans ce répertoire. La structure se décompose ainsi :
- [part0](./part0) : initialisation du serveur de plan
- [part1](./part1) : vérification
- [part2](./part2) : personnalisation
- data : répertoire qui contiendra la donnée idf

## Démarrage sans connexion internet
Vous devriez trouver le fichier `devoxx_plan_docker_images.tar.gz` sur la clef USB. C'est l'image Docker du serveur de plan. Chargez-le.
```
$ cd ~/DEVOXX_SUPPORT/plan/docker

$ docker load < devoxx_plan_docker_images.tar.gz
```

## Pour aller plus loin
Si vous souhaitez enrichir le plan avec vos données personnelles, vous pouvez vous inspirer de la partie part1, qui ajoute un _layer_ avec des points d'intérêt (cf. le fichier `static/lbc.json`).