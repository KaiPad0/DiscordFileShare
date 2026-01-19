import discord
from discord import app_commands

TOKEN = "YOUR_BOT_TOKEN"
FLASK_SERVER_URL = "http://kaipad123.servemp3.com:5000/upload" # ラズパイのURL

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

bot = MyBot()

@bot.tree.command(name="upload", description="動画アップロード用のリンクを発行します")
async def upload(interaction: discord.Interaction):
    # チャンネルのWebhookを取得または作成
    webhooks = await interaction.channel.webhooks()
    webhook = discord.utils.get(webhooks, name="VideoUploader")
    if not webhook:
        webhook = await interaction.channel.create_webhook(name="VideoUploader")
    
    # Webhook URLをパラメータに仕込んだリンクを作成
    upload_url = f"{FLASK_SERVER_URL}?webhook={webhook.url}"
    
    await interaction.response.send_message(
        f"以下のリンクから動画をアップロードしてください！\n完了するとこのチャンネルに投稿されます。\n{upload_url}",
        ephemeral=True # 本人にだけ見えるメッセージにする場合
    )

bot.run(TOKEN)