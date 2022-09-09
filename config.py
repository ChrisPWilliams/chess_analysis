import os
from db_connection_defaults import default_connectors   #local .py file for setting environment variable defaults, create your own if cloning

class MYSQL:
    USER=os.environ.get('DB_USER') or default_connectors.USER
    PORT=os.environ.get('PORT') or default_connectors.PORT
    DATABASE=os.environ.get('DATABASE') or default_connectors.DATABASE
    PASSWORD=os.environ.get('DB_PASS') or default_connectors.DB_PASS
    HOST=os.environ.get('DB_HOST') or default_connectors.HOST