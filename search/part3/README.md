## Ajout d'un champ de recherche simple (partie 3/4)
En ajoutant un simple champ de recherche en overlay sur la carte, nous sommes en mesure d'interroger Pelias. La séquence de traitement est la suivante :
- Interroger le serveur Pelias, qui délèguera à ElasticSearch le traitement de la requête,
- Transformer la réponse JSon de Pelias en __marker__ sur la carte,
- Reserrer la carte sur la zone, qui encadre l'ensemble des POIs.

A noter que les marqueurs sont cliquables afin d'en connaitre l'identité.

### Quelques tests d'abord
1. Lancez la commande suivante pour tester le parsing des résultats
```
python -m SimpleHTTPServer 8000
```
2. Procéder à quelques reqêtes (pharmacie, rue de vaugirard)
```
rue de sèvres
rue de sevre
pharmacie
...
```
### Intégration dans le partie __plan__
1. Copier/coller les fonctions suivantes dans la page HTML de plan
```
exec, clearMap, search, render et updateMap
```
2. Binding du champ et bouton de recherche sur la fonction exec()
```
Inspirez vous de la méthode précédente en attachant les fonctions avec JQuery par exemple.
...
```
Félicications ! Vous avez entre les mains un champ de recherche qui repose sur la données OpenStreetMap. Si vous en avez envi, rendez-vous à la partie 4 pour voir comment le personnaliser...
