import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    def __init__(self,bot):
        self.bot=bot
    
    #bot命令(需要觸發)
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('目前Bot的延遲是:'f'{round(self.bot.latency*1000)}(ms)')
    @commands.command()
    async def hi(self,ctx):
        await ctx.send("test")

def setup(bot):
    bot.add_cog(Main(bot))