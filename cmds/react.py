import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random,json,os
from opencc import OpenCC
import requests
import bs4
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import csv,re,os

#json檔案設定
with open("setting.json",mode='r',encoding="utf8") as jfile:
    jdata=json.load(jfile)





class React(Cog_Extension):
    
    
    cc = OpenCC('s2tw')
    @commands.command()
    async def 私密照(self,ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file=pic)
    @commands.command()
    async def win(self,ctx):
        
        f=open("C:\\Users\\Administrator\\Desktop\\amumu\\loldata.txt")
        
        text = []
        for line in f:
            text.append(line)
        for i in range(25):
            await ctx.send(text[i])
        
   
        
       
    
    @commands.command()
    async def sex(self,ctx):
        random_pic_3 = random.choice(jdata["pic_3"])
        pic_3 = discord.File(random_pic_3)
        await ctx.send(file=pic_3)
    
    @commands.command()
    async def lol(self,ctx):
        cc = OpenCC('s2tw')
                
        random_lol = "D:\\lel\\"+random.choice(os.listdir("D:\\lel"))
        pic_lol = discord.File(random_lol)
        await ctx.send(file=pic_lol)
        await ctx.send(cc.convert(random_lol.lstrip("D:\lel").rstrip(".jpg")))
    
    

def setup(bot):
    bot.add_cog(React(bot))