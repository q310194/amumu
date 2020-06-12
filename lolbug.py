import requests
from pyquery import PyQuery as pq
import csv,re

def get_message(five_mes):
    for items in five_mes:
        name=items.find("div.champion-index-table__name").text()
        #获取英雄名称

        win_chance=items.find("td.champion-index-table__cell--value").text()[:6]
        #获取胜率
        choice=items.find("td.champion-index-table__cell--value").text()[6:]
        #获取登场率

        img=items.find("td.champion-index-table__cell--value img").attr("src")
        fisrt_chance="T"+re.match(".*r-(.*?)\.png",img).group(1)
        #获取src属性并提取出优先级
        yield{
        "name":name,
        "win_chance":win_chance,
        "choice":choice,
        "fisrt_chance":fisrt_chance
        }


def write_csv(data,names):
	#参数names为文件名
    with open(names+".csv", "a", encoding="utf-8-sig", newline='') as file:
        fieldnames = ["name", "win_chance",
                          "choice", "fisrt_chance"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)


headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400",
            "Accept-Language":"zh-CN,zh;q=0.9"
                        }
html=requests.get("http://www.op.gg/champion/statistics",headers=headers).text

doc=pq(html)

for position in doc("tbody").items(): 
	#这里遍历五个tbody节点，分别代表五个位置
	
    names=re.match("tabItem champion-trend-tier-(.*)",position.attr("class")).group(1)
    #这里用正则表达式提取出tbody的calss属性的top，mid，adc等作为文件名
    
    for items in get_message(position.find("tr").items()):
    	#这里遍历每一个tbody节点的tr节点并利用get_message函数
        
        write_csv(items,names)
        if items.get("fisrt_chance")=="T1":
        	#输出T1英雄
            data=open("C:\\Users\\Administrator\\Desktop\\amumu\\loldata.txt",'a')
            print("當前版本T1  "+names+"有"+items.get("name")+"勝率為"+items.get("win_chance"),file=data)
            data.close()