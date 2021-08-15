from src.Catalogue import *
from src.Game import *


if __name__ == '__main__':

	game_A = Game( "Devil May Cry 5", 2019,  "Capcom", "M")
	game_B = Game( "Uncharted 4: A Thief's End", 2016, "Naughtt Dog", "T")
	game_C = Game( "The Legend of Zelda: Breath of the Wild",2017,"Nintendo","E")
	game_D = Game( "Final Fantasy XV", 2016,"Square Enix", "T")
	game_E = Game( "Marvel's Spider-Man",2018,"Insomniac Games","T")
	game_F = Game( "The Last of Us  ",2013,"Naughty Dog ","M")
	game_G = Game( "Super Smash Bros. Ultimate",2018,"Bandai Namco Studios","E")
	game_H = Game( "Splatoon's Spider-Man",2016,"Nintendo","T")
	game_I = Game( "The Witcher 3: Wild Hunt",2015,"CD Projekt","M")


	game_list = [game_F, game_G, game_I, game_H]

	result, msj = get_game_name(game_list, "Devil")
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj, error = get_game_rating(game_list, ["T"])
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj, error = get_game_rating(game_list, ["M", "T"])
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj, error = get_game_rating(game_list, ["A"])
	print(msj)
	print(error)
	for x in result:
		print(x)
	print("-"*20)



	result, msj = get_game_developer(game_list, "Square Enix")
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj = get_game_developer(game_list, "Rockstar")
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj = get_game_release_date(game_list, 1999, 2012 )
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj = get_game_release_date(game_list)
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj = get_game_release_date(game_list, 2020, 1999)
	print(msj)
	for x in result:
		print(x)
	print("-"*20)

	result, msj = get_game_release_date(game_list, 2018, 2020)
	print(msj)
	for x in result:
		print(x)
	print("-"*20)
