  import requests
from typing import List, Optional, Dict, Any

def fetch_data(url: str) -> Optional[Dict[str, Any]]:
    """
    Makes a GET request to the provided URL and returns the JSON data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Return the JSON content if request was successful
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_water_type_url() -> Optional[str]:
    """
    Retrieves the URL for the 'Water' type Pokémon from the PokeAPI.
    """
    url = "https://pokeapi.co/api/v2/type/"
    data = fetch_data(url)
    if data:
        # Look through the list of types to find 'water'
        for type_info in data.get('results', []):
            if type_info['name'].lower() == 'water':
                return type_info['url']
    return None

def fetch_water_pokemons() -> List[str]:
    """
    Fetches the list of all Water-type Pokémon by making an API request.
    """
    water_type_url = get_water_type_url()
    if water_type_url:
        data = fetch_data(water_type_url)
        if data:
            return [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return []

def display_pokemons(pokemons: List[str]) -> None:
    """
    Displays the names of all Water-type Pokémon in a readable format.
    """
    if pokemons:
        print("List of Water-type Pokémon:")
        for i, pokemon in enumerate(pokemons, start=1):
            print(f"{i}. {pokemon}")
    else:
        print("No Pokémon found.")

if __name__ == "__main__":
    """
    Main function to fetch and display Water-type Pokémon.
    """
    water_pokemons = fetch_water_pokemons()
    display_pokemons(water_pokemons)
