REGION = {'North America': 'na1',
			'Brazil': 'br1',
			'EU North': 'eun1',
			'EU West': 'euw1',
			'Japan': 'jp1',
			'Korea': 'kr',
			'Latin America 1': 'la1',
			'Latin America 2': 'la2',
			'Oceania': 'oc1',
			'Turkey': 'tr1',
			'Russia': 'ru1'}
ACCOUNT_REGION = {'Americas': 'americas',
					'Asia': 'asia',
					'Europe': 'europe'}
URL = {'base': 'https://{region}.api.riotgames.com/{url}?api_key={api_key}',

		#account-v1
		'account_by_riot_id': 'riot/accounts/v1/by-riot-id/{game_name}/{tagline}',
		'account_by_puuid': 'riot/account/v1/by-puuid/{puuid}',
		'account_active_shard': 'riot/account/v1/active-shards/by-game/{game}/by-puuid/{puuid}',

		#champion-v3
		'champion_rotations': 'lol/platform/v3/champion-rotations',


		#summoner-v4
		'summoner_by_name': 'lol/summoner/v4/summoners/by-name/{summonerName}',
		'summoner_by_puuid': 'lol/summoner/v4/summoners/by-puuid/{encryptedPUUID}',
		'summoner_by_summonerID': 'lol/summoner/v4/summoners/by-puuid/{encryptedSummonerId}',
		'summoner_by_account': 'lol/summoner/v4/summoners/by-account/{encryptedAccountId}'}