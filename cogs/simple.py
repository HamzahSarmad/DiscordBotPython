from discord.ext import commands
import discord
import random

class simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="myinfo",aliases=["Myinfo","MyInfo","whoami"],pass_context=True)
    async def myinfo(self, ctx):
        embed=discord.Embed(name="{ctx.message.author.name}",description="Here is all of the info I found")
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="Name: ",value=ctx.message.author.name,inline=True)
        embed.add_field(name="ID: ",value=ctx.message.author.id,inline=True)
        embed.add_field(name="Role: ",value=ctx.message.author.top_role,inline=False)
        embed.add_field(name="Joined: ",value=ctx.message.author.joined_at,inline=False)
        await ctx.send(embed=embed)
    @commands.command(name="cmds",aliases=["Commands","Command","command","commmands","help","Help"],pass_context=True)
    async def cmds(self, ctx):
        embed = discord.Embed(title="Commands",description="List of commands")
        embed.add_field(name="Commands",value="`-command`",inline=True)
        embed.add_field(name="Info",value="`-info`",inline=True)
        embed.add_field(name="Ping",value="`-ping`",inline=True)
        embed.add_field(name="Owner",value="`-owner`",inline=True)
        embed.add_field(name="8Ball",value="`-8ball`",inline=True)
        embed.add_field(name="Bells",value="`-bell (@user)`", inline=True)
        embed.add_field(name="Simp",value="`-simp`",inline=True)
        embed.add_field(name="Whiteknight",value="`-whiteknight`",inline=True)
        embed.add_field(name="Wholesome", value="`-wholesome`",inline=True)
        embed.add_field(name="meme",value="`-meme`",inline=True)
        embed.add_field(name="Aww",value="`-aww`",inline=True)
        embed.add_field(name="Inspirome",value="`-inspirome`",inline=True)
        embed.add_field(name="Enlighten", value="`-enlighten`",inline=True)
        embed.add_field(name="Level", value="`-level`",inline=True)
        embed.add_field(name="XP", value="`-xp`",inline=True)
        embed.add_field(name="Simpcount",value="`-simpcount`",inline=True)
        await ctx.send("Currently there are the following commands: ")
        await ctx.send(embed=embed)
    @commands.command(name="Acommands",aliases=["Admin","ACommands","Admincommands","acommands","acmds","Acmds"],pass_context=True)
    @commands.has_permissions(administrator=True)
    async def Acommmands(self, ctx):
        embed = discord.Embed(title="Commands",description="List of Admin Commands")
        embed.add_field(name="Simpy",value="`-simpy`",inline=True)
        embed.add_field(name="Desimp",value="`-desimp`",inline=True)
        await ctx.send("Current Admin Commands")
        await ctx.send(embed=embed)
    #Gives the bots info
    @commands.command(name="info",aliases=["Info"],pass_context=True)
    async def info(self, ctx):
        await ctx.send(f"Hey {ctx.message.author.name} {self.bot.user} is your average Bot which is currently connected to {ctx.guild.name}")
    @commands.command(name="owner", aliases=["Owner","Boss","Senpai"],pass_context=True)
    async def owner(self, ctx):
        await ctx.send(f"The owner of {ctx.guild.name} is {ctx.guild.owner.name}")
    @commands.command(name="ping", aliases=["Ping"],pass_context=True)
    #Simple ping to test latency
    async def ping(self, ctx):
        await ctx.send("Pong {0}ms".format(round(self.bot.latency, 3)))
    @commands.command(name="eightball",aliases=["8ball","8-ball","eight_ball","Eightball","Eight_ball"],pass_context=True)
    async def eightball(self, ctx):
        ballanswers = ["As I see it, yes.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don’t count on it.",
                    "It is certain.",
                    "It is decidedly so.",
                    "Most likely.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Outlook good.",
                    "Reply hazy, try again.",
                    "Signs point to yes.",
                    "Very doubtful.",
                    "Without a doubt.",
                    "Yes.",
                    "Yes – definitely.",
                    "You may rely on it."]
        await ctx.send(random.choice(ballanswers))
    @commands.command(name="keith",aliases=["Keith"],pass_context=True)
    async def keith(self, ctx):
        await ctx.send("Keeto")

def setup(bot):
    bot.add_cog(simple(bot))
