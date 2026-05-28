from unittest import case

import discord
from discord.ext import commands
from discord import app_commands
import random
import odds

class Fatecheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   #@app_commands.describe(nom_du_param="la description a montrer le user")
    @app_commands.command(name="fatecheck",description="Roll a fate check using the chaos factor")
    @app_commands.describe(chaos="Chaos factor that influence the roll's results")
    @app_commands.describe(odds="The likeliness of the roll. Takes the chaos factor into account")
    async def roll(self, interaction: discord.Interaction, chaos: int, likelyhood: odds.Odds):
        #error handling
        errmsg = discord.Embed(title="There was an error during the roll", description="The chaos factor value has to be between 1 and 9", color=discord.Color.red())
        if chaos > 9 or chaos < 0:
            await interaction.response.send_message(embed=errmsg, ephemeral=True)

        #roll handling
        randInt = random.randint(1,100)
        chance = likelyhood.value
        FATESUCCESS = {
            0: [1,1,1,5,10,15,25,35,50],
            1: [1,1,5,10,15,25,35,50,65],
            2: [1,5,10,15,25,35,50,65,75],
            3: [5,10,15,25,35,50,65,75,85],
            4: [10,15,25,35,50,65,75,85,90],
            5: [15,25,35,50,65,75,85,90,95],
            6: [25,35,50,65,75,85,90,95,99],
            7: [35,50,65,75,85,90,95,99,99],
            8: [50,65,75,85,90,95,99,99,99]
        }

        FATECRITS = {
            0: [81,81,81,82,83,84,86,88,91],
            1: [81,81,82,83,84,86,88,91,94],
            2: [81,82,83,84,86,88,91,94,96],
            3: [82,83,84,86,88,91,94,96,98],
            4: [83,84,86,88,91,94,96,98,99],
            5: [84,86,88,91,94,96,98,99,100],
            6: [86,88,91,94,96,98,99,100,0],
            7: [88,91,94,96,98,99,100,0,0],
            8: [91,94,96,98,99,100,0,0,0]
        }

        FATEFAILS = {
            0: [0,0,0,1,2,3,5,7,10],
            1: [0,0,1,2,3,5,7,10,13],
            2: [0,1,2,3,5,7,10,13,15],
            3: [1,2,3,5,7,10,13,15,17],
            4: [2,3,5,7,10,13,15,17,18],
            5: [3,5,7,10,13,15,17,18,19],
            6: [5,7,10,13,15,17,18,19,20],
            7: [7,10,13,15,17,18,19,20,20],
            8: [10,13,15,17,18,19,20,20,20]
        }

        if randInt >= FATECRITS[chance][chaos - 1]:
            result = "Exceptional yes!"
        elif randInt >= FATESUCCESS[chance][chaos - 1]:
            result = "Yes."
        elif randInt <= FATEFAILS[chance][chaos - 1]:
            result = "Exceptional no!"
        else:
            result = "No."



        #Message handling
        embed = discord.Embed(title="Dice roll results", description=f"You rolled a {randInt}!", color=discord.Color.purple())
        embed.add_field(name="The answer is", value=f"{result}", inline=False)
        embed.add_field(name="Chaos Factor:", value=f"{chaos}", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Fatecheck(bot))