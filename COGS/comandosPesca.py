from discord import embeds
from discord.ext import commands
from . import database
import discord
import random
class comandosPesca(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=['p', 'Pesca', 'PESCA'])
    async def pesca(self, ctx, *, atributo:str = None):
        #database.doesExist(ctx.author.id)
        #comprobar si existe al unirse un miembro..
        if 'lago' not in ctx.channel.name.lower():
            await ctx.send("¡Los comandos de pesca se deben usar en un canal que contenga 'lago' en el nombre!")
            return
        if atributo is None:
            await ctx.send('Usa `.help pesca` para más info sobre este comando!')
            return
        
        fishingLVL = database.getFishingLevel(ctx.author.id)[0][0]
        if(atributo in ('lago1', 'lago 1', '1', 'l1', 'l 1', 'Lago 1', 'L1', 'L 1') ):
            if fishingLVL > 0:
                listaPeces = database.getPecesbyDifficulty("Difficulty1")
            else:
                await ctx.send(f"Tu nivel es demasiado bajo!\nNivel actual: {fishingLVL} | Nivel requerido: 1")
                return
        elif(atributo in ('lago2', 'lago 2', '2', 'l2', 'l 2', 'Lago 2', 'L2', 'L 2') ):
            if fishingLVL >= 25:
                listaPeces = database.getPecesbyDifficulty("Difficulty2")
            else:
                await ctx.send(f"Tu nivel es demasiado bajo!\nNivel actual: {fishingLVL} | Nivel requerido: 25")
                return
        elif(atributo in ('lago3', 'lago 3', '3', 'l3', 'l 3', 'Lago 3', 'L3', 'L 3')):
            if fishingLVL >= 50:
                listaPeces = database.getPecesbyDifficulty("Difficulty3")
            else:
                await ctx.send(f"Tu nivel es demasiado bajo!\nNivel actual: {fishingLVL} | Nivel requerido: 50")
                return
        elif(atributo in ('lago4', 'lago 4', '4', 'l4', 'l 4', 'Lago 4', 'L4', 'L 4') ):
            if fishingLVL >= 75:
                listaPeces = database.getPecesbyDifficulty("Difficulty4")
            else:
                await ctx.send(f"Tu nivel es demasiado bajo!\nNivel actual: {fishingLVL} | Nivel requerido: 75")
                return
        else:
            await ctx.send("Argumento inválido. Usa `.help pesca` para más informacion sobre el comando!")
            return
        #importar mas lagos
        weight = []
        for _, _, _, _, diff in listaPeces:
            weight.append(diff/100)

        pescaChoice = random.choices(population=listaPeces, weights=weight)
        #tenemos el pescado ya, añadirlo con la base de datos
        _indexPescaChoice = listaPeces.index(pescaChoice[0])
        cosa = database.addFishofTier(pescaChoice[0][0], ctx.author.id)
        if cosa[0]:
            for _, name, XP, price, _ in pescaChoice:
                if price > 0:
                    string = f">**{ctx.author.mention}**< ha pescado *`{name} ({weight[_indexPescaChoice] * 100} %)`* valorado en __`{price} €`__!\nHa ganado **`{XP} xp`** y ha subido a nivel {cosa[1]}"
                else:
                    string = f">**{ctx.author.mention}**< ha pescado *`{name} ({weight[_indexPescaChoice] * 100} %)`* !\nHa ganado **`{XP} xp`** y ha subido a nivel {cosa[1]}"
        else:
            for _, name, XP, price, _ in pescaChoice:
                if price > 0:
                    string = f">**{ctx.author.mention}**< ha pescado *`{name} ({weight[_indexPescaChoice] * 100} %)`* valorado en __`{price} €`__!\nHa ganado **`{XP} xp`**!"
                else:
                    string = f">**{ctx.author.mention}**< ha pescado *`{name} ({weight[_indexPescaChoice] * 100} %)`* !\nHa ganado **`{XP} xp`**!"
        await ctx.send(string)
    @pesca.group(aliases=['inventory', 'Inv', 'inv', 'Inventory'])
    async def inventario(self, ctx):
        listaInv = database.getInventarioPesca(ctx.author.id)
        listaPeces = database.getInfoPeces()
        if listaInv:
            #inventory, first three are level, rod and id
            for  _, rodTier, _, _, _, ftier1, ftier2, ftier3, ftier4, ftier5, ftier6, ftier7, ftier8, ftier9, ftier10, btier1, btier2, btier3, btier4, btier5, cofresTesoro, llavesTesoro, trash in listaInv:
                embed=discord.Embed(title=" ", color=0x0f45ff)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                embed.set_author(name=f"Inventario de {ctx.author.display_name}")
                embed.add_field(name="__**Caña de pescar**__", value=f"Tier: {rodTier}")
                embed.add_field(name="__**Tesoros**__", value=f"Llaves: {llavesTesoro}\nCofres: {cofresTesoro}\n*(**{listaPeces[0][1]} €**) Basura:* {trash}", inline=False)
                embed.add_field(name="__**Peces**__", value=f"(**{listaPeces[1][1]} €**) {listaPeces[1][0]}: {ftier1}\n(**{listaPeces[2][1]} €**) {listaPeces[2][0]}: {ftier2}\n(**{listaPeces[3][1]} €**) {listaPeces[3][0]}: {ftier3}\n(**{listaPeces[4][1]} €**) {listaPeces[4][0]}: {ftier4}\n(**{listaPeces[5][1]} €**) {listaPeces[5][0]}: {ftier5}\n(**{listaPeces[6][1]} €**) {listaPeces[6][0]}: {ftier6}\n(**{listaPeces[7][1]} €**) {listaPeces[7][0]}: {ftier7}\n(**{listaPeces[8][1]} €**) {listaPeces[8][0]}: {ftier8}\n(**{listaPeces[9][1]} €**) {listaPeces[9][0]}: {ftier9}\n(**{listaPeces[10][1]} €**) {listaPeces[10][0]}: {ftier10}", inline=False)
                embed.add_field(name="__**Cebos**__", value=f"Tier 1: {btier1}\nTier 2: {btier2}\nTier 3: {btier3}\nTier 4: {btier4}\nTier 5: {btier5}", inline=False)
                await ctx.send(embed=embed)
    @pesca.group(aliases=['s', 'Stats', 'stat', 'stats'])
    async def estadisticas(self, ctx):
        stats = database.getFishingLevel(ctx.author.id)
        embed = discord.Embed(title=" ", color=0x0f45ff)
        embed.set_image(url=ctx.author.avatar_url)
        embed.set_author(name=f"Estadisticas de {ctx.author.display_name}")
        embed.add_field(name="------------PESCA-------------", value=f"**__Nivel__**: {stats[0][0]}\n**__Experiencia actual__**: {stats[0][1]} xp\n**__Experiencia para próximo nivel__**: {round(stats[0][2],2)} xp")
        await ctx.send(embed=embed)
    
    @pesca.group(aliases=['Sell', 'sell'])
    async def vender(self, ctx):
        dineroGanado = database.sellFish(ctx.author.id)
        if dineroGanado[0] > 0:
            if dineroGanado[1] > 0 and dineroGanado[2] == 0:
                await ctx.send(f">{ctx.author.mention}<\nHas vendido {dineroGanado[1]} piezas de basura.\nHas ganado *`{dineroGanado[0]} €`*")
                return
            elif dineroGanado[1] == 0 and dineroGanado[2] > 0:
                await ctx.send(f">{ctx.author.mention}<\nHas vendido {dineroGanado[2]} peces.\nHas ganado *`{dineroGanado[0]} €`*")
                return
            elif dineroGanado[1] >0 and dineroGanado[2] > 0:
                await ctx.send(f">{ctx.author.mention}<\nHas vendido {dineroGanado[1]} piezas de basura y {dineroGanado[2]} peces.\nHas ganado *`{dineroGanado[0]} €`*")
                return
        else:
            await ctx.send(f">{ctx.author.mention}\nNo tienes nada que vender!")
def setup(bot):
    bot.add_cog(comandosPesca(bot))