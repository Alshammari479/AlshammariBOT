import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# إعداد البوت
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

# تحميل الأوامر (Cogs)
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'✅ تم تحميل: {filename}')

@bot.event
async def on_ready():
    print(f'✅ البوت متصل بـ {bot.user}')
    print(f'📊 عدد السيرفرات: {len(bot.guilds)}')
    await bot.change_presence(activity=discord.Game(name="/help"))

@bot.event
async def on_guild_join(guild):
    print(f'🎉 انضم البوت إلى سيرفر: {guild.name}')

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())
