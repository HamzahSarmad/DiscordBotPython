from discord.ext import commands
from discord.ext.commands import *
import praw
import random
import discord
import mysql.connector
import re

#Access db
mydb = mysql.connector.connect(
    host="HOST",
    user="USER",
    passwd="PASSWORD",
    database="DATBASE",
    auth_plugin="mysql_native_password"
)
#Generates a random amount of xp on every message
def generateXP():
    return random.randint(1,15)


#Searching for the correct subreddits
reddit = praw.Reddit(client_id="CLIENT_ID",
                    client_secret="CLIENT_SECRET",
                    user_agent="USER_AGENT")
#Sets bots prefix
bot = commands.Bot(command_prefix="-")

#Print to console that bot is online
@bot.event
async def on_ready():
    print("Bot is online!")
    print(mydb)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        xp = generateXP()
        print(message.author.name + " will receive " + str(xp) + "xp")
        cursor = mydb.cursor()
        cursor.execute("SELECT user_xp, user_level FROM users WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if len(result) == 0:
            print("User not in database")
            cursor.execute("INSERT INTO users VALUES(" + str(message.author.id) + "," + str(xp) + ", 1)")
            mydb.commit()
            embed = discord.Embed(title="SimpBot", description="Congrats you leveled up to level 1!", colour=0x66ff33)
            await message.channel.send(embed=embed)
            print("User added to db")
        else:
            newXP = result[0][0] + xp
            currentLevel = result[0][1]
            #print("New xp: " + str(newXP))
            #print("Current Level: " + str(currentLevel))
            flag = False
            if newXP < 50:
                currentLevel = 1
            elif newXP > 50 and newXP <= 100:
                if currentLevel != 2:
                    flag = True
                currentLevel = 2
            elif newXP > 100 and newXP <= 175:
                if currentLevel != 3:
                    flag = True
                currentLevel = 3
            elif newXP > 175 and newXP <= 275:
                if currentLevel != 4:
                    flag = True
                currentLevel = 4
            elif newXP > 275 and newXP <= 400:
                if currentLevel != 5:
                    flag = True
                currentLevel = 5
            elif newXP > 400 and newXP <= 600:
                if currentLevel != 6:
                    flag = True
                currentLevel = 6
            elif newXP > 600 and newXP <= 825:
                if currentLevel != 7:
                    flag = True
                currentLevel = 7
            elif newXP > 825 and newXP <= 1075:
                if currentLevel != 8:
                    flag = True
                currentLevel = 8
            elif newXP > 1075 and newXP <= 1350:
                if currentLevel != 9:
                    flag = True
                currentLevel = 9
            elif newXP > 1350:
                if currentLevel != 10:
                    flag = True
                currentLevel = 10
            
            cursor.execute("UPDATE users SET user_xp = " + str(newXP) + ", user_level = " + str(currentLevel) + " WHERE client_id = " + str(message.author.id))
            mydb.commit()
            #print("Updated...")

            if flag:
                embed = discord.Embed()
                embed.set_author(name="SimpBot")
                embed.colour=0x66ff33
                embed.description = message.author.name + " leveled up to " + str(currentLevel)
                await message.channel.send(embed=embed)
    await bot.process_commands(message)
    
@bot.command(name="commands",aliases=["Commands","Command","command"],pass_context=True)
async def commands(ctx):
    embed = discord.Embed(title="Commands",description="List of commands")
    embed.add_field(name="Commands",value="-command")
    embed.add_field(name="Info",value="-info",inline=True)
    embed.add_field(name="Ping",value="-Ping",inline=True)
    embed.add_field(name="Owner",value="-owner",inline=True)
    embed.add_field(name="8Ball",value="-8ball",inline=True)
    embed.add_field(name="Simp",value="-simp",inline=True)
    embed.add_field(name="Whiteknight",value="-whiteknight",inline=True)
    embed.add_field(name="Wholesome", value="-wholesome",inline=True)
    embed.add_field(name="meme",value="-meme",inline=True)
    embed.add_field(name="Aww",value="-aww",inline=True)
    embed.add_field(name="Enlighten", value="-enligten",inline=True)
    embed.add_field(name="Level", value="-level",inline=True)
    embed.add_field(name="XP", value="-xp",inline=True)
    await ctx.send("Currently there are the following commands: ")
    await ctx.send(embed=embed)
@bot.command(name="Acommands",aliases=["Admin","ACommands","Admincommands"],pass_context=True)
@has_permissions(administrator=True)
async def Acommmands(ctx):
    embed = discord.Embed(title="Commands",description="List of Admin Commands")
    embed.add_field(name="Simpcount",value="-simpcount",inline=True)
    embed.add_field(name="Simpy",value="-simpy",inline=True)
    embed.add_field(name="Desimp",value="-desimp",inline=True)
    await ctx.send("Current Admin Commands")
    await ctx.send(embed=embed)
@bot.command(name="enlighten",aliases=["Enlighten","E"],pass_context=True)
async def enlighten(ctx):
    await ctx.send("'To simp or not to simp, that is the question: Whether 'tis nobler in the mind to suffer The denials and heartbreaks of non-queen Bitches, Or to take arms against a sea of self-doubt, And by opposing end them. To piss—to shit, No more; and by a shit to say we cause The heart-ache and the thousand natural Cummies that bussy (boy pussy) is heir to: 'tis a Queen Devoutly to be fucked. To piss, to shit; To shit, perchance to cum— Ayyyyyyy, there's the rub: For in that piss and shit what dreams may cum, When we have jacked off this immoral erection, Must give us puss—there's the respect That makes clammy titties of so long life. For who would bear the whips and scorns of Cock and ball torture, The cuck’s wrong , the proud man's condom, The pangs of virginity, the chad’s delay, The insolence of bad little girls for daddy, and The spurns that patience merit of the Cumguzzling little slut takes, When he himself might his cuck fetish make With a bare cock in? Who would infidels watch, To grunt and sweat under another wife, But that the dread of something after a date, The undiscovered country, from whose porn No simp returns, puzzles the will, And makes us rather game and act gangsta Than fly to others that we know not of? Thus simping does make cowards of us all, And thus the peepee poopoo of uh oh stinky Diaper Is sicklied o'er with the pale cast of Thought, and enterprises of great bitches and Moments with this regard their simping turn Awry and lose the game of seduction' -Keith 2020")
#Gives the bots info
@bot.command(name="info",aliases=["Info"],pass_context=True)
async def info(ctx):
    await ctx.send(f"Hey {ctx.message.author.name} {bot.user} is your average Bot which is currently connected to {ctx.guild.name}")
#Pulls a post from a subreddit and sends the link to the channel
@bot.command(name="simp",aliases=["Simp"],pass_context=True)
async def simp(ctx):
    simpPosts = list()
    for submission in reddit.subreddit("TheSimpPolice").hot(limit=50):
        simpPosts.append(submission.url)
    await ctx.send(random.choice(simpPosts))
@bot.command(name="aww",aliases=["Aww","aw","Aw","Awww","awww"],pass_context=True)
async def aww(ctx):
    awwPosts = list()
    for submission in reddit.subreddit("aww").hot(limit=50):
        awwPosts.append(submission.url)
    await ctx.send(random.choice(awwPosts))
@bot.command(name="wholesome",aliases=["Wholesome"],pass_context=True)
async def wholesome(ctx):
    wholesomePosts = list()
    for submission in reddit.subreddit("wholesomememes").hot(limit=50):
        wholesomePosts.append(submission.url)
    await ctx.send(random.choice(wholesomePosts))
@bot.command(name="owner", aliases=["Owner","Boss","Senpai"],pass_context=True)
async def owner(ctx):
    await ctx.send(f"The owner of {ctx.guild.name} is {ctx.guild.owner.name}")
#Pulls a post from a subreddit and sends the link to the channel
@bot.command(name="whiteknight", aliases=["Whiteknight","wk","WK","Wk","wK"],pass_context=True)
async def whiteknight(ctx):
    whiteknightPosts = list()
    for submission in reddit.subreddit("Whiteknighting").hot(limit=50):
        whiteknightPosts.append(submission.url)
    await ctx.send(random.choice(whiteknightPosts))
@bot.command(name="meme",aliases=["Meme"],pass_context=True)
async def meme(ctx):
    subreddits = ["dankmemes", "BlackPeopleTwitter","CrackheadCraigslist"]
    memeSubreddit = random.choice(subreddits)
    memePosts = list()
    for submission in reddit.subreddit(memeSubreddit).hot(limit=50):
        memePosts.append(submission.url)
    await ctx.send(random.choice(memePosts))
@bot.command(name="ping", aliases=["Ping"],pass_context=True)
#Simple ping to test latency
async def ping(ctx):
    await ctx.send("Pong {0}ms".format(round(bot.latency, 3)))
@bot.command(name="eightball",aliases=["8ball","8-ball","eight_ball","Eightball","Eight_ball"],pass_context=True)
async def eightball(ctx):
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
@bot.command(name="myinfo",aliases=["Myinfo","MyInfo","whoami"],pass_context=True)
async def myinfo(ctx):
    embed=discord.Embed(name="{ctx.message.author.name}",description="Here is all of the info I found")
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.add_field(name="Name: ",value=ctx.message.author.name,inline=True)
    embed.add_field(name="ID: ",value=ctx.message.author.id,inline=True)
    embed.add_field(name="Role: ",value=ctx.message.author.top_role,inline=False)
    embed.add_field(name="Joined: ",value=ctx.message.author.joined_at,inline=False)
    await ctx.send(embed=embed)
@bot.command(name="level", aliases=["Level","lvl","Lvl"],pass_context=True)
async def level(ctx):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT user_level FROM users WHERE client_id = " + str(ctx.message.author.id))
    result = mycursor.fetchone()
    await ctx.send(f"{ctx.message.author.name} is currrently level " + str(result[0]))
@bot.command(name="xp", aliases=["XP","Xp","Exp","exp"],pass_context=True)
async def xp(ctx):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT user_xp FROM users WHERE client_id = " + str(ctx.message.author.id))
    result = mycursor.fetchone()
    await ctx.send(f"{ctx.message.author.name} currently has " + str(result[0]) + "xp")
@bot.command(name="simpy",aliases=["Simpy"],pass_context=True)
@has_permissions(administrator=True)
async def simpy(ctx):
    userid = re.sub("[^0-9]","",str(ctx.message.content))
    cursor = mydb.cursor()
    cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(userid))
    result = cursor.fetchall()
    if len(result) == 0:
        print("User not in database")
        cursor.execute("INSERT INTO simpcounter VALUES(" + str(userid) + "," + "1)")
        mydb.commit()
        embed = discord.Embed(title="SimpBot", description="Simp counter has increased to 1", colour=0x66ff33)
        await ctx.send(embed=embed)
        print("User added to db")
    else:
        newcount = result[0][0] + 1
        cursor.execute("UPDATE simpcounter SET counter = " + str(newcount) + " WHERE client_id = " + str(userid))
        mydb.commit()
        await ctx.send("<@" + str(userid) + ">'s simpcounter has increased to " + str(newcount))
@bot.command(name="desimp",aliases=["Desimp","dsimp","Dsimp"],pass_context=True)
@has_permissions(administrator=True)
async def desimp(ctx):
    userid = re.sub("[^0-9]","",str(ctx.message.content))
    cursor = mydb.cursor()
    cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(userid))
    result = cursor.fetchall()
    if len(result) == 0:
        print("User not in database")
        await ctx.send(str(userid) + "'s simp counter is currently zero")
    else:
        newcount = result[0][0] - 1
        cursor.execute("UPDATE simpcounter SET counter = " + str(newcount) + " WHERE client_id = " + str(userid))
        mydb.commit()
        await ctx.send("<@" + str(userid) + ">'s simpcounter has decreased to " + str(newcount))
@bot.command(name="simpcount",aliases=["Simpcounter","sc","SC","Sc"])
async def simpcount(ctx):
    userid = re.sub("[^0-9]","",str(ctx.message.content))
    cursor = mydb.cursor()
    cursor.execute("SELECT counter FROM simpcounter WHERE client_id = " + str(userid))
    result = cursor.fetchall()
    await ctx.send("<@" + str(userid) + "> simp count: " + str(result[0][0]))

bot.run("TOKEN")

# 1 - 50 - lvl 1
# 51 - 100 - lvl2
# 101 - 175 - lvl3
# 176 - 275 - lvl4
# 276 - 400 - lvl5
# 401 - 600 - lvl6
# 601 - 825 - lvl7
# 826 - 1075 - lvl8
# 1076 - 1350 - lvl9
# 1351 - 1650 - lvl10
