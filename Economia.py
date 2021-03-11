from typing import Deque
import discord
import random
import asyncio
from discord.ext import commands
from COGS import database

class Economia(commands.Cog):
    def __init__(self, bot:discord.Client):
        self.bot = bot

    def coinflip(self):
        return random.randint(0,1)

    def rolldice(self, maxAmount):
        return random.randint(0, maxAmount)
    @commands.command()
    async def balance(self, ctx, member:discord.Member = None):
        if member is None:
            member = ctx.author
        if member.bot:
            await ctx.send(f"Los bots no tienen cartera...", delete_after=3)
            return
        balance = database.getBalance(member.id)
        await ctx.send(f"{member.mention} has:\n`{balance} €`")

    @commands.command()
    async def pedircredito(self, ctx, cuanto:float = None):
        if not database.doesExist(ctx.author.id):
            print(f'User {ctx.author.name} does not exist in database!')
        if cuanto is None:
            await ctx.send('Cantidad no válida!', delete_after=2)
            return
        debt = database.getDeuda(ctx.author.id)
        if debt < 2000.0:
            if cuanto > 0 and cuanto < (2000 - debt):
                database.pedirCredito(ctx.author.id, cuanto)
                await ctx.send(f"Te han sido concedidos:\n`{cuanto} €`")
        else:
            await ctx.send('Tienes mas de 2000€ de deuda, paga primero!', delete_after=2)
    @commands.command()
    async def pagarcredito(self, ctx, cuanto:float = None):
        if not database.doesExist(ctx.author.id):
            print(f'User {ctx.author.name} does not exist in database!')
        if cuanto is None:
            await ctx.send("Cantidad no válida!", delete_after=2)
            return
        balance = database.getBalance(ctx.author.id)
        deuda = database.getDeuda(ctx.author.id)
        if balance < cuanto:
            await ctx.send("No tienes tanto dinero en tu cuenta!")
            return
        else:
            if deuda >= cuanto:
                database.pagarCredito(ctx.author.id, cuanto)
                await ctx.send(f"Has pagado:\n`{cuanto} €`")
            else:
                await ctx.send(f"Eso es más dinero del que debes, tu deuda es:\n`**{deuda}**`")
    @commands.command()
    async def deuda(self, ctx, member:discord.Member = None):
        if not database.doesExist(ctx.author.id):
            print(f'User {ctx.author.name} does not exist in database!')
        if member is None:
            member = ctx.author
        await ctx.send(f"{member.mention} debe:\n`{database.getDeuda(member.id)} €`")
    @commands.command()
    async def betflip(self, ctx, opcion = 'c', amount:float = None):
        if not database.doesExist(ctx.author.id):
            print(f'User {ctx.author.name} does not exist in database!')
        if amount is None:
            if self.coinflip() == 0:
                await ctx.send('Ha salido:\n`CARA`')
            else:
                await ctx.send('Ha salido:\n`CRUZ`')
        else:
            if opcion.lower() == 'c':
                eleccion = 0
            elif opcion.lower() == 'x':
                eleccion = 1
            if amount > 0:
                if amount <= database.getBalance(ctx.author.id):
                    database.quitarDinero(ctx.author.id, amount)
                    sale = self.coinflip()
                    if sale == 0:
                        await ctx.send('Ha salido:\n`CARA`')
                    else:
                        await ctx.send("Ha salido:\n`CRUZ`")
                    if eleccion == sale:
                        await ctx.send(f"**Has ganado: `{float(amount) * 2} €`**")
                        database.darDinero(ctx.author.id, amount * 2)
                    else:
                        await ctx.send("Has **PERDIDO!**")
                else:
                    await ctx.send("No tienes tanto dinero!")
    @commands.command()
    async def betroll(self, ctx, amount:float = None):
        if not database.doesExist(ctx.author.id):
            print(f'User {ctx.author.name} does not exist in database!')
        if amount is None or amount <= 0:
            await ctx.send("No has apostado nada!")
            return
        if amount <= database.getBalance(ctx.author.id):
            roll = self.rolldice(100)
            database.quitarDinero(ctx.author.id, amount)
            await ctx.send(f"Ha salido:\n`{roll}!`")
            if roll < 66:
                await ctx.send('No has ganado nada!')
            elif roll >= 66 and roll < 90:
                await ctx.send(f'**Has ganado: `{float(amount) * 2} €`**')
                database.darDinero(ctx.author.id, amount * 2)
            elif roll >=90 and roll < 100:
                await ctx.send(f"**Has ganado: `{float(amount) * 4} €`**")
                database.darDinero(ctx.author.id, amount * 4)
            elif roll == 100:
                await ctx.send(f"***damn.*\n**Has ganado: `{float(amount) * 10} €!**`")
                database.darDinero(ctx.author.id, amount * 10)
        else:
            await ctx.send("No tienes tanto dinero!", delete_after=2)
    
    def sortList(self, list):
        return float(list[1])
    @commands.command()
    async def economia(self, ctx, string:str = None):
        if string is None:
            string = "local"
        leaderboard = []
        if string.lower() == "local":
            genteLst = database.getEconomia()
            async with ctx.typing():
                for discordID, balance in genteLst:
                    try:
                        miembro = await ctx.guild.fetch_member(discordID)
                    except:
                        print(f'Error fetching member with id: {discordID}')
                        miembro = None
                    if miembro is not None:
                        leaderboard.append((f"{miembro.name}#{miembro.discriminator}", float(balance)))
                await asyncio.sleep(2)
            leaderboard.sort(key=self.sortList, reverse=True)
        elif string.lower() == "global":
            genteLst = database.getEconomia()
            async with ctx.typing():
                for discordID, balance in genteLst:
                    try:
                        miembro = await self.bot.fetch_user(discordID)
                    except:
                        print(f'Error fetching member with id: {discordID}')
                        miembro = None
                    if miembro is not None:
                        leaderboard.append((f"{miembro.name}#{miembro.discriminator}", float(balance)))
                await asyncio.sleep(2)
            leaderboard.sort(key=self.sortList, reverse=True)
        else:
            await ctx.send("Argumento no válido!", delete_after=3)
        balancetotal = 0.0
        i = 1
        st = ""
        for nombre, balance in leaderboard:
            balancetotal += balance
        for nombre, balance in leaderboard[0:10]:
            st += f"**{i}->** *{nombre} - (**{balance} €**)*\n"
            i += 1
        embed=discord.Embed(title="Dinero Total:", description=f"**{balancetotal} €**")
        embed.set_author(name=f"{string.capitalize()} Economy", icon_url="https://www.pngkey.com/png/full/358-3580487_our-ocean-economy-economy-icon-png.png")
        embed.add_field(name="Top 10 más ricos:", value=st, inline=False)
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Economia(bot))