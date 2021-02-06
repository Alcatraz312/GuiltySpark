import discord
from discord.ext import commands
import random
import asyncpraw

reddit = asyncpraw.Reddit(client_id="a4N80AQ_USBGgQ",
                     client_secret="PHsGECOOvLD4OLwJspSNl1XwKQTs3g",
                     user_agent="python script")

client = commands.Bot(command_prefix="g!")
@client.event
async def on_ready():
    print("Your bot is ready")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hey there! , I am Guilty Spark , I was created by @Alcatraz b312 using Python")

@client.command()
async def creator(ctx):
    await ctx.send('<@669574365267886130> created me')

@client.command()
async def say(ctx,*,arg):
    await ctx.send(arg)

@client.command()
async def cya(ctx):
    await ctx.send("Bye!")

def to_upper(argument):
    return argument.upper()

@client.command()
async def bold(ctx, *, content: to_upper):
    await ctx.send(content)

@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def servers(ctx):
    await ctx.send("I am currently active in 3 servers")

@client.command()
async def memes(ctx, amount:int = 5):
    subreddit = await reddit.subreddit("memes")
    a = []
    top = subreddit.top(limit = amount)
    for submission in top:
        a.append(submission)
        random_sub = random.choice(a)
        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title = name)
        em.set_image(url = url)

        await ctx.send(embed = em)

client.run("Nzk4MDU3NjE4OTI4OTU5NDg4.X_vfEw.xs8zT_3NyJ9C7Xy67hQPKzzNQfQ")
