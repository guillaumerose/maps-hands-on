# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajouter un champ de recherche

Pour préparer le hands-on, nous allons récupérer les sources sur github et détailler la structure du projet.

Récupérer les sources sur github
```
git clone https://github.com/guillaumerose/maps-hands-on.git ~/maps-hands-on
```
Placez-vous dans le répertoire __search__ et listez le. La structure se décompose ainsi :
```
drwxrwxr-x 4 you you 4,0K mars  01 00:00 installation/
  +--drwxrwxr-x 3 you you 4,0K mars  01 00:00 data/
  +--drwxrwxr-x 2 you you 4,0K mars  01 00:00 docker/
drwxrwxr-x 2 you you 4,0K mars  01 00:00 part0/
  +--rw-rw-r-- 1 you you 1,1K mars  01 00:00 README.md
drwxrwxr-x 2 you you 4,0K mars  01 00:00 part1/
  +--rw-rw-r-- 1 you you 1,1K mars  00 00:00 README.md
drwxrwxr-x 2 you you 4,0K mars  01 00:00 part2/
  +--rw-rw-r-- 1 you you 1,1K mars  01 00:00 README.md
drwxrwxr-x 2 you you 4,0K mars  01 00:00 part3/
  +--rw-rw-r-- 1 you you 1,1K mars  01 00:00 README.md
-rw-rw-r-- 1 you ulrich  202 mars  01 00:00 README.md
```
- installation : contient la configuration Docker, Pelias et les données,
- part0 : partie initialisation des services Docker,
- part1 : partie initialisation des services Pelias,
- part2 : partie importation des données OpenStreetMap,
- part3 : partie intégration du champ de recherche sur la carte,
