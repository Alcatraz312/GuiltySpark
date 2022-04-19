import discord
from discord import channel
from discord.embeds import EmbedProxy
from discord.ext import commands , tasks
import random
import youtube_dl
from discord.voice_client import VoiceClient
import asyncio
from youtube_dl import YoutubeDL
import praw
import os
import math
import aiosqlite
from dotenv import dotenv_values

config = dotenv_values(".env")


client = commands.Bot(command_prefix="g!")

#custom help command
client.remove_command("help")

@client.group(inwoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "help" , description = "use  g!help <command> for extended information on a command." , color = ctx.author.color)
    em.add_field(name = "Fun" , value = "say , ping , upcase , choose")
    em.add_field(name = "Server" , value = "creator , joined , server , servers , members , github")
    em.add_field(name = "Level" , value = "stats , leaderboard")
    em.add_field(name = "Music" , value = "play , stop , queue , view , pause , leave , remove")
    em.add_field(name = "Moderation" , value = "kick , ban")

    await ctx.send(embed = em)

@help.command()
async def say(ctx):
    em = discord.Embed(title = "say" , description = "Repeats the sentence wrote by the user" , color = ctx.author.color)
    em.add_field(name= "**Syntax**" , value = "g!say <text>")
    await ctx.send(embed = em)
@help.command()
async def ping(ctx):
    em = discord.Embed(title = "ping" , description = "Shows the ping" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def bold(ctx):
    em = discord.Embed(title = "bold" , description = "Changes the case of the sentence to bold." , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!bold <text>")
    await ctx.send(embed = em)
@help.command()
async def creator(ctx):
    em = discord.Embed(title = "creator" , description = "Creator of this bot" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def joined(ctx):
    em = discord.Embed(title = "joined" , description = "Shows the time and date of join of a member in this server" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!joined <name of the member or member mention>")
    await ctx.send(embed = em)
@help.command()
async def server(ctx):
    em = discord.Embed(title = "server" , description = "server of origin" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def servers(ctx):
    em = discord.Embed(title = "servers" , description = "Total number of servers using this bot" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def members(ctx):
    em = discord.Embed(title = "members" , description = "gives the total number of members in this server" , color = ctx.author.color)
    await ctx.send(embed=em)
@help.command()
async def stats(ctx):
    em  = discord.Embed(title = "stats" , description = "Shows the stats of the user in this server" , color = ctx.author.color)
    await ctx.send(embed=em)
@help.command()
async def leaderboard(ctx):
    em = discord.Embed(title = "leaderboard" , description = "shows the level leaderboard of members in this server" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def play(ctx):
    em = discord.Embed(title = "play" , description = "Plays the music requested by the user in the voice channel" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!play <link of the song>")
    await ctx.send(embed = em)
@help.command()
async def stop(ctx):
    em = discord.Embed(title = "stop" , description = "Stops the song currently being played in the voice channel" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def queue(ctx):
    em = discord.Embed(title = "queue" , description = "Add the song in the queue as requested by the user" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!queue <link of the song>")
    await ctx.send(embed = em)
@help.command()
async def view(ctx):
    em = discord.Embed(title = "view", description = "Shows the current music queue" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def pause(ctx):
    em = discord.Embed(title = "pause" , description = "Pauses the music currently playing in the voice channel" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def remove(ctx):
    em = discord.Embed(title = "remove" , description = "Removes the song from the queue" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def leave(ctx):
    em = discord.Embed(title = "leave" , description = "Makes the bot leave the voice channel" , color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def kick(ctx):
    em = discord.Embed(title = "kick" , description = "Kicks the mentioned user" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!kick <mention user> <reason>")
    await ctx.send(embed= em)
@help.command()
async def ban(ctx):
    em = discord.Embed(title = "ban" , description = "Bans the mentioned user" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!ban <mention user> <reason>")
    await ctx.send(embed = em)
@help.command()
async def choose(ctx):
    em = discord.Embed(title = "choose" , description = "Chooses between multiple choices" , color = ctx.author.color)
    em.add_field(name = "**Syntax**" , value = "g!choose <choice1> <choice2> .... <choice nth>" )
    await ctx.send(embed = em)
@help.command()
async def github(ctx):
    em = discord.Embed(title = "github" , description = "Sends the github repository link of this bot" , color = ctx.author.color)
    await ctx.send(embed = em)

#reddit connection
reddit = praw.Reddit(client_id = "BuL6vCcSuCfHGg",
                     client_secret = "lhdbXabYByoNVlsa-kD9iWGbVhAixQ",
                     username = "Alcatraz-b312",
                     password = "1234moyv",
                     user_agent = "pythonpraw")

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

#ffmpeg connection
ffmpeg_options = {
    'options': '-vn -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle,activity = discord.Game("g!help"))
    print("Your bot is ready")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hey there! , I am Guilty Spark , I was created by Alcatraz b312 using Python")

@client.command()
async def creator(ctx):
    await ctx.send('<@669574365267886130> created me')

@client.command(name = "say" , help = "This command makes the bot repeats the sentence")
async def say(ctx,*,arg):
    await ctx.send(arg)

def to_upper(argument):
    return argument.upper()

@client.command(name = "bold" , help ="This command converts into uppercase")
async def upcase(ctx, *, content: to_upper):
    await ctx.send(content)

@client.command(name = "joined" , help = "This command gives the date and time of join of a member")
async def joined(ctx, *, member: discord.Member):
    await ctx.send('{0} joined on {0.joined_at}'.format(member))

@client.command()
async def servers(ctx):
    await ctx.send("I'm in " + str(len(client.guilds)) + " servers!")

@client.command(name = "ping" , help = "Shows the latency")
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms ')

#music commands
@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()
queue = []
@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        


@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()
 
 
@client.command()
async def play(ctx, url=None):
    print('hello world')
    
    if not url: 
        await ctx.send('Enter a URL! (otherwise listen to this)')
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    
    user=ctx.author
    voice_channel=user.voice.channel
    channel=None
    # only play music if user is in a voice channel
    if voice_channel:
        # grab user's voice channel
        channel=voice_channel.name
        
        # create StreamPlayer
        
        if not ctx.voice_client:
      
            vc = await voice_channel.connect()

        
        voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
        
        if not voice.is_playing():
            
            YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
            with YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                print(2)

            URL = info['formats'][0]['url']
            print(3)
            voice.play(discord.FFmpegPCMAudio(URL))
            print(voice.is_playing())
            print("Strated playing")
            # Sleep while audio is playing.
            
            
        else:
            await ctx.send("Already playing song")
            return
    else:
        await ctx.send('User is not in a channel.')

@client.command()
async def deez_what(ctx):
    await ctx.send("deez nuts!!!")

#meme command
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    
    top = subreddit.top(limit = 1)
    
    for submission in top:
        all_subs.append(submission)
        
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url
        
        em = discord.Embed(title = name)
        em.set_image(url = url)

        await ctx.send(embed = em)


    
#server
@client.command()
async def server(ctx):
    await ctx.send("https://discord.gg/CwZzF7TAcX")

@client.command()
async def github(ctx):
    await ctx.send("https://github.com/Alcatraz312/GuiltySpark")

'''
#level up system

async def initialise():
    await client.wait_until_ready()
    client.db = await aiosqlite.connect("expdata.db")
    await client.db.execute("Create table if not exists guilddata (guild_id int , user_id int , exp int ,Primary Key(guild_id , user_id))")

client.multiplier = 1

@client.event
async def on_message(message):
    if not message.author.bot:
        cursor = await client.db.execute("Insert or ignore into guilddata (guild_id , user_id , exp) Values (? ,? ,?)" , (message.guild.id , message.author.id , 1))

        if cursor.rowcount == 0:
            await client.db.execute("Update guilddata set exp = exp + 1 where guild_id = ? and user_id = ? " , (message.guild.id , message.author.id))
            cur = await client.db.execute("Select exp from guilddata where guild_id = ? and user_id = ?", (message.guild.id , message.author.id))
            data = await cur.fetchone()
            exp = data[0]
            lvl = math.sqrt(exp)/client.multiplier

            if lvl.is_integer():
                await message.channel.send(f"{message.author.mention} great , you are now level {int(lvl)}.")
        
        await client.db.commit()

    await client.process_commands(message)

#check stats

@client.command()
async def stats(ctx , member: discord.member = None):
    if member is None : member = ctx.author 

    #get user exp
    async with client.db.execute("Select exp from guilddata where guild_id = ? and user_id = ?" , (ctx.guild.id , member.id)) as cursor:
        data = await cursor.fetchone()
        exp = data[0]
    
    #calculate rank 
    async with client.db.execute("select exp from guilddata where guild_id = ?" , (ctx.guild.id,)) as cursor:
        rank = 1
        async for value in cursor:
            if exp < value[0]:
                rank+=1

    lvl = int(math.sqrt(exp)//client.multiplier)

    current_lvl_exp = (client.multiplier * (lvl))**2
    next_lvl_exp = (client.multiplier * (lvl+1))**2

    lvl_percentage = ((exp - current_lvl_exp) / (next_lvl_exp - current_lvl_exp)) * 100

    embed = discord.Embed(title = f"Status for {member.name}" , colour = discord.Colour.red())
    embed.add_field(name = "Level" , value = str(lvl))
    embed.add_field(name = "Exp" , value = f"{exp}/{next_lvl_exp}")
    embed.add_field(name = "Rank" , value = f"{rank}/{ctx.guild.member_count}")
    embed.add_field(name  = "Level Progress" , value = f"{round(lvl_percentage , 2)}%")

    await ctx.send(embed = embed)

    
#leaderboard 
@client.command()
async def leaderboard(ctx):
    buttons = {}
    for i in range (1,6):
        buttons[f"{i}\N{COMBINING ENCLOSING KEYCAP}"] = i
    
    previous_page = 0
    current = 1
    index = 1
    entries_per_page = 10

    embed = discord.Embed(title = f"Leaderboard page {current} " , description = "" , colour = discord.Colour.red())
    msg = await ctx.send(embed = embed )

    for button in buttons:
        await msg.add_reaction(button)

    while True:
        if current != previous_page:
            embed.title = f"Leaderboard page {current}"
            embed.description = ""

            async with client.db.execute("select user_id , exp from guilddata where guild_id = ? order by exp desc limit ? offset ?" , (ctx.guild.id , entries_per_page , entries_per_page*(current - 1) , )) as cursor:
                index = entries_per_page * (current - 1)

                async for entry in cursor:
                    index+=1
                    member_id , exp = entry
                    member = ctx.guild.get_member(member_id)
                    embed.description += f"{index}) {member.mention} : {exp}\n"

                await msg.edit(embed = embed)
        
        try:
            reaction , user = await client.wait_for("reaction add" , check = lambda reaction , user: user == ctx.author and reaction.emoji in buttons , timeout = 60.0)

        except asyncio.TimeoutError:
            return await msg.clear_reactions()
        
        else:
            previous_page = current
            await msg.remove_reaction(reaction.emoji , ctx.author)
            current = buttons[reaction.emoji]
'''
#total members in the server
@client.command()
async def members(ctx):
    await ctx.send("There are currently "+ str(ctx.guild.member_count) +" members in this server.")


@client.command()
async def choose(ctx , *choices : str):
    await ctx.send(random.choice(choices))

'''
#kick and ban

@client.command()
async def kick(ctx, member : discord.Member,*, reason = None):       #we put "*" here in order to able to make spaces between the words of reason
    await member.kick(reason = reason)

@client.command()
async def ban(ctx, member : discord.Member,* , reason = None):
    await member.ban(reason = reason)
'''

'''
client.loop.create_task(initialise())
'''
client.run(config["DISCORD_TOKEN"] if "DISCORD_TOKEN" in config else os.environ['DISCORD_TOKEN'])

# asyncio.run(client.db.close())

