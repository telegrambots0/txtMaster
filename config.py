import os

API_ID = API_ID = 25263708

API_HASH = os.environ.get("API_HASH", "9bde48b267ce65a576b478c0ff8c7bbb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7073327110:AAGFGVPzzqquAQNMBXACtyZRv5UuVvOIGgg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6955269919))

LOG = -1002137091035

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6955269919").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
