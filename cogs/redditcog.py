from discord.ext import commands
import praw
import random
import discord

#connecting to reddit
reddit = praw.Reddit(client_id="",
                    client_secret="",
                    user_agent="")
class redditcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Pulls a post from a subreddit and sends the link to the channel
    @commands.command(name="simp",aliases=["Simp"],pass_context=True)
    async def simp(self, ctx):
        simpPosts = list()
        for submission in reddit.subreddit("TheSimpPolice").new(limit=50):
            simpPosts.append(submission.url)
        await ctx.send(random.choice(simpPosts))
    @commands.command(name="aww",aliases=["Aww","aw","Aw","Awww","awww"],pass_context=True)
    async def aww(self, ctx):
        awwPosts = list()
        for submission in reddit.subreddit("aww").new(limit=50):
            awwPosts.append(submission.url)
        await ctx.send(random.choice(awwPosts))
    @commands.command(name="wholesome",aliases=["Wholesome"],pass_context=True)
    async def wholesome(self, ctx):
        wholesomePosts = list()
        for submission in reddit.subreddit("wholesomememes").new(limit=50):
            wholesomePosts.append(submission.url)
        await ctx.send(random.choice(wholesomePosts))
    @commands.command(name="whiteknight", aliases=["Whiteknight","wk","WK","Wk","wK"],pass_context=True)
    async def whiteknight(self, ctx):
        whiteknightPosts = list()
        for submission in reddit.subreddit("Whiteknighting").new(limit=50):
            whiteknightPosts.append(submission.url)
        await ctx.send(random.choice(whiteknightPosts))
    @commands.command(name="meme",aliases=["Meme"],pass_context=True)
    async def meme(self, ctx):
        subreddits = ["dankmemes", "BlackPeopleTwitter","CrackheadCraigslist"]
        memeSubreddit = random.choice(subreddits)
        memePosts = list()
        for submission in reddit.subreddit(memeSubreddit).new(limit=50):
            memePosts.append(submission.url)
        await ctx.send(random.choice(memePosts))
    @commands.command(name="inspirome",aliases=["Inspirome","inspire","Inspire"],pass_context=True)
    async def inspirome(self, ctx):
        inspiromePosts = list()
        for submission in reddit.subreddit("inspirobot").new(limit=50):
            inspiromePosts.append(submission.url)
        embed = discord.Embed()
        embed.set_image(url=f"{random.choice(inspiromePosts)}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(redditcog(bot))
