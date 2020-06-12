import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json
import os

#json檔案設定
with open("setting.json",mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self,member):
            channel = self.bot.get_channel(int(jdata['大廳']))
            await channel.send(f'{member.mention} ,歡迎加入!')
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int(jdata['大廳']))
        await channel.send(f'{member.mention} 退出了伺服器! QQ')
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ["amumu","阿姆姆","秉軒","軒哥"]
        if msg.content in keyword and msg.author!=self.bot.user:
            await msg.channel.send("hi")

def setup(bot):
    bot.add_cog(Event(bot))