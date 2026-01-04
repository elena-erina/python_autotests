import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'trainer_token'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemon_created = {
    "name": "Panita",
    "photo_id": 333
}

body_put_pokemon = {
    "pokemon_id": "1017408",
    "name": "Ulitik",
    "photo_id": 400
}

body_add_pokeball = {
    "pokemon_id": "1032009"
}


'''response = requests.post(url=f'{URL}/pokemons', headers = HEADER, json = body_pokemon_created)
print(response.text)'''

'''response_put_pokemon = requests.put(url=f'{URL}/pokemons', headers = HEADER, json = body_put_pokemon)
print(response_put_pokemon.text)'''

response_add_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)


