# Mise en place du plan
Placez-vous dans ce répertoire et listez-le. La structure se décompose ainsi :
- [part0](./part0) : initialisation du serveur de plan,
- [part1](./part1) : personnalisation,
- tileserver-gl.tar.gz : serveur de plan
- data : repertoire contenant la donnée idf

## Démarrage sans connexion internet
vous pouvez charger le serveur de plan directement depuis le fichier tileserver-gl.tar.gz
```
docker load < tileserver-gl.tar.gz
```

### Déroulement de la partie Plan
La partie part0 est le minimum pour intégrer un plan. Si vous souhaitez le personnaliser, vous pouvez vous inspirer de la partie part1, qui ajoute un _layer_ avec des Poi.
