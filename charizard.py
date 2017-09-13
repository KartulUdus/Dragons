#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import xmltodict
import heapq


def getweather(id):

    # Return weather for the game

    wurl = ('http://www.dragonsofmugloar.com/weather/api/report/' + str(id))
    potato = requests.get(wurl).content
    weather = json.loads(json.dumps(xmltodict.parse(potato)))
    return weather['report']


def trainCharizard(ash, weather):

    # Train Charizard to cope with the weather

    ash['wingStrength'] = ash.pop('agility')
    ash['scaleThickness'] = ash.pop('attack')
    ash['clawSharpness'] = ash.pop('armor')
    ash['fireBreath'] = ash.pop('endurance')

    if 'name' in ash:
        del ash['name']

    stats = heapq.nlargest(4, ash, key=ash.get)

    if weather in ("NMR", "FUNDEFINEDG"):

        ash[stats[0]] += 2
        ash[stats[1]] -= 2

    if weather == "T E":

        for skill in ash:
            ash[skill] = 5

    if weather == "HVA":

        ash['wingStrength'] = 5
        ash['scaleThickness'] = 5
        ash['clawSharpness'] = 10
        ash['fireBreath'] = 0

    charizard = {
        "dragon": ash
    }

    print "DRAGON: ", str(charizard)
    print "WEATHER: ", str(weather)
    return charizard


def potato():

    # Do all the things in the right order

    getGame = requests.get('http://www.dragonsofmugloar.com/api/game').text
    game = json.loads(getGame)
    ash = game['knight']
    id = game['gameId']
    weather = getweather(id)

    print ("====================", id, "====================")
    print "KNIGHT:", str(ash)
    charizard = trainCharizard(ash, weather['code'])
    if weather['code'] != "SRO":
        tobattle(charizard, id)
    else:
        print "RESULT:",\
            {"status": "Victory", "message": "Knight died in the storm"
             " while dragon stayed home"}


def play():

    # Poser with the purpose of looping potato

    count = 400
    for games in range(count):
        potato()


def tobattle(dragon, id):

    # send the trained charizard to battle

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard = json.dumps(dragon)
    headers = {"Content-Type": "application/json"}
    result = requests.put(url, data=charizard, headers=headers).content
    print ("RESULT:", result)


if __name__ == "__main__":
    play()
