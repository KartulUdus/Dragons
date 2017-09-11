#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
import requests
import xmltodict
import heapq
getGame = 'http://www.dragonsofmugloar.com/api/game'

def Weather(id):

    wurl=('http://www.dragonsofmugloar.com/weather/api/report/'+str(id))
    potato = requests.get(wurl).content
    weather = json.loads(json.dumps(xmltodict.parse(potato)))
    print weather['report']



def potato():

    game = json.load(urllib2.urlopen(getGame))
    ash = game['knight']
    id = game['gameId']

    statsg=['attack','armor','agility','endurance']
    for row in statsg:
        print row
    if 'name' in ash:
        del ash['name']


    ash['clawSharpness'] = ash.pop('armor')
    ash['scaleThickness'] = ash.pop('attack')
    ash['wingStrength'] = ash.pop('endurance')
    ash['fireBreath'] = ash.pop('agility')
    print ash
    stats = heapq.nlargest(4, ash, key=ash.get)
    print stats
    ash[stats[0]] +=1
    ash[stats[1]] += 1
    ash[stats[2]] -= 2


    print ash
    charizard = genCharizard(ash)
    print charizard


    tobattle(charizard,id)

def tobattle (dragon, id):

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard=json.dumps(dragon)
    print charizard
    headers = {"Content-Type": "application/json"}
    result=requests.put(url,data=charizard,headers=headers).content
    print result

def genCharizard(dragon):

    charizard = {
        "dragon": dragon
    }
    return charizard

if __name__ == "__main__":
  potato()
