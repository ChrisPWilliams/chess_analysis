import mysql.connector
from mysql.connector import errorcode
from config import MYSQL

class Database:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(user=MYSQL.USER,
                                        password=MYSQL.PASSWORD,
                                        host=MYSQL.HOST,
                                        port=MYSQL.PORT)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        else:
            self.cnx.close()

        print(f"Connected to MySQL at {MYSQL.HOST}, on port {MYSQL.PORT}")
        self.cursor = self.cnx.cursor()

        def create_database(cursor):
            try:
                cursor.execute(f"CREATE DATABASE {MYSQL.DATABASE} DEFAULT CHARACTER SET 'utf8'")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
                exit(1)

        try:
            self.cursor.execute(f"USE {MYSQL.DATABASE}")
        except mysql.connector.Error as err:
            print(f"Database {MYSQL.DATABASE} does not exist.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(self.cursor)
                print(f"Database {MYSQL.DATABASE} created successfully.")
                self.cnx.database = MYSQL.DATABASE
            else:
                print(err)
                exit(1)

    def __enter__(self):
        try:
            print("Creating games table:")
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS 'games' (
                        'game_id' INT NOT NULL AUTO_INCREMENT, 
                        'played_date' DATE, 
                        'time_control' SMALLINT, 
                        'colour' ENUM('white', 'black'), 
                        'result' ENUM('win', 'checkmated', 'agreed', 'repetition', 'timeout', 'resigned', 'stalemate', 'lose', 'insufficient', '50move', 'abandoned', 'threecheck', 'timevsinsufficient'),
                        'my_rating' SMALLINT,
                        'moves' VARCHAR(20000) NOT NULL,
                        PRIMARY KEY ('game_id')) 
                        ENGINE=InnoDB""")               #should support games of up to 1000 moves, if you're playing more than 1000 move chess games what the fuck are you doing
        except mysql.connector.Error as err:
                print(err.msg)
        else:
            print("OK")
            return self
        

    def addgame(self, game):
        game_id = self.cursor.lastrowid
        self.cursor.execute(f"""INSERT INTO games 
                (game_id, played_date, time_control, colour, result, my_rating, moves)
                VALUES {game_id}, {game.played_date}, {game.time_control}, {game.colour}, {game.result}, {game.my_rating}, {game.moves})""")

    def deletegame(self, id):
        self.cursor.execute(f"DELETE FROM games WHERE game_id = {id}")

    def __exit__(self, exc_type, exc_value, traceback):
        self.cnx.close()



