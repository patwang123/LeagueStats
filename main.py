from LeagueStats import *
from dotenv import load_dotenv
import os

def main():
	load_dotenv()
	api_key = os.getenv('API_KEY') #use your own!
	api = LeagueStats(api_key)
	r = api.get_summoner_by_name('Patwang123')
	print(r)
if __name__ == '__main__':
	main()