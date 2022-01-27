from os import environ

TEAM = environ.get('TEAM', None)
AUTHKEY = environ.get('AUTHKEY', None)

# user IDs like U01ABCD01
ALLOWED_USER_IDS = []
