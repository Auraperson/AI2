from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "22727413"
# -------------------------------------------------------------
API_HASH = "61c37838e6e3193388c7c2fe3e7c8858"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING1 = getenv("STRING_SESSION", None)
DB_NAME = "samira-bot"
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "7685184136"))
BOT_ID = int(getenv("BOT_ID", "7791021817"))
SUPPORT_GRP = "BESTIE_UNITE_CLUB"
UPDATE_CHNL = "Silenthrex"
OWNER_USERNAME = "silenthrax"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002754356584"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "6766551134").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()
 
# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Auraperson/AI2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
