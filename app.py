import os
from discord_client.client import client

client.run(os.environ.get("DISCORD_APP_TOKEN"))
