import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from link import plstry
from queue import Queue 
//dw the api key from the initial commit is not aviable anymore don't bother
TOKEN = ''
client= commands.Bot(command_prefix="&")
def youtube(url: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'opus',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("[*]DOWNLOADING")
        ydl.download([url])
        print("[*]FiNISHED")
        
    for file in os.listdir("./"):
        if file.endswith(".opus"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.opus")
def play(ctx):
   try:
     voice = get(client.voice_clients, guild=ctx.guild)
     voice.play(discord.FFmpegPCMAudio("song.opus"))
     voice.source = discord.PCMVolumeTransformer(voice.source)
     voice.source.volume = 0.1
   except discord.ClientException:
        ctx.send("Rabdare!")
        return
@client.command(pass_context=True)
async def stai(ctx):
     voice = get(client.voice_clients, guild=ctx.guild)
     voice.pause()
@client.command(pass_context=True)
async def inapoi(ctx):
     voice = get(client.voice_clients, guild=ctx.guild)
     voice.resume()
@client.command(pass_context=True)
async def hai(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
@client.command(pass_context=True)
async def mars(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
@client.command(pass_context=True)
async def baga(ctx, url: str):
    urlreal="https://www.youtube.com/"+str(plstry(url))
    print(urlreal)
    voice = get(client.voice_clients, guild=ctx.guild)
    song_there = os.path.isfile("song.opus")
    if song_there:
        os.remove("song.opus")
    youtube(urlreal)
    play(ctx)
client.run(TOKEN)
