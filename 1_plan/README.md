# Mise en place du plan
Placez-vous dans ce répertoire. La structure se décompose ainsi :
- [part0](./part0) : initialisation du serveur de plan
- [part1](./part1) : vérification
- [part2](./part2) : personnalisation
- tileserver-gl.tar.gz : serveur de plan
- data : répertoire qui contiendra la donnée idf

## Démarrage sans connexion internet
Vous pouvez charger le serveur de plan directement depuis le fichier tileserver-gl.tar.gz
```
docker load < tileserver-gl.tar.gz
```

## Pour aller plus loin
Si vous souhaitez enrichir le plan avec vos données personnelles, vous pouvez vous inspirer de la partie part1, qui ajoute un _layer_ avec des points d'intérêt (cf. le fichier `static/lbc.json`).
