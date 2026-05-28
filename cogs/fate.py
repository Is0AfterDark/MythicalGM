import discord
from discord.ext import commands
from discord import app_commands
import random
import chaos

class Fatecheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   #@app_commands.describe(nom_du_param="la description a montrer le user")
    @app_commands.command(name="fatecheck",description="Roll a fate check using the chaos factor")
    @app_commands.describe(shape="Dice shape to roll")
    async def roll(self, interaction: discord.Interaction, chaos: chaos.ChaosFactor):
        chaos = chaos.value
        randInt = random.randint(1,100)
        embed = discord.Embed(title="Dice roll results", description=f"You rolled a {randInt}!", color=discord.Color.purple())
        embed.add_field(name="Chaos Factor:", value=f"{chaos}", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Fatecheck(bot))