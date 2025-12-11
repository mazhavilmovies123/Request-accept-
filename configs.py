from os import path, getenv
import os, time 
#from pyrogram.types import BotCommand

class Config:
    API_ID = int(getenv("API_ID", "21419016"))
    API_HASH = getenv("API_HASH", "79198e1eb4cfd0f771a89d83b9144e7e")
    BOT_TOKEN = getenv("BOT_TOKEN", "8320877229:AAH_I5dbw-YFsn6niXpOV7TeNGt7OTdwagY")
    UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "MazhavilMoviesUpdates")
    UPDATECHANNEL_ID = int(getenv("UPDATECHANNEL_ID", "-1002674451609"))
    ADMIN = list(map(int, getenv("ADMIN", "1933114137").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://kentkouhali5l_db_user:gFvGsyASnQPu9rDZ@cluster0.m9xgtlr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOG_CHANNEL = -1003259271720
    
    #web response 
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    BOT_UPTIME  = time.time()
    PORT = os.environ.get("PORT", "8080")
    
    DP_PIC = os.environ.get("DP_PIC", "https://envs.sh/_qj.mp4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME","Mazhavil_approver_bot")
 # Subsprice Gif & Auto Request Accept
    SURPRICE = os.environ.get("SURPRICE", "https://envs.sh/_qj.mp4").split()

    LOGO = """🇩 🇵_🇧 🇴 🇹 🇿"""

dp1 = Config()
