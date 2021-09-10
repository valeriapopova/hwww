from pprint import pprint

import requests

TOKEN = '2619421814940190'
urls = [
    'https://superheroapi.com/api/2619421814940190/search/Hulk',
    'https://superheroapi.com/api/2619421814940190/search/Captain%America',
    'https://superheroapi.com/api/2619421814940190/search/Thanos',
]

def information():
    info = []
    for url in urls:
        response = requests.get(url)
        info.append(response.json())
    return info

# pprint(information())


def brain_test():
    heroes = []
    for item in information():
        for powerstat in item['results']:
            heroes.append({
                'name': powerstat['name'],
                'intelligence': powerstat['powerstats']['intelligence'],
            })

    intelligence_ = 0
    name = ''
    for intelligence_hero in heroes:
        if intelligence_ < int(intelligence_hero['intelligence']):
            intelligence_ = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f'{name} самый умный супергерой,его интеллект: {intelligence_}')


brain_test()
