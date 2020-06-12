import discord,datetime
from discord.ext import commands
from core.classes import Cog_Extension
import json,datetime

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

    @commands.command()
    async def about(self,ctx):
        embed=discord.Embed(title="Amumu Bot 功能", description="測試階段,歡迎debug", color=0x218b04)
        embed.set_thumbnail(url="https://p2.bahamut.com.tw/HOME/creationCover/15/0002744315_B.JPG")
        embed.add_field(name="$win", value="LOL本週五路T1角", inline=False)
        embed.add_field(name="$clean 數字", value="清除[數字]條訊息", inline=False)
        embed.add_field(name="$lol", value="抽取一個英雄(已更新全英雄)", inline=False)
        embed.add_field(name="$sex", value="傳送一張sex圖(圖包募集中)", inline=False)
        embed.add_field(name="$ping", value="目前機器人延遲(重要嗎?)", inline=False)
        embed.set_footer(text="by IKEA")
        await ctx.send(embed=embed)
    
    @commands.command()#bot復誦訊息
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.command()#清理訊息
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit=num+1)
    
    
    
    
        

def setup(bot):
    bot.add_cog(Main(bot))