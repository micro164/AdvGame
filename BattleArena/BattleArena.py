from Client.Client import get_player_list
from Utilities.HelperUtilities import filter_out_self
from Battle.Battle import battle
from Classes.Classes import Enemy

final_player_list = list()


def player_vs_player():
	_display_player_list()

	player_index = input("Who do you want to fight? ")
	enemy_to_fight = final_player_list[int(player_index) - 1]
	print(enemy_to_fight)
	print(enemy_to_fight.name)
	print(str(enemy_to_fight.MaxHP))
	print(str(enemy_to_fight.Strength))
	print(str(enemy_to_fight.Defense))
	print(str(enemy_to_fight.exp))
	print(str(enemy_to_fight.lvl))

	battle(Enemy(
		enemy_to_fight.name,
		enemy_to_fight.MaxHP,
		enemy_to_fight.Strength,
		enemy_to_fight.Defense,
		enemy_to_fight.MaxExp,
		enemy_to_fight.lvl,
		enemy_to_fight.MaxHP,
		False
	))


def _display_player_list():
	filtered_list = filter(filter_out_self, get_player_list())

	for filtered in filtered_list:
		final_player_list.extend(filtered)

	if len(final_player_list) != 0:
		index = 1
		for player in final_player_list:
			print(str(index) + ". Name: " + player.name + " Class: " + player.Pclass)
			index += 1
	else:
		print("No players found")
