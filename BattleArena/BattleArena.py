from Client.Client import get_player_list


def player_vs_player():
	_display_player_list()


def _display_player_list():
	player_list = get_player_list()

	for player in player_list:
		print("Name: " + player.name + " Class: " + player.Pclass)
