from cfonts import render
import requests

#title
output = render("Pokemon API", font="block")
print(output)

#data
pokemons={
    "pikachu":"https://pokeapi.co/api/v2/pokemon/pikachu",
    "charizard":"https://pokeapi.co/api/v2/pokemon/charizard",
    "greninja":"https://pokeapi.co/api/v2/pokemon/greninja"
   }

#info
def get_pokemon_info(name):
    url=pokemons[name]
    response=requests.get(url)

    if response.status_code==200:
        pokemon_data=response.json()
        return (
            f"Name:{pokemon_data.get('name')}\n"
            f"ID:{pokemon_data.get('id')}\n"
            f"Height:{pokemon_data.get('height')}\n"
            f"Weight:{pokemon_data.get('weight')}"
        )
    else:
        return f"Failed to retrieve data->Status code: {response.status_code}"

#display
print("Available Pokemon:",pokemons.keys())
pokemon_name=input("Enter Pokemon name: ").lower()

if pokemon_name:
    res=get_pokemon_info(pokemon_name)
    print(res)
else:
    print("Not allowed")
