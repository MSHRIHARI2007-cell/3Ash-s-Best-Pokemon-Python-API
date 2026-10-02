from cfonts import render
import requests
output = render("Pokemon API", font="block")
print(output)


pokemon ={"pikachu":"https://pokeapi.co/api/v2/","charizard":"https://pokeapi.co/api/v2/","greninja":"https://pokeapi.co/api/v2/"}


def get_pokemon_info(name):
    url=pokemon[name]
    response=requests.get(url)

    if (response.status_code == 200):
        pokemon_data=response.json()
        print(pokemon_data)
    else:
        print(f"Failed tp retrieve data {response.status_code}")

print("Available Pokemon:",pokemon.keys())
pokemon_name=input("Enter Pokemon name:").lower()
if pokemon_name in pokemon:
    get_pokemon_info(pokemon_name)
else:
    print("pokemon not found!")
