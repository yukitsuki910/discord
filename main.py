
import discord
from discord.ext import commands

import os


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")

# name指令顯示名稱，description指令顯示敘述
# name的名稱，中、英文皆可，但不能使用大寫英文
@bot.tree.command(name = "hello", description = "Hello, world!")
async def hello(interaction: discord.Interaction):
    # 回覆使用者的訊息
    await interaction.response.send_message("Hello, world!")

import random


@bot.tree.command(name = "飲料", description = "今天喝甚麼？")
async def 飲料(interaction: discord.Interaction):
    divinations= [ "萬波","迷客夏","五十嵐"
,"可不可","河堤上的貓",
"甲文青","三分春色",
"酸奶多","CoCo","鶴茶樓","五桐號"
    ]
    result = random.choice(divinations)
    await interaction.response.send_message(f"今天我想來點：{result}")

@bot.tree.command(name = "晚餐", description = "還在煩惱吃甚麼嗎？")
async def 晚餐(interaction: discord.Interaction):
    divinations = [ "青虎食堂","開心丼飯","胖焗","偷斯","蛋包先生","湯食主義","吉野家","八方雲集","四海遊龍","自助餐","黑乾麵","南台灣","日式炒麵","ok泡麵"
    ]
    result = random.choice(divinations)
    await interaction.response.send_message(f"今天的晚餐就吃：{result}")

@bot.tree.command(name = "抽籤", description = "來看看今天的運氣吧~")
async def 抽籤(interaction: discord.Interaction):
    divinations = [ "大吉", "中吉",  "小吉",
        "吉",
       "末吉",
        "凶",
        "大凶"
    ]
    result = random.choice(divinations)
    await interaction.response.send_message(f"你抽到的籤是：{result}")



bot.run(os.getenv("TOKEN"))
