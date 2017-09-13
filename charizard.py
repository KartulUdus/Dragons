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


    ash['wingStrength'] = ash.pop('agility')
    ash['scaleThickness'] = ash.pop('attack')
    ash['clawSharpness'] = ash.pop('armor')
    ash['fireBreath'] = ash.pop('endurance')

    if 'name' in ash:
        del ash['name']


    stats = heapq.nlargest(4, ash, key=ash.get)

    if weather in ("NMR", "FUNDEFINEDG"):

        ash[stats[0]] += 2
        ash[stats[1]] -= 1
        ash[stats[2]] -= 1

    if weather == "T E":

        ash['wingStrength'] = 5
        ash['scaleThickness'] = 5
        ash['clawSharpness'] = 5
        ash['fireBreath'] = 5

    if weather == "HVA":

        ash['wingStrength'] = 6
        ash['scaleThickness'] = 6
        ash['clawSharpness'] = 8
        ash['fireBreath'] = 0


    charizard = {
        "dragon": ash
    }


    print ("DRAGON: ", charizard)


    print ("DEBUG WEATHER: ", weather)

    return charizard

def potato():

    getGame = requests.get('http://www.dragonsofmugloar.com/api/game').text
    game = json.loads(getGame)
    ash = game['knight']
    id = game['gameId']
    weather = getweather(id)

    print ("===========================")
    if weather['code']=="HVA":
        print ash['endurance']
    print ("KNIGHT:", ash)
#    print ("WEATHER:", weather)
    charizard = trainCharizard(ash, weather['code'])
    if weather['code'] is not "SRO":
        tobattle(charizard, id)
    else:
        print "I WANT TO LIVE!!"



def play():

    count = 400
    for games in range(count):
        potato()



def tobattle(dragon, id):

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard = json.dumps(dragon)
    headers = {"Content-Type": "application/json"}
    result = requests.put(url, data=charizard, headers=headers).content
    print ("RESULT:", result)


if __name__ == "__main__":
    play()
