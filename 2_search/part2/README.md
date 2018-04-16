## Ajout d'un champ de recherche simple
Pour pouvoir interroger notre serveur Pelias, nous allons avoir besoin d'ajouter un champ de saisie et un bouton.

La séquence de traitement est la suivante :
- Interroger la brique Pelias/API sur 127.0.0.1:4000,
- Transformer la réponse JSon de Pelias en __marker__,
- Reserrer la carte sur la zone, qui encadre le POI trouvé.

### Ajout des éléments HTML et script
Pensez à ajouter le code HTML/JS dans le fichier index.html, qui correspond au conteneur plan allumé (part0, part1 ou part2). Pour plus de facilité, nous avons ajouté des marqueurs sous forme de commentaires, dans les fichiers index.html, afin de vous aidez à placer les codes HTML/JS des parties plan, search et route.

1. Copier le code HTML suivant dans le FORM __form-search__ dans le fichier __index.html__
```html
<input id="search" type="input" type="text" placeholder="Rechercher dans OpenStreetMap" name="q" class="form-control mb-2 mr-sm-2"/>
    <button id="search_button" class="btn btn-primary mb-2" type="button">
    <i class="fa fa-search"></i>
</button>
```
2. Copier le code Javascript suivant dans la balise __script__ dans le fichier [index.html](../../1_plan/part0/static/index.html)
```js
var marker = null;
$('#search_button').on('click', function (e) {
    if (marker != null) {
        marker.remove();
    }
    $.getJSON('http://127.0.0.1:4000/v1/search?size=1&text=' + $('#search').val(), function (result) {
        coord = result.features["0"].geometry.coordinates
        var el = document.createElement('div');
        el.className = 'marker';
        marker = new mapboxgl.Marker(el)
                .setLngLat(coord)
                .addTo(map);
        map.fitBounds(new mapboxgl.LngLatBounds(coord, coord), {maxZoom: 15});
    });
    return false;
});
```
Sauvegardez les modifications.

3. Testez quelques requêtes

Le serveur de plan du début de l'atelier devrait être en train de tourner, ainsi que le serveur Pelias.

Il n'est pas nécessaire de redémarrer le serveur de plan, un simple CTRL+R sur la page suffit.
```
tour eiffel
rue de sèvres
quartier république
école maternelle lahire
```

Félicitations ! Vous avez entre les mains un champ de recherche qui repose sur la données OpenStreetMap. Si vous souhaitez le personnaliser, rendez-vous à la [partie bonus](../bonus).