from discord.ext import commands
from discord.ext.commands import Bot
import praw
import random

reddit = praw.Reddit(client_id="****",
                    client_secret="****",
                    user_agent="simpbot")
whiteknightSubreddit = reddit.subreddit("Whiteknighting")
simpSubreddit = reddit.subreddit("TheSimpPolice")
awwSubreddit = reddit.subreddit("aww")

simpPosts = list()
whiteknightPosts = list()
awwPosts = list()

for submission in whiteknightSubreddit.hot(limit=25):
    whiteknightPosts.append(submission.url)
for submission in simpSubreddit.hot(limit=25):
    simpPosts.append(submission.url)
for submission in awwSubreddit.hot(limit=25):
    awwPosts.append(submission.url)

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_message(message):
    if "simp" in message.content:
        if message.author.bot == True:
            return
        elif message.author.bot == False:
            await message.channel.send("To simp or not to simp, that is the question: Whether 'tis nobler in the mind to suffer The denials and heartbreaks of non-queen Bitches, Or to take arms against a sea of self-doubt, And by opposing end them. To piss—to shit, No more; and by a shit to say we cause The heart-ache and the thousand natural Cummies that bussy (boy pussy) is heir to: 'tis a Queen Devoutly to be fucked. To piss, to shit; To shit, perchance to cum— Ayyyyyyy, there's the rub: For in that piss and shit what dreams may cum, When we have jacked off this immoral erection, Must give us puss—there's the respect That makes clammy titties of so long life. For who would bear the whips and scorns of Cock and ball torture, The cuck’s wrong , the proud man's condom, The pangs of virginity, the chad’s delay, The insolence of bad little girls for daddy, and The spurns that patience merit of the Cumguzzling little slut takes, When he himself might his cuck fetish make With a bare cock in? Who would infidels watch, To grunt and sweat under another wife, But that the dread of something after a date, The undiscovered country, from whose porn No simp returns, puzzles the will, And makes us rather game and act gangsta Than fly to others that we know not of? Thus simping does make cowards of us all, And thus the peepee poopoo of uh oh stinky Diaper Is sicklied o'er with the pale cast of Thought, and enterprises of great bitches and Moments with this regard their simping turn Awry and lose the game of seduction")
    elif message.content.startswith("-Simp"):
        await message.channel.send(random.choice(simpPosts))
    elif message.content.startswith("-Commands"):
        await message.channel.send("Currently there are 3 commands:\n-info\n-simp\n-whiteknight\n")
    elif message.content.startswith("-Whiteknight"):
        await message.channel.send(random.choice(whiteknightPosts))
    elif message.content.startswith("-Info"):
        await message.channel.send(f"{bot.user} is the bot for all your simp/whiteknight needs")
    elif message.content.startswith("-aww"):
        await message.channel.send(random.choice(awwPosts))
    
bot.run("****")
