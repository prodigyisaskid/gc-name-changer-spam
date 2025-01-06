import discord
from discord.ext import commands
import time
import getpass

client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_ready():
    print('Logged in as', client.user)

    channel_id = int(input('gc ID: '))
    initial_name = input('gc name: ')
    channel = client.get_channel(channel_id)

    if channel is not None:
        count = 1
        while True:
            await channel.edit(name=f'{initial_name} {count}')
            count += 1
            time.sleep(0)
    else:
        print('Could not find the specified channel.')

client.run("token here", bot=False)
