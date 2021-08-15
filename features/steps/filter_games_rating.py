from behave import *
from src.Game import *
from src.Catalogue import *

# Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
    context = {}

@then("{total} game will match")
def step_impl(context,total):
    print(total+" game will match")

@given("the user selects one or more ratings")
def step_impl(context):
    game_ratings = []
    for row in context.table:
        game_ratings.append(row['CATEGORY'])
    context.ratings = game_ratings


@when('the names of these games are')
def step_impl(context):
    expected_games = True
    result_games = []
    for row in context.table:
        result_games.append(row['NAME'])
    for game in context.result:
        if game.name not in result_games:
            print("No game " + game.name)
            expected_games = False
    assert expected_games is True

@when('choosing the {type_search} option')
def step_impl(context, type_search):
    if type_search == 'search by ratings':
        context.type_search = type_search


@when("the games are")
def step_impl(context):
    game_list = []
    for row in context.table:
        game = Game(row['NAME'], row['RELEASE DATE'], row['DEVELOPER'], row['RATE'])
        game_list.append(game)
    context.games = game_list


@when("there is no match with the list of games")
def step_impl(context):
    validate = True
    for row in context.games:
        if row.rating is not context.ratings:
            print('No rating match')
            validate = False
        assert False is validate


@then("following message will be displayed: {message}")
def step_impl(context, message):
    print(message)


@given("the user enter the rating option:{XRating}")
def step_impl(context,XRating):
    message=get_game_rating(context.games,context.ratings)

    context.message = message