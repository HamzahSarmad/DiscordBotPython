from discord.ext import commands
import sqlite3
import discord

#Access DB
mydb = sqlite3.connect("cogs/userlevels.db")

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="money", aliases=["bal","balance","Money","Bal","Balance","bells","Bells","bell","Bell"], pass_context=True)
    async def money(self, ctx, member: discord.User):
        if not member:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT balance FROM economy WHERE client_id = " + str(ctx.message.author.id))
            result = mycursor.fetchall()
            await ctx.send(f"{ctx.message.author.name}'s bell balance = " + str(result[0][0]))
        else:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT balance FROM economy WHERE client_id = " + str(member.id))
            result = mycursor.fetchall()
            await ctx.send(str(member) + "'s bell balance = " + str(result[0][0]))


def setup(bot):
    bot.add_cog(economy(bot))
