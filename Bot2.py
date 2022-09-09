from dis import disco
from pydoc import describe
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
from io import BytesIO


config = dotenv_values(".env")


client = commands.Bot(command_prefix="g!")

#custom help command
client.remove_command("help")

@client.group(inwoke_without_command = True)
async def help(ctx):
    em = discord.Embed(title = "help" , description = "use  g!help <command> for extended information on a command." , color = ctx.author.color)
    em.add_field(name = "Fun" , value = "say , ping , upcase , choose , mogus , squads , duos")
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
@help.command()
async def mogus(ctx):
    em = discord.Embed(title = "mogus", description = "Sends a mogus", color = ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def squads(ctx):
    em = discord.Embed(title = "squads", description = " Generates 2 random teams of 4 players", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "g!squads <player 1>,<player 2>,<player 3>.....<player 8>")
    await ctx.send(embed = em)
@help.command()
async def duos(ctx):
    em = discord.Embed(title = "duos", description = "Generates random teams of 2 players", color = ctx.author.color)
    em.add_field(name = "**Syntax**", value = "g!duos <player 1>,<player 2>,<player 3>......<player n>      NOTE : Number of players should be even",)
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


#total members in the server
@client.command()
async def members(ctx):
    await ctx.send("There are currently " + str(ctx.guild.member_count) + " members in this server.")


@client.command()
async def choose(ctx , *choices : str):
    await ctx.send(random.choice(choices))

myfile = discord.File('mogus.txt')     #set file 
@client.command()
async def mogus(ctx):
    await ctx.send(file = myfile)


@client.command()
async def squads(ctx, arg : str):
    b = arg.split(",")
    c = []

    if (len(b) > 8 or len(b) < 8):
        await ctx.send("Invalid number of arguments were given, please give exactly 8 arguments")
    
    else:

        for i in range(4):
            z = random.choice(b)
            b.remove(z)
            c.append(z)
    
        embed = discord.Embed(title = "Random generated teams",color = ctx.author.color)
        embed.set_author(name = ctx.author.display_name, icon_url= ctx.author.avatar_url)     #display user's name and user pfp
        embed.set_thumbnail(url= "https://thumbs.dreamstime.com/b/vs-versus-logo-design-template-duel-icon-vector-illustration-versus-logo-design-template-duel-icon-vs-symbol-vector-182360815.jpg")
        embed.add_field(name= "Team A:", value = str(c), inline= False)         #inline = False won't allow the second field to be next to the first field
        embed.add_field(name = "Team B:",value = str(b), inline= False)
        await ctx.send(embed = embed)


@client.command()
async def duos(ctx,arg : str):
    b = arg.split(",")
    t = len(b)
    if (t%2 != 0):
        await ctx.send("Odd or invalid number of arguments were given, please give even number of arguments")
    else:
        n = int(len(b)/2)
        c = []
        
        for i in range(n):
            s = str(i+1)
            c.append([])
            for j in range(2):
                x = random.choice(b)
                b.remove(x)
                c[i].append(x)
            embed = discord.Embed(color = ctx.author.color)
            embed.add_field(name = "Team "+ s +" :", value = c[i], inline= False)
            embed.set_thumbnail(url="https://pngtree.com/freepng/vs-or-versus-logo-design-template-duel-icon_6009619.html")
            await ctx.send(embed = embed)




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

