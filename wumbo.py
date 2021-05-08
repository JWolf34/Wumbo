import discord
from discord.ext import commands
import json
import log
import sql


with open('config.json') as config_file:
    data = json.load(config_file)

TOKEN = data['discord'][0]['token']

client = commands.Bot(command_prefix='!')



@client.event
async def on_ready():
    log.info('***STARTUP***')


client.run(TOKEN)
