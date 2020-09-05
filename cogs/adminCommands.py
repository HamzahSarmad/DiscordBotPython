from discord.ext import commands
import discord

class adminCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="load",aliases=["Load"],pass_content=True)
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, *,module : str):
        try:
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send(e, delete_after=5)
    
    @commands.command(aliases=['purge','wipe'], pass_context=True)
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"{amount-1} has been purged from the chat.", delete_after=5)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please specify an amount of messages to delete.", delete_after=5)

def setup(bot):
    bot.add_cog(adminCommands(bot))
