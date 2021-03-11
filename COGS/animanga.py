from discord.ext import commands
from discord.ext.commands.errors import ChannelNotReadable
import mal
import discord
import asyncio
from NHentai import NHentai as nhen
from . import constantes
reactions = ('0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣')

class AniManga(commands.Cog, name='Anime y Manga'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def asearch(self, ctx, *, string):
        if ctx.author.bot:
            return
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reactions
        async with ctx.typing():
            results = mal.AnimeSearch(string).results
            await asyncio.sleep(3)
        if len(results) > 0:
            st = ""
            i = 0
            for res in results[0:10]:
                st += f" {i} -> {res.title} ({res.mal_id})\n"
                i+=1
            message = await ctx.send(f'Se han encontrado los siguientes titulos (id):\n```{st}```')
            for a in range(0, i):
                await message.add_reaction(reactions[a])
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                await message.delete()
                index = reactions.index(str(reaction))
                async with ctx.typing():
                    anime = mal.Anime(results[index].mal_id)
                    await asyncio.sleep(3)
                genres = "|"
                for a in anime.genres:
                    genres += f" {a} |"

                embed=discord.Embed(title=f"{anime.title_english}", url=f"{anime.url}", description=f"Score: {anime.score}", color=0x1ffb13)
                embed.set_thumbnail(url=f"{anime.image_url}")
                embed.add_field(name="Generos", value=f"{genres}", inline=False)
                embed.add_field(name="Duracion", value=f"{anime.episodes} episodios de {anime.duration}", inline=False)
                embed.add_field(name="Synopsis", value=f"{anime.synopsis[0:1020]}...", inline=False)
                await ctx.send(embed=embed)
            except asyncio.TimeoutError:
                await message.delete()
                await ctx.send("Se ha agotado el tiempo de respuesta!")

        elif len(results) == 1:
            anime = mal.Anime(results[0].mal_id)
            genres = ""
            for a in anime.genres:
                genres += f" {a} |"
            embed=discord.Embed(title=f"{anime.title_english}", url=f"{anime.url}", description=f"Score: {anime.score}", color=0x1ffb13)
            embed.set_thumbnail(url=f"{anime.image_url}")
            embed.add_field(name="Generos", value=f"{genres}", inline=False)
            embed.add_field(name="Duracion", value=f"{anime.episodes} episodios de {anime.duration}", inline=False)
            embed.add_field(name="Synopsis", value=f"{anime.synopsis[0:1020]}...", inline=False)
            await ctx.send(embed=embed)
            
        else:
            await ctx.send('Sin resultados!')

    @commands.command()
    async def msearch(self, ctx, *, string):
        if ctx.author.bot:
            return
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in reactions
        async with ctx.typing():
            results = mal.MangaSearch(string).results
            await asyncio.sleep(3)
        if len(results) > 0:
                st = ""
                i = 0
                for res in results[0:10]:
                    st += f" {i} -> {res.title} ({res.mal_id})\n"
                    i+=1
                message = await ctx.send(f'Se han encontrado los siguientes titulos (id):\n```{st}```')
                for a in range(0, i):
                    await message.add_reaction(reactions[a])
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                    await message.delete()
                    index = reactions.index(str(reaction))
                    async with ctx.typing():
                        manga = mal.Manga(results[index].mal_id)
                        await asyncio.sleep(3)
                    genres = "|"
                    for a in manga.genres:
                        genres += f" {a} |"

                    title = manga.title_english
                    if title is None:
                        title = manga.title
                    embed=discord.Embed(title=f"{title}", url=f"{manga.url}", description=f"Score: {manga.score}", color=0x1ffb13)
                    embed.set_thumbnail(url=f"{manga.image_url}")
                    embed.add_field(name="Generos", value=f"{genres}", inline=False)
                    embed.add_field(name="Duracion", value=f"{manga.volumes} volumenes y {manga.chapters} capitulos", inline=False)
                    embed.add_field(name="Synopsis", value=f"{manga.synopsis[0:1020]}...", inline=False)
                    await ctx.send(embed=embed)
                except asyncio.TimeoutError:
                    await message.delete()
                    await ctx.send("Se ha agotado el tiempo de respuesta!")
        elif len(results) == 1:
            manga = mal.Manga(results[0].mal_id)
            genres = ""
            for a in manga.genres:
                genres += f" {a} |"
            
            title = manga.title_english
            if title is None:
                title = manga.title
            embed=discord.Embed(title=f"{title}", url=f"{manga.url}", description=f"Score: {manga.score}", color=0x1ffb13)
            embed.set_thumbnail(url=f"{manga.image_url}")
            embed.add_field(name="Generos", value=f"{genres}", inline=False)
            embed.add_field(name="Duracion", value=f"{manga.volumes} volumenes y {manga.chapters} capitulos", inline=False)
            embed.add_field(name="Synopsis", value=f"{manga.synopsis[0:1020]}...", inline=False)
            await ctx.send(embed=embed)
            
        else:
            await ctx.send('Sin resultados!')

    @commands.command()
    async def hsearch(self, ctx, *, numero:int = None):
        if numero is None:
            await ctx.send("Número no válido!")
            return
        nhentai = nhen()
        async with ctx.typing():
            doujin = nhentai._get_doujin(id=numero)
            await asyncio.sleep(3)
        if doujin:
            ##
            tagsPeligrosos=constantes.TAGS_PELIGROSOS
            ##
            tags = "|"
            if(set(tagsPeligrosos) & set(doujin.tags)):
                peligro = (set(tagsPeligrosos) & set(doujin.tags))
                for a in peligro:
                    tags += f" {a} |"
            else:
                tags = "| nada |"
            tags2 = "|"
            for a in doujin.tags:
                tags2+=f" {a} |"
            characters = "|"
            for a in doujin.characters:
                characters+=f" {a} |"
            lang = "|"
            for a in doujin.languages:
                lang+=f" {a} |"
            embed=discord.Embed(title=f"{doujin.title}", url=f"https://www.nhentai.net/g/{numero}", description=f"Paginas Totales: {doujin.total_pages}", color=0x1ffb13)
            embed.add_field(name="**!TAGS PELIGROSOS!**", value=f"{tags}", inline=False)
            embed.add_field(name="TAGS", value=f"{tags2}", inline=False)
            embed.add_field(name="PERSONAJES", value=f"{characters}", inline=False)
            embed.add_field(name="IDIOMA", value=f"{lang}", inline=False)
            await ctx.send(embed=embed)

    @commands.command()
    async def rhen(self, ctx, *, nada=None):
        nhentai = nhen()
        async with ctx.typing():
            doujin = nhentai.get_random()
            await asyncio.sleep(3)
        if doujin:
            tagsPeligrosos=constantes.TAGS_PELIGROSOS
            ##
            tags = "|"
            if(set(tagsPeligrosos) & set(doujin.tags)):
                peligro = (set(tagsPeligrosos) & set(doujin.tags))
                for a in peligro:
                    tags += f" {a} |"
            else:
                tags = "| nada |"
            tags2 = "|"
            for a in doujin.tags:
                tags2+=f" {a} |"
            characters = "|"
            for a in doujin.characters:
                characters+=f" {a} |"
            lang = "|"
            for a in doujin.languages:
                lang+=f" {a} |"
            embed=discord.Embed(title=f"{doujin.title}", url=f"https://www.nhentai.net/g/{doujin.id}", description=f"Paginas Totales: {doujin.total_pages}", color=0x1ffb13)
            embed.add_field(name="**!TAGS PELIGROSOS!**", value=f"{tags}", inline=False)
            embed.add_field(name="TAGS", value=f"{tags2}", inline=False)
            embed.add_field(name="Personajes", value=f"{characters}", inline=False)
            embed.add_field(name="Idioma", value=f"{lang}", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Error sacando un d random!")
def setup(bot):
    bot.add_cog(AniManga(bot))