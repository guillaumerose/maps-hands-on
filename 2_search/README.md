# Ajouter un champ de recherche
Placez-vous dans le répertoire __search__ et listez-le. La structure se décompose ainsi :
- [part0](./part0) : initialisation des services Docker et Pelias,
- [part1](./part1) : importation des données OpenStreetMap,
- [part2](./part2) : intégration du champ de recherche sur la carte,
- [bonus](./bonus) : intégration de données tierces (STIF).

### Déroulement de la partie Search
Les parties part0 à part2 sont les étapes minimums pour intégrer un champ de rechercher à notre carte. Si vous souhaitez personnaliser votre moteur de recherche, vous pouvez vous inspirer de la partie bonus, qui permet l'ajout de donnée tierce comme les données du STIF (ensemble des zones d'embarquements en IDF).

### Préparation du répertoire des assets
Nous travaillerons dans un répertoire situé dans les sources du projet. Créer les répertoires suivant :
```
mkdir -p ~/maps-hands-on/search/installation/data/openstreetmap
```
```
mkdir ~/maps-hands-on/search/installation/docker
```