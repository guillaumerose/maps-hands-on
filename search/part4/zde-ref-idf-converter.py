#!/usr/bin/python3

import csv

node_id = 0

print('<?xml version="1.0" encoding="UTF-8"?><osm version="0.6" generator="csv2osm">')

with open('zde-ref-idf.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')

    for row in reader:
        node_id = node_id + 1
        geo_point=row['Geo Point'].replace(" ", "").split(",")
        print('<node id="{}" lat="{}" lon="{}">'.format(node_id, geo_point[0], geo_point[1]))
        print('<tag k="{}" v="{}"/>'.format("highway", "bus_stop"))
        print('<tag k="{}" v="{}"/>'.format("amenity", "bus_station"))
        print('<tag k="{}" v="{}"/>'.format("name", "Arrêt STIF " + row['NOM']))
        print('</node>')

print('</osm>')