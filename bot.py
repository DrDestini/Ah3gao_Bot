import logging
import discord
from discord import member
from discord.ext import commands
from discord.flags import Intents
from COGS import database

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
token = open('token.txt','r').read()
bot = commands.Bot(command_prefix='.', intents=intents)
game = discord.Game("with the API")
bot.remove_command('help')
@bot.event
async def on_guild_join(guild):
    print(f'Joined a new guild: {guild.name}\nFetching members!')
    guild.fetch_members()
    for member in guild.members:
        if not member.bot:
            database.doesExist(member.id)
    print(f"Done fetching and importing members for: {guild.name}")

@bot.event
async def on_member_join(member):
    print(f'NEW MEMBER in: {member.guild.name}\nName: {member.name} --> Importing to database!')
    if not member.bot:
            database.doesExist(member.id)
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=game)
    bot.load_extension('COGS.comandosBasicos')
    bot.load_extension('COGS.Economia')
    bot.load_extension('COGS.animanga')
    bot.load_extension('COGS.comandoHelp')
    bot.load_extension('COGS.comandosPesca')
    print('fetching and registering all guild members...')
    guild:discord.Guild
    for guild in bot.guilds:
        guild.fetch_members()
        for member in guild.members:
            if not member.bot:
                database.doesExist(member.id)
    print('-----------------------Done!------------------------')
    print('logged as {0.user}\nThis bot is currently in {1} guilds'.format(bot, len(bot.guilds)))
@bot.event
async def on_message(message):
    if message.author.bot:
            return
    if 'uwu' in message.content.lower():
        database.saidUwU(message.author.id)
    if 'owo' in message.content.lower():
        database.saidOwO(message.author.id)    
    await bot.process_commands(message)

bot.run(token)