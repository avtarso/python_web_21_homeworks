import os
from sys import argv


if len(argv) >= 2 and argv[1] == "prod":
    BOT_TOKEN = os.getenv("BOT_CURRENCY")
else:
    BOT_TOKEN = os.getenv("BOT_IBANTEST")