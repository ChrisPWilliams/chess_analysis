import requests
from backend.dbsetup import Database
from utils import Game
from config import CHESS
from chessdotcom import get_player_game_archives

with Database() as db:
    db.deleteall()
myarchives = get_player_game_archives(CHESS.USER)
myarchivesjson = myarchives.json

for archive in myarchivesjson["archives"]:
    response = requests.get(archive)
    with Database() as db:
        for gamejson in response['games']:
            game = Game()
            game.load_from_json(gamejson)
            db.addgame(game)
