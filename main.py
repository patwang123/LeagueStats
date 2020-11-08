from LeagueStats import *
def main():
	api_key = 'RGAPI-39682736-62c2-4870-9240-41eb76b425cc'
	api = LeagueStats(api_key)
	r = api.get_summoner_by_name('Patwang123')
	print(r)
if __name__ == '__main__':
	main()