def rec_coin(target,coins):
	min_coins= target
	
	if target in coins:
		return 1

	else:
		for i in [c for c in coins if c<=target]:
			num_coins = 1 + rec_coin(target-1,coins)

			if num_coins<min_coins:
				min_coins=num_coins

	return min_coins


def rec_coin_dyam(target,coins,known_result):
	min_coins=target
	
	if target in coins:
		known_result[target]=1
		return 1
	
	elif known_result[target]>0:
		return known_result[target]

	else:
		for i in [c for c in coins if c <=target]:
			num_coins = 1+rec_coin_dyam(target-i,coins,known_result)

		if num_coins < min_coins:
			min_coins= num_coins
			known_result[target]=min_coins

	return min_coins

target=74

coins =[1,5,10,25]
known_result=[0]*(target+1)

def lo(target,coins):
	stop=True
	count =0
	while stop:
		
		if target > max(coins):
			target-=max(coins)
		
		elif target < max(coins):
			coins = [c for c in coins if c is < target]
			
			




print(rec_coin_dyam(target,coins,known_result))