import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()
import os

TOKEN = os.getenv('TOKEN')
FLASK_SERVER_URL = "http://kaipad123.servemp3.com:5000/upload" # ラズパイのURL
intents = discord.Intents.default() 
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client)

@tree.command(name="upload", description="アップロード画面を開きます")
async def upload(interaction: discord.Interaction):
    # このコマンド専用の「後日談用URL」を取得
    # interaction.followup.url がそれにあたります
    webhook_url = interaction.followup.url
    
    # ユーザーには「ここからアップロードしてね」というリンクを送る
    upload_url = f"http://あなたのサーバーIP:5000/upload?webhook={webhook_url}"
    
    await interaction.response.send_message(f"以下のリンクから動画をアップロードしてください！\n{upload_url}", ephemeral=True)



client.run(TOKEN)