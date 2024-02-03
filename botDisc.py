import os
import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
intents.members = True # se necessário
intents.presences = True # se necessário

# Configuração do bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Executa texto no cmd
@bot.command()
async def run(ctx, text:str):
    cmd = [f'{text}']
    process = await asyncio.create_subprocess_exec(*cmd)
    await process.communicate()

# Executa o bot
load_dotenv()
bot.run(os.getenv('ID_BOT'))
