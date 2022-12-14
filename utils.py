import re
from datetime import date


def PGN_clean(pgn_str):     # there is other data in the pgn with ratings etc. but we don't care about this for the db as it's in the json from chess.com
    pgn_str = re.sub(r".*\n\n|\{[^}]*} *|\$\d+ *|\d+\.\.\. *", "", pgn_str, 0, re.DOTALL)   #strip out all comments and other stuff so the pgn contains moves only
    return pgn_str

class Game:
    def __init__(self):
        self.played_date = date(2020,1,1)
        self.time_control = 600
        self.colour = "white"
        self.result = "stalemate"
        self.my_rating = 1000
        self.moves = ""

    def load_from_json(self, gamejson, user):
        if gamejson['rules'] == 'chess':
            initial_date_str = re.search(r'(?<=\[Date \")[^\"]*', gamejson['pgn']).group()
            dateargs = re.split("\.", initial_date_str)
            self.played_date = date(*[int(x) for x in dateargs])
            self.time_control = gamejson['time_control']
            if gamejson['white']['username'] == user:
                self.colour = 'white'
            else:
                self.colour = 'black'
            self.result = gamejson[self.colour]['result']
            self.my_rating = gamejson[self.colour]['rating']
            self.moves = PGN_clean(gamejson['pgn'])
            return 0
        else:
            print("warning: this game uses unsupported format/rules, do not load to db")
            return 1
        

