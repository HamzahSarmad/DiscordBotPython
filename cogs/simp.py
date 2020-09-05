from discord.ext import commands
import discord
import re
import sqlite3

#Access db
mydb = sqlite3.connect("cogs/userlevels.db")

class simp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="enlighten",aliases=["Enlighten","E"],pass_context=True)
    async def enlighten(self, ctx):
        await ctx.send("'To simp or not to simp, that is the question: Whether 'tis nobler in the mind to suffer The denials and heartbreaks of non-queen Bitches, Or to take arms against a sea of self-doubt, And by opposing end them. To piss—to shit, No more; and by a shit to say we cause The heart-ache and the thousand natural Cummies that bussy (boy pussy) is heir to: 'tis a Queen Devoutly to be fucked. To piss, to shit; To shit, perchance to cum— Ayyyyyyy, there's the rub: For in that piss and shit what dreams may cum, When we have jacked off this immoral erection, Must give us puss—there's the respect That makes clammy titties of so long life. For who would bear the whips and scorns of Cock and ball torture, The cuck’s wrong , the proud man's condom, The pangs of virginity, the chad’s delay, The insolence of bad little girls for daddy, and The spurns that patience merit of the Cumguzzling little slut takes, When he himself might his cuck fetish make With a bare cock in? Who would infidels watch, To grunt and sweat under another wife, But that the dread of something after a date, The undiscovered country, from whose porn No simp returns, puzzles the will, And makes us rather game and act gangsta Than fly to others that we know not of? Thus simping does make cowards of us all, And thus the peepee poopoo of uh oh stinky Diaper Is sicklied o'er with the pale cast of Thought, and enterprises of great bitches and Moments with this regard their simping turn Awry and lose the game of seduction' -Keith 2020")

    @commands.command(name="simpy",aliases=["Simpy"],pass_context=True)
    @commands.has_permissions(administrator=True)
    async def simpy(self, ctx, member: discord.User):
        cursor = mydb.cursor()
        cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        if len(result) == 0:
            print("User not in database")
            cursor.execute("INSERT INTO simpcounter VALUES(" + str(member.id) + "," + "1)")
            mydb.commit()
            embed = discord.Embed(title="SimpBot", description="Simp counter has increased to 1", colour=0x66ff33)
            await ctx.send(embed=embed)
            print("User added to db")
        else:
            newcount = result[0][0] + 1
            cursor.execute("UPDATE simpcounter SET counter = " + str(newcount) + " WHERE client_id = " + str(member.id))
            mydb.commit()
            await ctx.send(str(member) + "'s simpcount has increased to " + str(newcount))

    @commands.command(name="desimp",aliases=["Desimp","dsimp","Dsimp"],pass_context=True)
    @commands.has_permissions(administrator=True)
    async def desimp(self, ctx, member: discord.User):
        cursor = mydb.cursor()
        cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(member.id))
        result = cursor.fetchall()
        if len(result) == 0:
            print("User not in database")
            await ctx.send(str(member) + "'s simp counter is currently zero")
        else:
            newcount = result[0][0] - 1
            cursor.execute("UPDATE simpcounter SET counter = " + str(newcount) + " WHERE client_id = " + str(member.id))
            mydb.commit()
            await ctx.send(str(member.id) + "'s simpcounter has decreased to " + str(newcount))

    @commands.command(name="simpcount",aliases=["Simpcounter","simcounter","sc","SC","Sc","Simpcount"])
    async def simpcount(self, ctx, member: discord.User):
        if not member:
            cursor = mydb.cursor()
            cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(ctx.message.author.id))
            result = cursor.fetchall()
            if len(result) == 0:
                await ctx.send("<@" + str(ctx.message.author.id) + "> simp count: 0")
            else:
                await ctx.send("<@" + str(ctx.message.author.id) + "> simp count: " + str(result[0][0]))
        else:
            cursor = mydb.cursor()
            cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(member.id))
            result = cursor.fetchall()
            if len(result) == 0:
                await ctx.send(str(member) + "'s simp count: 0")
            else:
                await ctx.send(str(member) + "'s simp count: " + str(result[0][0]))

def setup(bot):
    bot.add_cog(simp(bot))
