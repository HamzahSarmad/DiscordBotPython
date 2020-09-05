import discord
from discord.ext import commands
import requests, json

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="weather", aliases=["Weather"],pass_context=True)
    async def weather(self, ctx, city : str):
        embed=discord.Embed(title="Weather", description=f"Here is the current weather in {city}")
        api_key = "KEY"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            main = data["main"]
            temp = round(main["temp"] - 273.15,2)
            press = main["pressure"]
            humidity = main["humidity"]
            z = data["weather"]

            weather_desc = z[0]["description"]

            embed.add_field(name="Temperature",value=f"{temp}",inline=True)
            embed.add_field(name="Humidity",value=f"{humidity}",inline=True)
            embed.add_field(name="Pressure",value=f"{press}",inline=True)
            embed.add_field(name="Weather report",value=f"{weather_desc}",inline=True)
            await ctx.send(embed=embed)
        else:
            await ctx.send("404: City Not Found")

def setup(bot):
    bot.add_cog(weather(bot))