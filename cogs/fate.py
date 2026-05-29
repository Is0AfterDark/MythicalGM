import discord
from discord.ext import commands
from discord import app_commands
import random
import odds


async def randomevent():
    eventInt = random.randint(1, 100)
    event = ""

    # This is bad and I should be ashamed of it.
    # TODO rework later
    if eventInt in range(1, 6):
        event = "Remote Event"
    elif eventInt in range(6, 10):
        event = "Ambiguous Event"
    elif eventInt in range(10, 20):
        event = "New NPC"
    elif eventInt in range(21, 40):
        event = "NPC Action"
    elif eventInt in range(41, 45):
        event = "NPC Negative"
    elif eventInt in range(46, 50):
        event = "NPC Positive"
    elif eventInt in range(51, 55):
        event = "Move toward a Thread"
    elif eventInt in range(56, 65):
        event = "Move away from a Thread"
    elif eventInt in range(66, 70):
        event = "Close a Thread"
    elif eventInt in range(71, 80):
        event = "PC Negative"
    elif eventInt in range(81, 85):
        event = "PC Positive"
    elif eventInt in range(86, 100):
        event = "Current Context"

    return event


class Fatecheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   #@app_commands.describe(nom_du_param="la description a montrer le user")
    @app_commands.command(name="fatecheck",description="Roll a fate check using the chaos factor")
    @app_commands.describe(chaos="Chaos factor that influence the roll's results")
    @app_commands.describe(likelyhood="The likeliness of the roll. Takes the chaos factor into account")
    async def fate(self, interaction: discord.Interaction, chaos: int, likelyhood: odds.Odds):
        #error handling
        errmsg = discord.Embed(title="There was an error during the roll", description="The chaos factor value has to be between 1 and 9", color=discord.Color.red())
        if chaos > 9 or chaos < 0:
            await interaction.response.send_message(embed=errmsg, ephemeral=True)

        #roll handling
        randInt = random.randint(1,100)
        chance = likelyhood.value
        result = ""
        chaosvalue = randInt % 10
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

        FATEFAILS = {
            0: [81,81,81,82,83,84,86,88,91],
            1: [81,81,82,83,84,86,88,91,94],
            2: [81,82,83,84,86,88,91,94,96],
            3: [82,83,84,86,88,91,94,96,98],
            4: [83,84,86,88,91,94,96,98,99],
            5: [84,86,88,91,94,96,98,99,100],
            6: [86,88,91,94,96,98,99,100,101],
            7: [88,91,94,96,98,99,100,101,101],
            8: [91,94,96,98,99,100,101,101,101]
        }

        FATECRITS = {
            0: [101,101,101,1,2,3,5,7,10],
            1: [101,101,1,2,3,5,7,10,13],
            2: [101,1,2,3,5,7,10,13,15],
            3: [1,2,3,5,7,10,13,15,17],
            4: [2,3,5,7,10,13,15,17,18],
            5: [3,5,7,10,13,15,17,18,19],
            6: [5,7,10,13,15,17,18,19,20],
            7: [7,10,13,15,17,18,19,20,20],
            8: [10,13,15,17,18,19,20,20,20]
        }

        SAMESIES = [11,22,33,44,55,66,77,88,99]


        if FATEFAILS[chance][chaos - 1] == 101 or FATECRITS[chance][chaos - 1] == 101:
            result = "Yes."
        elif randInt <= FATECRITS[chance][chaos - 1]:
            result = "Exceptional yes!"
        elif randInt > FATESUCCESS[chance][chaos - 1]:
            result = "No."
        elif randInt >= FATEFAILS[chance][chaos - 1]:
            result = "Exceptional no!"
        else:
            result = "Yes."

        #Message handling
        embed = discord.Embed(title=f"You rolled a {randInt}! The Oracle says...{result}", description=f"", color=discord.Color.purple())
        embed.add_field(name="Parameters:", value=f"Chaos factor: {chaos} | Likelyhood: {likelyhood.name}", inline=False)
        if randInt in SAMESIES and chaosvalue == chaos:
            randev = await randomevent()
            embed.add_field(name=f"Random Event: {randev}", value="", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Fatecheck(bot))