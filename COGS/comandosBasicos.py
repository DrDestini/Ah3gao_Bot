import discord
from discord.ext import commands
import datetime as DT
import random

from COGS import database
OWNERID = 223949937010802688
from discord.ext.commands.core import command
class comandosBasicos(commands.Cog, name='Comandos Basicos'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! -> **{int(self.bot.latency * 1000)} ms**')
    
    @commands.command()
    async def choose(self, ctx, *, string):
        if string:
            options = string.split(',')
            chosen = random.choice(options)
            await ctx.send(f'I choose: {chosen}')
    @commands.command()
    async def guildstats(self, ctx):
        embed=discord.Embed(title=' ', description=ctx.guild.name, color=0xff0006)
        embed.set_author(name="GUILD STATS")
        embed.add_field(name=f"Dueño: *@{ctx.guild.owner.display_name}*", value='\u200b', inline=False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        numbots = 0
        for member in ctx.guild.members:
            if member.bot:
                numbots+=1

        embed.add_field(name=f"Miembros: {ctx.guild.member_count}", value=f"Humanos: {ctx.guild.member_count - numbots} | Bots: {numbots}", inline=False)
        embed.add_field(name=f"Creado: {ctx.guild.created_at.strftime('%m/%d/%Y a las %H:%M:%S')}", value='\u200b', inline=True)
        embed.add_field(name=f"Limite Archivos: {ctx.guild.filesize_limit / 1024 / 1024} MB", value='\u200b', inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def userstats(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        lst = database.getUwUOwO(member.id)
        if lst:
            (uwu, owo) = lst[0]
        else:
            (uwu, owo) = (0,0)
        embed=discord.Embed(title=' ', description=member.display_name, color=0xff0006)
        embed.set_author(name=f"{member.name}'s USER STATS")
        embed.add_field(name=f"Entró en el server:", value=f"*{member.joined_at.strftime('%m/%d/%Y a las %H:%M:%S')}*", inline=False)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name=f"Usuario creado:", value=f"{member.created_at.strftime('%m/%d/%Y a las %H:%M:%S')}", inline=False)
        embed.add_field(name=f"Ha dicho UwU:", value=f'{uwu} veces', inline=True)
        embed.add_field(name=f"Ha dicho OwO:", value=f'{owo} veces', inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def suggest(self, ctx, *, suggest:str = None):
        if suggest is None:
            await ctx.send("Agrega un mensaje a la sugerencia.")
            return
        try:
            file = open("./suggestions.txt", 'a')
            file.write(f"{ctx.author.name}#{ctx.author.discriminator} suggested: {suggest}\n")
            file.close()
            owner = await self.bot.fetch_user(OWNERID)
            await owner.send(f"**{ctx.author.name}#{ctx.author.discriminator}** suggested: {suggest}\nExecuted in guild: **{ctx.guild.name}** and channel: **#{ctx.channel.name}**")
            await ctx.send("Sugerencia anotada!", delete_after=3)
        except Exception as e:
            print(f"Exception: {e}")
            await ctx.send("Error recibiendo la sugerencia!", delete_after=3)
def setup(bot):
    bot.add_cog(comandosBasicos(bot))

