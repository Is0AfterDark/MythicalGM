import discord
from discord.ext import commands
from discord import app_commands
import random
import diceShape
from diceShape import DiceShape

class Diceroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   #@app_commands.describe(nom_du_param="la description a montrer le user")
    @app_commands.command(name="diceroll",description="Roll a dice.")
    @app_commands.describe(shape="Dice shape to roll")
    async def diceroll(self, interaction: discord.Interaction, shape: diceShape.DiceShape):
        randInt = random.randint(1,shape.value)
        embed = discord.Embed(title="Dice roll results", description=f"You rolled a {randInt}!", color=discord.Color.purple())
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Diceroll(bot))