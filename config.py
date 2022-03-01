import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("5271448590:AAHz07JQwrUUx-vO2tE_C5Xvg8qVC9lThvE", "")
    # The Telegram API things
    API_ID = int(os.environ.get("11391818",)
    API_HASH = os.environ.get("ae243843b0c6fe3b59f0919d5d5a84f8")
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
    HTTP_PROXY = os.environ.get("", "")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("5131599131", ""))
    SESSION_NAME = "UPLOADER-RVX-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("mongodb+srv://Ravindu:Ravi12ndu.@cluster0.y33ek.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", "")
    MAX_RESULTS = "50"
