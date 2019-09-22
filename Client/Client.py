#!/usr/bin/python3
import socket
import pickle
from Classes.Classes import Player


def _decode(key, string):
	encoded_chars = []
	for i in range(len(string)):
		key_c = key[i % len(key)]
		encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
		encoded_chars.append(encoded_c)
	encoded_string = ''.join(encoded_chars)
	return encoded_string


with open('../Client/secretKey.txt', 'rb') as f:
	secretKey = pickle.load(f)


def get_player_list():
	new_player = Player(Player)
	new_list = []
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = 'gk\x97a\x95l\x9a\x92\x93cj'
	actual_host = _decode(secretKey, host)
	port = 8080
	try:
		server.connect((actual_host, port))
		sending = pickle.dumps(new_player)
		server.send(sending)
		message = server.recv(1024)
		new_list.append(pickle.loads(message))
		server.close()
	except:
		print("Server Can't be reached.")
	return new_list
