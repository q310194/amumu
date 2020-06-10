import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

#json檔案設定
with open("setting.json",mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):
    @commands.command()
    async def 私密照(self,ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)

    @commands.command()
    async def 鬆餅(self,ctx):
        random_pic_2 = random.choice(jdata["pic_2"])
        pic_2 = discord.File(random_pic_2)
        await ctx.send(file=pic_2)

def setup(bot):
    bot.add_cog(React(bot))