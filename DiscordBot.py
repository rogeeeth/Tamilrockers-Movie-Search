import discord
from discord import voice_client
from discord.ext import commands
from discord.ext.commands.core import command
from discord.player import FFmpegAudio
import youtube_dl 
from discord import player

class music(commands.Cog):
    def __init__(self,client):
         self.client=client
    
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("Join VC!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:   
            await ctx,voice_client.move_to(voice_channel)


    
    @commands.command()
    async def disconnect(self,ctx):
           await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self,ctx,url):
        FFMPEG_options = {'before options': "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max_5","options" : '-vn'}
        YDL_options = {'format':'bestaudio'}
        vc = ctx,voice_client

        with youtube_dl.YoutubeDL(YDL_options) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'] [0] ['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_options)
                vc.play(source)

    @commands.command()
    async def pause(self,ctx):
         await ctx,voice_client.pause()
         await ctx.send("Paused⏸️")
    
    @commands.command()
    async def resume(self,ctx):
         await ctx,voice_client.resume()
         await ctx.send("Resume⏯️")

    


def setup(client):
     client.add_cog(music(client))



