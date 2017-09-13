#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import xmltodict
import heapq



def getweather(id):

    wurl = ('http://www.dragonsofmugloar.com/weather/api/report/' + str(id))
    potato = requests.get(wurl).content
    weather = json.loads(json.dumps(xmltodict.parse(potato)))
    return weather['report']


def trainCharizard(ash, weather):

    if 'name' in ash:
        del ash['name']
    ash['wingStrength'] = ash.pop('agility')
    ash['scaleThickness'] = ash.pop('attack')
    ash['clawSharpness'] = ash.pop('armor')
    ash['fireBreath'] = ash.pop('endurance')

    stats = heapq.nlargest(4, ash, key=ash.get)

    ash[stats[0]] += 2
    ash[stats[1]] -= 1
    ash[stats[2]] -= 1

    charizard = genCharizard(ash)

    print ("DRAGON: ", charizard)
    print ("DEBUG WEATHER: ", weather)

    return charizard

def potato():

    getGame = 'http://www.dragonsofmugloar.com/api/game'
    game = json.loads(requests.get(getGame).content)
    ash = game['knight']
    id = game['gameId']
    weather = getweather(id)

    print ("=========================== GAME: ",game)
    print ("KNIGHT:", ash)
    print ("WEATHER:", weather)

    charizard = trainCharizard(ash, weather)
    tobattle(charizard, id)

    exit(1)

def play():

    count = 4
    for games in range(count):
        potato()



def tobattle(dragon, id):

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard = json.dumps(dragon)
    headers = {"Content-Type": "application/json"}
    result = requests.put(url, data=charizard, headers=headers).content
    print ("RESULT:", result)


def genCharizard(dragon):

    charizard = {
        "dragon": dragon
    }
    return charizard


if __name__ == "__main__":
    potato()
