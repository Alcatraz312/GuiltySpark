import discord
from discord.ext import commands
client = commands.Bot(command_prefix="g!")
@client.event
async def on_ready():
    print("Your bot is ready")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hey there! , I am Guilty Spark , I was created by @Alcatraz b312 using Python")
@client.command()
async def Bff(ctx):
    await ctx.send("My Best friend is Botube")
@client.command()
async def creator(ctx):
    await ctx.send('<@669574365267886130> created me')
@client.command()
async def say(ctx,*,arg):
    await ctx.send(arg)
@client.command()
async def yo(ctx):
    await ctx.send("yo fellas , wassup")
@client.command()
async def cya(ctx):
    await ctx.send("Bye!")
client.run("Nzk4MDU3NjE4OTI4OTU5NDg4.X_vfEw.xs8zT_3NyJ9C7Xy67hQPKzzNQfQ")