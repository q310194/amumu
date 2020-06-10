import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready ():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(537672020729790510)
    await channel.send(f'{member.mention} 歡迎加入!')
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(537672020729790510)
    await channel.send(f'{member.mention} 退出了伺服器! QQ')

bot.run("NzE5NzcxMDcyODE1MzAwNjEy.XuD3aA.7Lw4b7tF_4bOQ2MW8mXTXpoRjBU")

