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
        tabRes = ["No", "Yes", "Exceptional Yes!", "Exceptional No!"]
        result = ""

        match chaos:
            case 1:
                match likelyhood:
                    case 3:
                        if randInt >= 82:
                            result = tabRes[2]
                        elif randInt > 5:
                            result = tabRes[1]
                        elif randInt < 5:
                            result = tabRes[0]
                        elif randInt == 1:
                            result = tabRes[3]
                    case 4:
                        if randInt >= 83:
                            result = tabRes[2]
                        elif randInt > 10:
                            result = tabRes[1]
                        elif randInt < 10:
                            result = tabRes[0]
                        elif randInt <= 2:
                            result = tabRes[3]
                    case 5:
                         if randInt >= 84:
                             result = tabRes[2]
                         elif randInt > 15:
                             result = tabRes[1]
                         elif randInt < 15:
                             result = tabRes[0]
                         elif randInt <= 3:
                             result = tabRes[3]
                    case 6:
                         if randInt >= 86:
                             result = tabRes[2]
                         elif randInt > 25:
                             result = tabRes[1]
                         elif randInt < 25:
                             result = tabRes[0]
                         elif randInt <= 5:
                             result = tabRes[3]
                    case 7:
                         if randInt >= 88:
                             result = tabRes[2]
                         elif randInt > 35:
                             result = tabRes[1]
                         elif randInt < 35:
                             result = tabRes[0]
                         elif randInt <= 7:
                             result = tabRes[3]
                    case 8:
                         if randInt >= 91:
                             result = tabRes[2]
                         elif randInt > 50:
                             result = tabRes[1]
                         elif randInt < 50:
                             result = tabRes[0]
                         elif randInt <= 10:
                             result = tabRes[3]
                    case _:
                        if randInt >= 81:
                            result = tabRes[2]
                        else:
                            result = tabRes[1]
            case 2:
                match likelyhood:
                     case 0:
                         pass
                     case 1:
                         pass
                     case 2:
                         pass
                     case 3:
                         pass
                     case 4:
                         pass
                     case 5:
                         pass
                     case 6:
                         pass
                     case 7:
                         pass
                     case 8:
                         pass
            case 3:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 4:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 5:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 6:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 7:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 8:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass
            case 9:
                match likelyhood:
                    case 0:
                        pass
                    case 1:
                        pass
                    case 2:
                        pass
                    case 3:
                        pass
                    case 4:
                        pass
                    case 5:
                        pass
                    case 6:
                        pass
                    case 7:
                        pass
                    case 8:
                        pass

        #Message handling
        embed = discord.Embed(title="Dice roll results", description=f"You rolled a {randInt}!", color=discord.Color.purple())
        embed.add_field(name="The answer is", value=f"{result}", inline=False)
        embed.add_field(name="Chaos Factor:", value=f"{chaos}", inline=False)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Fatecheck(bot))