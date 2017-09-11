#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import urllib2
import requests
import xmltodict
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

    stats=['attack','armor','agility','endurance']
    for row in stats:
        print row
    if 'name' in ash:
        del ash['name']
    bestcal=max(ash.values())
    result = filter(lambda x: x[1] == bestcal, ash.items())

    print result


    print ash , id
#    charizard= genCharizard(
#               ash['attack'],
#               ash['armor'],
#                ash['agility'],
#               ash['endurance'])
#    tobattle(charizard,id)

def tobattle (dragon, id):

    url = 'http://www.dragonsofmugloar.com/api/game/' + str(id) + '/solution'
    charizard=json.dumps(dragon)
    print charizard
    headers = {"Content-Type": "application/json"}
    result=requests.put(url,data=charizard,headers=headers).content
    print result

def genCharizard(thick,sharp,strength,fire):

    charizard = {
        "dragon": {
            "scaleThickness": thick,
            "clawSharpness": sharp,
            "wingStrength": strength,
            "fireBreath": fire
        }
    }
    return charizard

if __name__ == "__main__":
  potato()
