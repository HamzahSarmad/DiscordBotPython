from discord.ext import commands
import sqlite3

#Access db
mydb = sqlite3.connect("cogs/userlevels.db")

class level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="level", aliases=["Level","lvl","Lvl"],pass_context=True)
    async def level(self, ctx):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT user_level FROM users WHERE client_id = " + str(ctx.message.author.id))
        result = mycursor.fetchone()
        await ctx.send(f"{ctx.message.author.name} is currrently level " + str(result[0]))
        
    @commands.command(name="xp", aliases=["XP","Xp","Exp","exp"],pass_context=True)
    async def xp(self, ctx):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT user_xp FROM users WHERE client_id = " + str(ctx.message.author.id))
        result = mycursor.fetchone()
        await ctx.send(f"{ctx.message.author.name} currently has " + str(result[0]) + "xp")


def setup(bot):
    bot.add_cog(level(bot))