import discord
from discord.ext import commands
from discord import app_commands
import random
from cogs.fate import randomevent

class ExpectedScene(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   #@app_commands.describe(nom_du_param="la description a montrer le user")
    @app_commands.command(name="exscene",description="Roll for an expected scene")
    @app_commands.describe(chaos="Chaos factor")
    async def exscene(self, interaction: discord.Interaction, chaos: int):
        # error handling
        global altdie
        errmsg = discord.Embed(title="There was an error during the roll",
                               description="The chaos factor value has to be between 1 and 9",
                               color=discord.Color.red())
        if chaos > 9 or chaos < 0:
            await interaction.response.send_message(embed=errmsg, ephemeral=True)

        #mechanism
        scenedten = random.randint(1, 10)
        scenemsg = ""
        nevent = ""
        SCENE_ALT = {
            1: "Remove a Character",
            2: "Add a Character",
            3: "Reduce/Remove an Activity",
            4: "Increase an Activity",
            5: "Remove an Object",
            6: "Add an Object",
            7: "Roll Twice"
        }

        def two_rolls():
            altdtenone = random.randint(1, 10)
            altdtentwo = random.randint(1, 10)

            while altdtenone >= 7 or altdtentwo >= 7:
                altdtenone = random.randint(1, 10)
                altdtentwo = random.randint(1, 10)

            results = [altdtenone, altdtentwo]
            return results

        if scenedten > chaos:
            scenemsg = "Expected Scene."
        elif scenedten < chaos and scenedten % 2 == 0:
            scenemsg = "Interrupt scene!"
            nevent = await randomevent()
        else:
            scenemsg = "Altered scene!"
            altdie = random.randint(1,10)
            if altdie > 7:
                altevents = two_rolls()
                nevent = f"{SCENE_ALT[7]}! Alterations: {SCENE_ALT[altevents[0]]} ({altevents[0]}), {SCENE_ALT[altevents[1]]} ({altevents[1]})"
            else:
                nevent = f"{SCENE_ALT[altdie]}"

        embed = discord.Embed(title=f"Scene roll results: {scenedten}. {scenemsg}", description=f"", color=discord.Color.purple())
        if nevent == "":
            embed.add_field(name=f"Chaos factor: {chaos}", value=f"", inline=False)
        elif scenemsg == "Altered scene!":
            embed.add_field(name=f"{nevent}", value=f"", inline=False)
            embed.add_field(name=f"Chaos factor: {chaos}", value=f"", inline=False)
            embed.add_field(name=f"Altered scene roll: {altdie}", value=f"", inline=False)
        else:
            embed.add_field(name=f"{nevent} | Chaos factor: {chaos}", value=f"", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(ExpectedScene(bot))