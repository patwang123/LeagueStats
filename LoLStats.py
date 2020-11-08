from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = 'RGAPI-77198d94-40c9-4e39-847f-138d229e50eb' #GET THIS FROM https://developer.riotgames.com/
watcher = LolWatcher(api_key)
region = 'na1'


user = 'Patwang123'
user = watcher.summoner.by_name(region,user)
print(user)

#rank information
ranked_stats = watcher.league.by_summoner(region,user['id'])
print(ranked_stats)