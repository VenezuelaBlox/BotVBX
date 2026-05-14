from settings import settings
import discord
from bot_logic import gen_pass, gen_emoji, flip_coin, obtener_arepa

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('emoji'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('moneda'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('smile'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('arepa'):
        await message.channel.send(obtener_arepa())
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run(settings["TOKEN"])
