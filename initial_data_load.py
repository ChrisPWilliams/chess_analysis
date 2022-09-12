import requests
from backend.dbsetup import Database
from utils import Game
from config import CHESS_DOT_COM
from chessdotcom import get_player_game_archives

with Database() as db:
    db.deleteall()
myarchives = get_player_game_archives(CHESS_DOT_COM.USER)
myarchivesjson = myarchives.json

for archive in myarchivesjson["archives"]:
    response = requests.get(archive)
    with Database() as db:
        for gamejson in response['games']:
            game = Game()
            game.load_from_json(gamejson, CHESS_DOT_COM.USER)
            db.addgame(game)
