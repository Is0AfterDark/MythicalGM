import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class Client(commands.Bot):
    async def on_ready(self):
        try:
            synced = await self.tree.sync()
            print(f'Synced {len(synced)} commands')
        except Exception as e:
            print(f'Error syncing commands: {e}')

    async def setup_hook(self):
        for file in os.listdir("cogs"):
            if file.endswith(".py"):
                try:
                    await client.load_extension(f"cogs.{file[:-3]}")
                    print(f"Loaded {file}")
                except Exception as e:
                    print(f"Failed to load {file}")
                    print(f"[ERROR] {e}")

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

client.run(TOKEN)