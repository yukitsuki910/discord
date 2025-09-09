
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
,"可不可","teatop","清心","芳逸","mr wish","CoCo","鶴茶樓","五桐號"
    ]
    result = random.choice(divinations)
    await interaction.response.send_message(f"今天我想來點：{result}")

@bot.tree.command(name = "晚餐", description = "還在煩惱吃甚麼嗎？")
async def 晚餐(interaction: discord.Interaction):
    divinations = [ "拉麵","八方","韓式料理"," 丼飯","八方","麥當勞","炒麵","泡麵"
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


# --- 假 web server，讓 Render 偵測用 ---
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_server():
    port = int(os.environ.get("PORT", 3000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"Listening on port {port}")
    server.serve_forever()

# 開一個執行緒跑 web server，不會卡住 bot
threading.Thread(target=run_server).start()


bot.run(os.getenv("TOKEN"))
