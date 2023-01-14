from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 17983098
API_HASH = "ee28199396e0925f1f44d945ac174f64"
BOT_TOKEN = "5596598781:AAEVMvT3LNz2wrSYiy69CbuOPvHAcTkmKvg"
BOT_UN = "Fbmessenger1235bot"
AUTH_USERS = "1227193881"
LOG_CHANNEL = "e7alat19871"
LOG_ID = "-1001683878954"
FORCESUB = "-1001230414925"
FORCESUB_UN = "ibnAlQyyim"
ACCESS_CHANNEL = "-1001606038689"
MONGODB_URI = "mongodb+srv://Bala7a19871:Ibntaymya1.@cluster0.5mtsc.mongodb.net/?retryWrites=true&w=majority"
Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
