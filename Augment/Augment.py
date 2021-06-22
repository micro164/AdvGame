from Classes.Classes import Player


def augment(player_value, item_value, item_lvl_value, item_name, value_name):
	"""Augment a weapon or armor adding to ites attack or defense"""
	
	player_value = player_value - item_value
	item_value = item_value + item_lvl_value
	player_value = player_value + item_value
	print("Your " + item_name + " now has " + str(item_value) + " " + value_name)
