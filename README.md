# Reconstruire Google Maps en moins de 3 heures

Dans cet atelier, nous allons assembler les mêmes briques de base que possède Google Maps, à partir de solutions Open Source :
- un plan,
- un calcul d'itinéraire,
- une fonction de recherche.

Cet atelier a besoin de certains fichiers disponibles dans ce repository et des images pré-construites disponibles en téléchargement : [DEVOXX_SUPPORT](https://drive.google.com/file/d/1gSWROd8-mElJ8OgP61UwHPeawdsp8Vhn/view?usp=sharing)

Vous pouvez clôner de projet.

Les instructions supposent que le repository du hand-on est disponible dans le répertoire `~/maps-hands-on` et que les fichiers de données et images Docker pré-construites ont été décompressés dans `~/DEVOXX_SUPPORT`.

```
$ cd ~
$ git clone https://github.com/guillaumerose/maps-hands-on.git
```

Outils pré-requis :
- __docker__
- __docker-compose__, (version 1.20 minimum) cf. instructions d'installation [ici](https://docs.docker.com/compose/install/)

Il sera également utile d'avoir les outils suivants, ou leurs équivalents :
- __curl__, pour appeler les serveurs installés et vérifier que cela marche
- __jq__, pour formatter les fichiers json en ligne de commande

Pour commencer l'atelier, ouvrez le répertoire [plan](1_plan).
