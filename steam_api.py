import requests
from pprint import pprint

BASE_URL = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api_key}&steamid={steam_id}&format=json"

SUMMARY_URL = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}"

NEWS_URL = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=440&count=3&maxlength=300&format=json"

API_KEY = "FF7F1079B659AD97EE7576316178FA08"

JWIN_ID = "76561198039527077"

def get_games(STEAM_ID, API_KEY):
    url = BASE_URL.format(api_key = API_KEY, steam_id = STEAM_ID)
    resp = requests.get(url, params={'per_page': 10})
    if not resp.ok:
        return None
    return resp.json()

def get_user_summary(user_id, key):
    url = SUMMARY_URL.format(API_KEY = key, STEAM_ID = user_id)
    resp = requests.get(url)
    if not resp.ok:
        return None
    return resp.json()