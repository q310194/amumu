import discord
from discord.ext import commands
import json
import random
import os
from os import walk
import requests
from pyquery import PyQuery as pq
import csv,re



#json檔案設定
with open("setting.json",mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)
#bot關鍵字


bot = commands.Bot(command_prefix='$')

#bot事件(發生即觸發)
@bot.event
async def on_ready ():
    activity = discord.Game(name="$about", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(">> Bot is online <<")




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

