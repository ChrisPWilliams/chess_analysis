import os
from db_connection_defaults import default_connectors   #local .py file for setting environment variable defaults, create your own if cloning

class MYSQL:
    USER=os.environ.get('DB_USER') or default_connectors.USER
    PORT=os.environ.get('PORT') or default_connectors.PORT
    DATABASE=os.environ.get('DATABASE') or default_connectors.DATABASE
    PASSWORD=os.environ.get('DB_PASS') or default_connectors.DB_PASS
    HOST=os.environ.get('DB_HOST') or default_connectors.HOST

class CHESS_DOT_COM:
    USER=default_connectors.CHESS_USER 

# to run this locally, use the following default connectors to get everything set up. Create a db_connection_defaults.py file with the following structure:

# class default_connectors():
#     USER = 'your database username'
#     DB_PASS = 'your database password'
#     DATABASE = 'your database name'
#     PORT = 3306               # default port for mysql, if you have set up your server with a different port use that one
#     HOST = 'localhost'
#     CHESS_USER = 'your chess.com username'