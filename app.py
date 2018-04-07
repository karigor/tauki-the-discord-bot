import os

from discord_client.client import client

client.run(os.environ.get("DISCORD_BOT_TOKEN"))
