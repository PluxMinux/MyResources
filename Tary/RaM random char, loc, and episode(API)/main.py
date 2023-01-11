import requests, random


def randomLocation():
    n = random.randint(1,126)
    responseLocation = requests.get("https://rickandmortyapi.com/api/location/"+str(n))
    print(responseLocation.json()["name"])


def randomCharacter():
    n = random.randint(1,826)
    responseCharacter = requests.get("https://rickandmortyapi.com/api/character/"+str(n))
    print(responseCharacter.json()["name"])
    
def randomEpisode():
    n = random.randint(1,51)
    responseEpisode = requests.get("https://rickandmortyapi.com/api/episode/"+str(n))
    print(responseEpisode.json()["name"])


for x in range(5):
    randomLocation()

print("\n")

for y in range(5):
    randomCharacter()

print("\n")
    
for z in range(5):
    randomEpisode()


# #Display in the form of JSON
# import json
# def jprint(obj):
#     # create a formatted string of the Python JSON object
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     #print(text)
#     return text
# print(jprint(response.json()))