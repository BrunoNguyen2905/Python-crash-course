import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data.get('name', [])
    else:
        print(f"Pokemon {pokemon_name} not found.")
        return None


print(get_pokemon_info("pikachu"))
