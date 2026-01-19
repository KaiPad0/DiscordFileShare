import discord
from discord import app_commands
from dotenv import load_dotenv
load_dotenv()
import os

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default() 
client = discord.Client(intents=intents) 
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("ログインしました")

@tree.command(name="upload", description="アップロード画面を開きます")
async def upload(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    # このコマンド専用の「後日談用URL」を取得
    # interaction.followup.url がそれにあたります
    webhook_url = interaction.followup.url
    user_id = interaction.user.id

    # ユーザーには「ここからアップロードしてね」というリンクを送る
    upload_url = f"http://kaipad123.servemp3.com:5000/upload?webhook={webhook_url}&userid={user_id}"
    
    await interaction.followup.send(f"以下のリンクから動画をアップロードしてください！\n{upload_url}", ephemeral=True)



client.run(TOKEN)