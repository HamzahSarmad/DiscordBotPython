import discord
from discord.ext import commands
import requests, json

class tronald(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name="donald", aliases = ["Donald", "trump","Trump"])
    async def donald(self, ctx):
        response = requests.get("https://api.tronalddump.io/random/quote")

        if response.status_code == 200:
            data = response.json()
            tag = ""
            for i in data["tags"]:
                tag = i
            val = data["value"]
            await ctx.send(f"Trump's thoughts about {tag}: {val}")

    @commands.command(name="nasaPOTD",aliases=["NasaPOTD"])
    async def nasaPOTD(self, ctx):
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=KEY")

        if response.status_code == 200:
            data = response.json()
            url = data["url"]
            await ctx.send(f"Nasa Picture of the Day \n{url}")

def setup(bot):
    bot.add_cog(tronald(bot))