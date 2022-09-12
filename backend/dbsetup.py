import mysql.connector
from mysql.connector import errorcode
from config import MYSQL
from utils import Game

class Database:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user=MYSQL.USER,
                                        password=MYSQL.PASSWORD,
                                        host=MYSQL.HOST,
                                        port=MYSQL.PORT,
                                        database=MYSQL.DATABASE)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        else:
            print(f"Connected to MySQL at {MYSQL.HOST}, on port {MYSQL.PORT}")
            self.cursor = self.cnx.cursor()


    def __enter__(self):
        try:
            print("Connecting to games table:")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS games (
                        game_id INT NOT NULL AUTO_INCREMENT, 
                        played_date DATE, 
                        time_control VARCHAR(10), 
                        colour ENUM('white', 'black'), 
                        result ENUM('win', 'checkmated', 'agreed', 'repetition', 'timeout', 'resigned', 'stalemate', 'lose', 'insufficient', '50move', 'abandoned', 'threecheck', 'timevsinsufficient'),
                        my_rating INT,
                        moves VARCHAR(10000) NOT NULL,
                        PRIMARY KEY (game_id)) 
                        ENGINE=InnoDB""")               #should support games of up to 1000 moves, if you're playing more than 1000 move chess games what the fuck are you doing
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("OK")
        return self
        

    def addgame(self, game):
        self.cursor.execute(f"""INSERT INTO games 
                (played_date, time_control, colour, result, my_rating, moves)
                VALUES (%s, %s, %s, %s, %s, %s)""", 
                (game.played_date, game.time_control, game.colour, game.result, game.my_rating, game.moves))
        self.cnx.commit()

    def deletegame(self, id):
        self.cursor.execute(f"DELETE FROM games WHERE game_id = {id}")
        self.cnx.commit()
    
    def deleteall(self):
        print("Clearing all games from database(!)")
        self.cursor.execute(f"DELETE FROM games")
        self.cnx.commit()

    def most_recent_update(self):
        self.cursor.execute(f"SELECT played_date FROM games WHERE game_id = MAX(game_id)")
        for (played_date) in self.cursor:
            date = played_date
        return date
    
    def fetch_on_date(self, date):
        self.cursor.execute(f"SELECT time_control, colour, result, my_rating, moves FROM games WHERE played_date = %s", (date))
        games = []
        for (time_control, colour, result, my_rating, moves) in self.cursor:
            game = Game()
            game.played_date = date
            game.colour = colour
            game.time_control = time_control
            game.result = result
            game.my_rating = my_rating
            game.moves = moves
            games.append(game)
        return games

    def __exit__(self, exc_type, exc_value, traceback):
        self.cnx.close()



