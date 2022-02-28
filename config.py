import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("5271469949:AAF1K4-j2wCQNmgf2w2ts__y7S-ou5D8klw", "")
    # The Telegram API things
    API_ID = int(os.environ.get("7322056",))
    API_HASH = os.environ.get("89074aa74ed297150b3120914946db5c")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 500000000000000000000000
    TG_MAX_FILE_SIZE = 2097152000000000000000000000000
    FREE_USER_MAX_FILE_SIZE = 5000000000000000000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("182.74.243.47:3128", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("1387186514", ""))
    SESSION_NAME = "UPLOADER-RVX-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("postgres://lqgzvowgqawpig:63442795843431f67c93c37fba1e5963310b49f4173346576f1b72576f5879c2@ec2-34-230-110-100.compute-1.amazonaws.com:5432/d7qkolg9gvqf5i", "")
    MAX_RESULTS = "50"
