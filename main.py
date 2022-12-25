#!/usr/bin/python3.11

import src.bot as bot
import os

from dotenv import load_dotenv

load_dotenv("./.env")


if __name__ == "__main__":
    TOKEN = os.environ.get("DISCORD_TOKEN")
    
    bot.run_discord_bot(TOKEN)
