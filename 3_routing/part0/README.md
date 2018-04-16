## Setup Docker

Les images Docker sont disponibles sur __DEVOXX_SUPPORT__, mais si vous préférez les construire vous-même, vous pouvez les récupérer avec les commandes Docker suivantes.

### Importer les images Docker
```
$ cd ~/DEVOXX_SUPPORT/route/docker

$ docker load --input devoxx_route_docker_images.tar.gz
```

### Construire les images Docker
```
$ docker pull osrm/osrm-backend # Open Source Routing Machine

$ docker pull guillaumerose/osmosis # application Java pour manipuler les données OpenStreetMap
```

Le fichier `Dockerfile` de la deuxième image est visible [ici](../tech/osmosis/Dockerfile).