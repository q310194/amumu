import discord
from discord.ext import commands
import json
import random
import os

#json檔案設定
with open("setting.json",mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)
#bot關鍵字
bot = commands.Bot(command_prefix='$')

#bot事件(發生即觸發)
@bot.event
async def on_ready ():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(int(jdata['大廳']))
    await channel.send(f'{member.mention} ,歡迎加入!')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(jdata['大廳']))
    await channel.send(f'{member.mention} 退出了伺服器! QQ')

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-Loaded {extension} done.')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-Loaded {extension} done.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')


if __name__ == "__main__":
    bot.run(jdata['TOKEN'])

