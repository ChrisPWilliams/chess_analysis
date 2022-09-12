from backend.dbsetup import Database
from utils import Game
from config import CHESS_DOT_COM
from chessdotcom import get_player_games_by_month

with Database() as db:
    most_recent_date = db.most_recent_update()
    response = get_player_games_by_month(CHESS_DOT_COM.USER, most_recent_date.year, most_recent_date.month)
    responsejson = response.json
    games_to_check = db.fetch_on_date(most_recent_date)
    for gamejson in responsejson['games']:
        game = Game()
        game.load_from_json(gamejson)
        if game.played_date == most_recent_date:
            included = False
            for game_to_check in games_to_check:
                if game == game_to_check:
                    included = True
                    break
            if not included:
                db.addgame(game)
        elif game.played_date > most_recent_date:
            db.addgame(game)

