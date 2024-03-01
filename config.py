import os

API_ID = API_ID = 27815405

API_HASH = os.environ.get("API_HASH", "4e70821cd2af3322f7cf2f2887e32821")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7078184845:AAEHj8NIzn7-kGJXumQgAGVlhDnhrhf6uB8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6679714610))

LOG = -1002146213576

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6679714610").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
