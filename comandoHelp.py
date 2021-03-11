from discord.ext import commands
import discord
class comandoHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True, aliases=['h', 'Help', 'HELP'])
    async def help(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="Comandos")
        embed.add_field(name="__**Basicos**__", value="**.suggest** -> Sugerir algo relacionado con el bot\n**.ping** -> ¿Responde el bot?\n**.choose** -> Elegir entre varias opciones\n**.guildstats** -> Ver las estadisticas del servidor\n**.userstats** -> Ver las estadisticas de un miembro", inline=False)
        embed.add_field(name="__**Economía**__", value="**.balance** -> Ver el dinero de un miembro\n**.deuda** -> Ver la deuda de un miembro\n**.economia** -> Ver el ranking local/global\n**.betflip** -> Apostar en cara/cruz\n**.betroll** -> Apostar en un dado\n**.pedircredito** -> Pedir dinero al banco\n**.pagarcredito** -> Pagar deudas", inline=False)
        embed.add_field(name="__**Anime y Manga**__", value="**.asearch** -> Buscar un anime por nombre en MAL\n**.msearch** -> Buscar un manga por nombre en MAL\n**.hsearch** -> Buscar números en nhentai\n**.rhen** -> Sacar un *H* aleatorio", inline=False)
        embed.add_field(name="__**Pesca**__", value="**.pesca** -> Tira la caña en uno de los lagos. (Usa help .pesca para más información)\n**\t->.pesca inventario** -> Muestra tu inventario de pesca.\n**\t->.pesca stats** -> Muestra tu nivel actual y la XP necesaria para subir de nivel.\n**\t->.pesca vender** -> Vende todos los peces que tienes por dinero.", inline=False)
        embed.set_footer(text="Escribe .help <comando> para más ayuda")
        await ctx.send(embed=embed)

    @help.group()
    async def suggest(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .SUGGEST")
        embed.add_field(name="__**Descripción**__", value="Usa este comando si tienes alguna sugerencia para el desarrollo del bot.",inline=False)
        embed.add_field(name="__**Uso**__", value=".suggest <sugerencia>",inline=False)

        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)

    @help.group()
    async def ping(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .PING")
        embed.add_field(name="__**Descripción**__", value="Usa este comando para comprobar que el bot sigue vivo.",inline=False)
        embed.add_field(name="__**Uso**__", value=".ping",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)

    @help.group()
    async def choose(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .CHOOSE")
        embed.add_field(name="__**Descripción**__", value="Este comando te ayuda a elegir entre varias opciones.", inline=False)
        embed.add_field(name="__**Uso**__", value=".choose <opcion 1>,[opcion 2],[opcion 3]...",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)

    @help.group()
    async def guildstats(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .GUILDSTATS")
        embed.add_field(name="__**Descripción**__", value="Usa este comando para ver las estadísticas del servidor.", inline=False)
        embed.add_field(name="__**Uso**__", value=".guildstats",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)

    @help.group()
    async def userstats(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .USERSTATS")
        embed.add_field(name="__**Descripción**__", value="Usa este comando para ver las estadísticas de un miembro, las veces que ha dicho *uwu* o *owo*.", inline=False)
        embed.add_field(name="__**Uso**__", value=".userstats [*@miembro*]",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def balance(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .BALANCE")
        embed.add_field(name="__**Descripción**__", value="Te permite ver la cantidad de dinero que posee un miembro o tu mismo.", inline=False)
        embed.add_field(name="__**Uso**__", value=".balance [*@miembro*]",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def deuda(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .DEUDA")
        embed.add_field(name="__**Descripción**__", value="Te permite ver la cantidad de dinero que debe un miembro o tu mismo.", inline=False)
        embed.add_field(name="__**Uso**__", value=".deuda [*@miembro*]",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def economia(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .ECONOMIA")
        embed.add_field(name="__**Descripción**__", value="Te permite ver el ranking de los 10 más ricos a nivel de servidor o a nivel global.", inline=False)
        embed.add_field(name="__**Uso**__", value=".economia [local/global]",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def betflip(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .BETFLIP")
        embed.add_field(name="__**Descripción**__", value="Apuesta dinero en una tirada de moneda, si aciertas ganas tu apuesta x2", inline=False)
        embed.add_field(name="__**Uso**__", value=".betflip <c/x> <cantidad>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def betroll(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .BETROLL")
        embed.add_field(name="__**Descripción**__", value="Apuesta en una tirada de dado de 0 a 100, las recompensas son las siguientes: \n0-66 -> nada | 66-90 -> x2 | 90-99 -> x4 | 100 -> **x10**.", inline=False)
        embed.add_field(name="__**Uso**__", value=".betroll <cantidad>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def pedircredito(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .PEDIRCREDITO")
        embed.add_field(name="__**Descripción**__", value="Pide dinero al banco, hasta un máximo de 1000€ a la vez. No puedes tener más de 2000€ de deuda.", inline=False)
        embed.add_field(name="__**Uso**__", value=".pedircredito <cantidad>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def pagarcredito(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .PAGARCREDITO")
        embed.add_field(name="__**Descripción**__", value="Paga tu deuda, no puedes recibir credito si tienes más de 2000€ de deuda.", inline=False)
        embed.add_field(name="__**Uso**__", value=".pagarcredito <cantidad>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def asearch(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .ASEARCH")
        embed.add_field(name="__**Descripción**__", value="Busca un anime en la base de datos de MyAnimeList", inline=False)
        embed.add_field(name="__**Uso**__", value=".asearch <nombre>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def msearch(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .MSEARCH")
        embed.add_field(name="__**Descripción**__", value="Busca un manga en la base de datos de MyAnimeList.", inline=False)
        embed.add_field(name="__**Uso**__", value=".msearch <cantidad>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def hsearch(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .HSEARCH")
        embed.add_field(name="__**Descripción**__", value="Busca un conjunto de digitos mágicos en ||NHENTAI.NET||", inline=False)
        embed.add_field(name="__**Uso**__", value=".hsearch <número>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def rhen(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .RHEN")
        embed.add_field(name="__**Descripción**__", value="Saca un hentai aleatorio de ||NHENTAI.NET||", inline=False)
        embed.add_field(name="__**Uso**__", value=".rhen",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)
    
    @help.group()
    async def pesca(self, ctx):
        embed=discord.Embed(title=" ")
        embed.set_author(name="HELP .PESCA")
        embed.add_field(name="__**Descripción**__", value="Tira la caña en uno de los lagos:\n\t->Lago 1 (lago1): lv 1\n\t->Lago 2 (lago2): lv 25\n\t->Lago 3 (lago3): lv 50\n\t->Lago 4 (lago3): lv 75", inline=False)
        embed.add_field(name="__**Argumentos**__", value="->lago1/lago2/lago3/lago4\n->inventario\n->stats\n->vender", inline=False)
        embed.add_field(name="__**Uso**__", value=".pesca <argumento>",inline=False)
        
        embed.set_footer(text="<> = parámetro obligatorio | [] parámetro opcional")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(comandoHelp(bot))