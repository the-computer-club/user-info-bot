import discord 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=942432077079535656))
    print('Bot is ready')

@tree.command(name='lookup', guild = discord.Object(id=942432077079535656))
async def lookup(ctx, username: str):
    await ctx.response.send_message('Artist: ' + username)

@tree.command(name='insert', guild = discord.Object(id=942432077079535656))
async def insert(ctx, artist: str):
    pass

@tree.command(name='refresh', description='refreshes the known artists list', guild = discord.Object(id=942432077079535656))
async def refresh(ctx):
    pass

if __name__ == '__main__':
    token = open('secrets/token.txt', 'r').read()
    client.run(token)
