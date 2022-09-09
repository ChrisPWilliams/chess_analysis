import re

def PGN_clean(pgn_str):     # there is other data in the pgn with ratings etc. but we don't care about this for the db as it's in the json from chess.com
    pgn_str = re.sub(r".*\n\n|\{[^}]*} *|\$\d+ *|\d+\.\.\. *", "", pgn_str, 0, re.DOTALL)
    return pgn_str
