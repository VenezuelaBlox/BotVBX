from settings import settings
import random
import os
import aiohttp
import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_emoji, flip_coin, obtener_arepa


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='', intents=intents, help_command=None)

ALLOWED_CHANNEL_ID = 1501754471649378335



@bot.check
async def allowed_places(ctx):
    if ctx.guild is None:
        return True

    if ctx.channel.id == ALLOWED_CHANNEL_ID:
        return True

    await ctx.send("❌ Usa este bot en el canal permitido o por mensaje privado.")
    return False



@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')




@bot.command()
async def hello(ctx):
    await ctx.send('¡Hola! Soy un bot')

@bot.command()
async def smile(ctx):
    await ctx.send(gen_emoji())

@bot.command()
async def coin(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def passw(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def arepa(ctx):
    await ctx.send(obtener_arepa())


@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)



@bot.command()
async def meme(ctx):
    try:
        img_name = random.choice(os.listdir('images'))
        with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    except:
        await ctx.send("No hay imágenes disponibles 😢")




async def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data['url']


@bot.command()
async def duck(ctx):
    await ctx.send(await get_duck_image_url())


async def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data['url']


@bot.command()
async def dog(ctx):
    await ctx.send(await get_dog_image_url())


async def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data['image']


@bot.command()
async def fox(ctx):
    await ctx.send(await get_fox_image_url())


async def get_pokemon():
    pokemon_id = random.randint(1, 151)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()
            return data['name'], data['sprites']['front_default']


@bot.command()
async def pokemon(ctx):
    name, image = await get_pokemon()
    await ctx.send(f'Pokémon: {name}')
    await ctx.send(image)


async def search_anime(anime_name):
    url = f'https://kitsu.io/api/edge/anime?filter[text]={anime_name}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            data = await res.json()

            if not data['data']:
                return None

            anime = data['data'][0]
            title = anime['attributes']['canonicalTitle']
            synopsis = anime['attributes']['synopsis']

            return title, synopsis


@bot.command()
async def anime(ctx, *, nombre):
    result = await search_anime(nombre)

    if not result:
        await ctx.send("No encontré ese anime.")
        return

    title, synopsis = result

    if len(synopsis) > 500:
        synopsis = synopsis[:500] + "..."

    await ctx.send(f'🎌 Anime encontrado: {title}\n\n{synopsis}')




@bot.command(aliases=['ayuda'])
async def helpp(ctx):
    await ctx.send("""
📜 LISTA DE COMANDOS

!hello → Saluda al bot
!smile → Emoji aleatorio
!coin → Lanza moneda
!passw → Genera contraseña
!arepa → Arepa aleatoria

!add x y → Suma números
!heh n → Repite "he"
!meme → Imagen aleatoria

!duck → Pato
!dog → Perro
!fox → Zorro
!pokemon → Pokémon
!anime nombre → Buscar anime

!helpp / !ayuda → Lista de comandos
""")



@bot.event
async def on_command_error(ctx, error):
    pass  


bot.run(settings["TOKEN"])
