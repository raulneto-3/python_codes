import configparser
from steam import Steam

# Read the API key from keys.conf
config = configparser.ConfigParser()
config.read('keys.conf')
api_key = config['DEFAULT']['STEAM_API_KEY']

steam = Steam(api_key)

# Replace 'STEAM_ID' with the actual Steam ID you want to query
steam_id = 'ninguemD'

# Get player summaries
player_info = steam.users.get_user_details(steam_id)

print(f"Player Name: {player_info['personaname']}")
print(f"Profile URL: {player_info['profileurl']}")
print(f"Avatar: {player_info['avatarfull']}")