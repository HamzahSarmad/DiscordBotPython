from discord.ext import commands
import discord
import smtplib

class bugSplat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bug",aliases=["Bug"],pass_context=True)
    async def bug(self, ctx, bugMessage : str):
        content = bugMessage
        mail = smtplib.SMTP("*****", 0000)
        mail.ehlo()
        mail.starttls()
        mail.login("EMAIL","PASSWORD")
        mail.sendmail("EMAIL", "EMAIL", content)
        mail.close
        await ctx.send("Bug has been reported :thumbsup:")




def setup(bot):
    bot.add_cog(bugSplat(bot))
