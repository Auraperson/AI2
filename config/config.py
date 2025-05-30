from os import getenv

from pyrogram import filters
from dotenv import load_dotenv

load_dotenv()

API_ID = "27402174"
# -------------------------------------------------------------
API_HASH = "53cdb3d648bf50e7625386b3e6879c23"
# --------------------------------------------------------------
BOT_TOKEN = getenv("7882598019:AAF9FW-MiuOZi-VJK41YOjBg44Nrnnnxyw4", None)
STRING1 = getenv("BQGiH74AMnVmD7Z8p4bdNjNjH0dDq0QBLvwYKMP0qkiIvwjeaBL0sFBVLnGdeTsVJ5ceI00NBOFOSiQEJZTBfVP7iIduh5LPUwQ6XupuaslRZ1H0pC_E2VvbctP27g4ArQ_M4RNA99YBesgCmlg11NpOqVIE8LY3HawAmzKQUbiKtJzRyMfhGUv_cJDnc9dJSL1E8kFn_4Pi0IbEaExKXDU2wxbGZJWtWPr4wQH8-hM-CnN9b1OqBcPYuEQpZNhY2hIOKr8L4IJiOA5eaVhQFqHYWK6Su1MiGQXDEQS85xgB4HQp-hQYeGMqqKdAptr2Nv5iCIVR7_Vofp30SdqCKh1Fm8WD0wAAAAG_nNwGAA", None)
DB_NAME = "shizuDB"
MONGO_URL = getenv("mongodb+srv://sr7blackbirds:5mRE2CGlkCXmI5pL@cluster0.jsssmx8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
OWNER_ID = int(getenv("OWNER_ID", "7978151350"))
BOT_ID = int(getenv("BOT_ID", "7940019678"))
SUPPORT_GRP = "BESTIE_UNITE_CLUB"
UPDATE_CHNL = "Silenthrex"
OWNER_USERNAME = "silenthrax"
TIME_ZONE = "Asia/Kolkata"
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002267586320"))
# --------------------------------------------------------------
SUDOERS = list(map(int, getenv("SUDOERS", "7982034286").split()))
# --------------------------------------------------------------

### DONT TOUCH or EDIT codes after this line
BANNED_USERS = filters.user()

# For customized or modified Repository
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Silenthrax/AI2",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
