# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajouter un champ de recherche

Pour préparer le hands-on, nous allons récupérer les sources sur github et détailler la structure du projet.

Récupérer les sources sur github
```
git clone https://github.com/guillaumerose/maps-hands-on.git ~/maps-hands-on
```
Placez-vous dans le répertoire __search__ et listez le. La structure se décompose ainsi :
```
- installation : contient la configuration Docker, Pelias et les données,
- part0 : partie initialisation des services Docker,
- part1 : partie initialisation des services Pelias,
- part2 : partie importation des données OpenStreetMap,
- part3 : partie intégration du champ de recherche sur la carte,
- part4 : partie intégration de données tierces (STIF).
```
