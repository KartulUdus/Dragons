#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
import requests
import xmltodict
import heapq

getGame = 'http://www.dragonsofmugloar.com/api/game'

def getweather(id):

    wurl=('http://www.dragonsofmugloar.com/weather/api/report/'+str(id))
    potato = requests.get(wurl).content
    weather = json.loads(json.dumps(xmltodict.parse(potato)))
    return weather['report']



def potato():

    game = json.load(urllib2.urlopen(getGame))
    ash = game['knight']
    id = game['gameId']

    if 'name' in ash:
        del ash['name']
    print "==========================="
    print ("KNIGHT:",ash)
    print ("WEATHER:",getweather(id)['code'])

    ash['wingStrength'] = ash.pop('agility')
    ash['scaleThickness'] = ash.pop('attack')
    ash['clawSharpness'] = ash.pop('armor')
    ash['fireBreath'] = ash.pop('endurance')

    stats = heapq.nlargest(4, ash, key=ash.get)

    ash[stats[0]] +=2
    ash[stats[1]] -=1
    ash[stats[2]] -=1


    if (getweather(id)['code']=='NMR'):
        charizard = genCharizard(ash)
        print ("DRAGON:",charizard['dragon'])
        tobattle(charizard,id)
    else:
        print "The weather is not nice, i'd rather stay home"

def play():

    count=40
    for games in range(count):
        potato()


def tobattle (dragon, id):

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard=json.dumps(dragon)
    headers = {"Content-Type": "application/json"}
    result=requests.put(url,data=charizard,headers=headers).content
    print ("RESULT:",json.loads(result))

def genCharizard(dragon):

    charizard = {
        "dragon": dragon
    }
    return charizard

if __name__ == "__main__":
  play()
