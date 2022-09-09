import os
from db_connection_defaults import default_connectors   #local .py file for setting environment variable defaults, create your own if cloning

env_vars = os.environ.items()

class MYSQL:
    USER=env_vars['DB_USER'] or default_connectors.USER
    PORT=env_vars['PORT'] or default_connectors.PORT
    DATABASE=env_vars['DATABASE'] or default_connectors.DATABASE
    PASSWORD=env_vars['DB_PASS'] or default_connectors.DB_PASS
    HOST=env_vars['DB_HOST'] or default_connectors.HOST