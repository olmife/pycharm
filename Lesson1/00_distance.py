#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расссеткетояний между ними
# # расстояние на координатной  - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moskow = sites['Moscow']
london= sites['London']
paris= sites['Paris']
moskow_london = ((moskow[0]-london[0])**2 + (moskow[1]-london[1])**2)**0.5
moskow_paris = ((moskow[0]-paris[0])**2 + (moskow[1]-paris[1])**2)**0.5
london_paris = ((london[0]-paris[0])**2 + (london[1]-paris[1])**2)**0.5


distances= dict()
distances['Moskow']= {}
distances['Moskow']["London"]= moskow_london
distances["Moskow"]["Paris"]= moskow_paris
distances['London']= {}
distances['London'] ['Paris'] = london_paris
distances['London']['Moskow'] = moskow_london
distances['Paris']= {}
distances['Paris']['Moskow'] = moskow_paris
distances['Paris']['London'] = london_paris
pprint(distances)



