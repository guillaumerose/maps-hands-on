## Ajout d'un champ de recherche simple
Avant de nous intégrer sur la carte finale, nous allons interroger notre serveur Pelias au moyen d'une simple page HTML de test.

La séquence de traitement est la suivante :
- Interroger le serveur Pelias, qui délèguera à ElasticSearch le traitement de la requête,
- Transformer la réponse JSon de Pelias en __marker__ sur la carte,
- Reserrer la carte sur la zone, qui encadre l'ensemble des POIs.

A noter que les marqueurs sont cliquables afin d'en connaitre l'identité.

### Test rapide du serveur Pelias
1. Déplacez-vous dans le répertoire de la partie 3
```
$ cd ~/maps-hands-on/search/part3
```
2. Lancez un serveur HTTP _via_ une commande Python
```
Pour Python 2
$ python -m SimpleHTTPServer 8000

Pour Python 3
$ python3 -m http.server 8000
```
3. Testez quelques requêtes
```
rue de sèvres
```
Utilisez le slider afin d'être plus ou moins permissif sur ranking des résultats retournés.
Par exemple, la recherche du terme "pharmacie montparnasse" retourne beaucoup de POI, utilisez le slider pour affiner pour votre recherche.

Félicitations ! Vous avez entre les mains un champ de recherche qui repose sur la données OpenStreetMap. Si vous souhaitez le personnaliser, rendez-vous à la [partie 4](https://github.com/guillaumerose/maps-hands-on/tree/master/search/part4).