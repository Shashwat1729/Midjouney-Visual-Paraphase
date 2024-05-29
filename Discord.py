import discord
import os
import asyncio
from discord.ext import commands

# Replace with your bot token
TOKEN = "MTI0NDI2NTU5MDc1MjAyMjU4Mg.GY1LHf.ADdZsShJmY1muJREm0FPI6v-GgFgrtxakU3gns"
# Replace with your channel ID
CHANNEL_ID = 1238313627266711573

# Initial address for the image folder
IMAGE_FOLDER = r"C:\Users\shash\Downloads\Automation\Midjourney"

# Define the intents
intents = discord.Intents.default()
intents.message_content = True

# Bot command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('------')

@bot.command()
async def upload_image(ctx, *,image_name):
    file_path = os.path.join(IMAGE_FOLDER, image_name)
    if not os.path.isfile(file_path):
        await ctx.send(f'File {image_name} not found.')
        return

    if not image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        await ctx.send(f'File {image_name} is not a valid image format.')
        return

    try:
        await ctx.send(file=discord.File(file_path))
        print(f'Uploaded {image_name}')
    except Exception as e:
        print(f'Error uploading image: {e}')

# Run the bot within an event loop
async def run_bot():
    try:
        await bot.start(TOKEN)
    except Exception as e:
        print(f'Error starting bot: {e}')

# Create an event loop and run the bot
loop = asyncio.get_event_loop()
loop.create_task(run_bot())
loop.run_forever()
