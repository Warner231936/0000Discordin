import discord
import aiohttp
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config['bot']['token']
BROADCAST_URL = config['bot']['broadcast_url']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def broadcast_message(message, is_request=False):
    data = {
        'user': str(message.author),
        'content': message.content,
        'is_request': is_request,
    }
    try:
        async with aiohttp.ClientSession() as session:
            await session.post(BROADCAST_URL, json=data)
    except Exception as e:
        print(f'Broadcast failed: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    is_req = message.content.startswith('!req')
    await broadcast_message(message, is_request=is_req)
    if is_req:
        await message.channel.send('Request received.')

client.run(TOKEN)
