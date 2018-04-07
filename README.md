# Reconstruire Google Maps en moins de 3 heures

Dans cet atelier, nous allons assembler les mêmes briques de base que possède Google Maps, y partir de solutions Open Source :
- un plan
- un calcul d'itinéraire
- une fonction de recherche

Cet atelier a besoin de certains fichiers disponibles dans ce repository.

Vous pouvez le cloner à partir de Github, ou, de préférence, copier les fichiers fournis sur une clef USB.

Les instructions supposent que le repository est disponible dans le répertoire `~/maps-hands-on`.

```
$ cd ~
$ git clone https://github.com/guillaumerose/maps-hands-on.git
```

Outils pré-requis :
- __docker__
- __docker-compose__, cf. instructions d'installation [ici](https://docs.docker.com/compose/install/)

Il sera également utile d'avoir les outils suivants, ou leurs équivalents :
- __Python 2__, pour lancer un serveur HTTP
- __curl__, pour appeler les serveurs installés et vérifier que cela marche
- __jq__, pour formatter les fichiers json en ligne de commande

Pour commencer l'atelier, ouvrez le répertoire [plan](plan).
