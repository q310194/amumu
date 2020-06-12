import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json,asyncio,datetime

#背景作業
class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(666378706775965706)
            while not self.bot.is_closed():
                now_time= datetime.datetime.now().strftime('%H%M')
                with open("setting.json",mode='r',encoding="utf8") as jfile:
                    jdata=json.load(jfile)
                if now_time==jdata['time']:
                    await self.channel.send('嘟嘟--12點了,早點睡ㄅ')
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set channel:{self.channel.mention}')
    
    @commands.command()
    async def set_time(self,ctx,time):
        with open("setting.json",mode='r',encoding="utf8") as jfile:
            jdata=json.load(jfile)
        jdata['time'] = time
        with open("setting.json",mode='w',encoding="utf8") as jfile:
            json.dump(jdata,jfile,indent=4)

                





def setup(bot):
    bot.add_cog(Task(bot))