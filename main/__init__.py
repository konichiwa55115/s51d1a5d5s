from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=17983098, cast=int)
API_HASH = config("API_HASH", default="ee28199396e0925f1f44d945ac174f64")
BOT_TOKEN = config("BOT_TOKEN", default="5596598781:AAEVMvT3LNz2wrSYiy69CbuOPvHAcTkmKvg")
BOT_UN = config("BOT_UN", default="Fbmessenger1235bot")
AUTH_USERS = config("AUTH_USERS", default=1227193881, cast=int)
LOG_CHANNEL = config("LOG_CHANNEL", default="e7alat19871")
LOG_ID = config("LOG_ID", default="-1001683878954")
FORCESUB = config("FORCESUB", default="1230414925")
FORCESUB_UN = config("FORCESUB_UN", default="ibnAlQyyim")
ACCESS_CHANNEL = config("ACCESS_CHANNEL", default="-1001606038689")
MONGODB_URI = config("MONGODB_URI", default="mongodb+srv://Bala7a19871:Ibntaymya1.@cluster0.5mtsc.mongodb.net/?retryWrites=true&w=majority")
Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
