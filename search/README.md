# Reconstruire Google Maps en moins de 3 heures (Devoxx France 2018)

## Ajouter un champ de recherche

Pour préparer le hands-on, nous allons récupérer les sources sur github et détailler la structure du projet.

Récupérer les sources sur github
```
git clone https://github.com/maps-hands-on/maps-hands-on/
```
Placez-vous dans le répertoire __search__ et listez le. La structure se décompose ainsi :
```
drwxrwxr-x 4 ulrich ulrich 4,0K mars  25 00:44 installation/
  +--rw-rw-r-- 1 ulrich ulrich 3,8K mars  24 15:41 docker-compose.yml
  +-drwxrwxr-x 4 ulrich ulrich 4,0K mars  25 00:18 elasticsearch/
  +--rw-rw-r-- 1 ulrich ulrich   10 mars  25 00:44 .env
  +-drwxrwxr-x 2 ulrich ulrich 4,0K mars  25 00:18 libpostal_baseimage/
  +--rw-rw-r-- 1 ulrich ulrich  616 mars  25 00:21 pelias.json
drwxrwxr-x 2 ulrich ulrich 4,0K mars  24 14:00 part0/
  +--rw-rw-r-- 1 ulrich ulrich 1,1K mars  25 00:16 README.md
drwxrwxr-x 2 ulrich ulrich 4,0K mars  25 00:59 part1/
  +--rw-rw-r-- 1 ulrich ulrich 1,1K mars  25 00:16 README.md
drwxrwxr-x 2 ulrich ulrich 4,0K mars  25 00:59 part2/
  +--rw-rw-r-- 1 ulrich ulrich 1,1K mars  25 00:16 README.md
-rw-rw-r-- 1 ulrich ulrich  202 mars  25 12:14 README.md
```
- installation : contient la configuration Docker et Pelias,
- part0 : partie initialisation des services Docker,
- part1 : partie initialisation des services Pelias,
- part2 : partie importation des données OpenStreetMap,
