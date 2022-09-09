import os

env_vars = os.environ.items()

class MYSQL:
    USER=env_vars['USER']
    PORT=env_vars['PORT'] or 3307
    DATABASE=env_vars['DATABASE']
    PASSWORD=env_vars['DB_PASS']
    HOST=env_vars['HOST']