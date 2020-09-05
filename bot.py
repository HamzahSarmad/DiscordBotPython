import discord
from discord.ext import commands
import random
import math
from datetime import datetime
import sqlite3

#Access db
mydb = sqlite3.connect("cogs/userlevels.db")

#Generates a random amount of xp on every message between 1 and 15
def generateXP():
    return random.randint(1,15)

def generateBells():
    return random.randint(1,3)

#Sets bots prefix
bot = commands.Bot(command_prefix="-")
#Removes in-built help command
bot.remove_command("help")

#Print to console when bot is online
@bot.event
async def on_ready():
    print("Bot is online!")
    print(mydb)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        # LOGS CHANNEL
        channel = discord.utils.get(message.guild.text_channels, name="logs")
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
        embed = discord.Embed(title=message.author.name,description=currentTime)
        embed.add_field(name="user id: ", value=message.author.id, inline=False)
        embed.add_field(name="Channel",value=message.channel.name,inline=False)
        embed.add_field(name="Message",value=message.content,inline=False)
        embed.set_footer(text="Message Sent")
        await channel.send(embed=embed)

        # XP / ECO
        xp = generateXP()
        bell = generateBells()
        print(message.author.name + " will receive " + str(xp) + "xp")
        print(message.author.name + " will receive " + str(bell) + " bells")

        cursor = mydb.cursor()
        cursor.execute("SELECT user_xp, user_level FROM users WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        cursor.execute("SELECT balance from Economy WHERE client_id = " + str(message.author.id))
        bellResult = cursor.fetchall()

        if len(result) == 0:
            print("User not in database")
            cursor.execute("INSERT INTO users VALUES(" + str(message.author.id) + "," + str(xp) + ", 1)")
            mydb.commit()
            embed = discord.Embed(title="Level up!", description="`Congrats you leveled up to level 1!`", colour=0x66ff33)
            await message.channel.send(embed=embed)
            print("User added to db")
        else:
            newXP = result[0][0] + xp
            currentLevel = result[0][1]
            newLevel = math.floor(newXP ** (1/4))
            cursor.execute("UPDATE users SET user_xp = " + str(newXP) + ", user_level = " + str(newLevel) + " WHERE client_id = " + str(message.author.id))
            mydb.commit()

            if newLevel > currentLevel:
                embed = discord.Embed()
                embed.set_author(name="SimpBot")
                embed.colour=0x66ff33
                embed.description = message.author.name + " leveled up to " + str(currentLevel)
                await message.channel.send(embed=embed)

        if len(bellResult) == 0:
            print("User not in db")
            cursor.execute("INSERT INTO Economy VALUES(" + str(message.author.id) + ", 0)")
            mydb.commit()
            print("User added to db")
        else:
            newBell = bellResult[0][0] + bell
            cursor.execute("UPDATE Economy SET balance = " + str(newBell) + " WHERE client_id = " + str(message.author.id))
            mydb.commit()
    await bot.process_commands(message)

@bot.event
async def on_message_delete(message):
    if message.author.bot:
        return
    else:
        # LOGS DELETED MESSAGES CHANNEL
        channel = discord.utils.get(message.guild.text_channels, name="logs")
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")

        embed = discord.Embed(title=message.author.name,description=currentTime)
        embed.add_field(name="user id: ", value=message.author.id, inline=False)
        embed.add_field(name="Channel",value=message.channel.name,inline=False)
        embed.add_field(name="Message Deleted",value=message.content,inline=False)
        embed.set_footer(text="Message Deleted")
        await channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        # LOGS EDITED MESSAGES CHANNEL
        channel = discord.utils.get(before.guild.text_channels, name="logs")
        now = datetime.now()
        currentTime = now.strftime("%d/%m/%Y %H:%M:%S")
        
        embed = discord.Embed(title=before.author.name,description=currentTime)
        embed.add_field(name="user id: ", value=before.author.id, inline=False)
        embed.add_field(name="Channel",value=before.channel.name,inline=False)
        embed.add_field(name="Before",value=before.content,inline=False)
        embed.add_field(name="After",value=after.content,inline=False)
        embed.set_footer(text="Message Edited")
        await channel.send(embed=embed)

#Attempts to reload cogs without having to restart bot.
@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, cog):
    try:
        bot.unload_extension(f"cogs.{cog}")
        bot.load_extension(f"cogs.{cog}")
        # Alerts the chat where the command was sent, that the Cog has been reloaded.
        await ctx.send(f"{cog} has been reloaded.", delete_after=10)
    except Exception as e:
        channel = bot.get_channel(711363906492432394)
        await channel.send(f"Cog: {cog} did not start up properly, restart the bot completely. <@&440571822879145984>")
        raise e


extensions = ["cogs.simp","cogs.simple","cogs.redditcog","cogs.level","cogs.economy","cogs.adminCommands","cogs.bugSplat","cogs.weather","cogs.tronald"]

for ext in extensions:
    bot.load_extension(ext)
    
bot.run("TOKEN")
