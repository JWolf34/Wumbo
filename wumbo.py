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

@client.command()
async def register(ctx):
    user = ctx.author
    user_attributes = [user.id, user.name, user.nick]

    log.info("Registering new user to the database...")

    try:
        sql.insertUser(user_attributes)
        log.info("Successfully added new user " + user.name + "!")
        await ctx.send("You've registered with Wumbo! Thanks!")
    except Exception as e:
        log.exception(e)
        error = str(e)
        if "duplicate" in error:
            log.debug("User has already registered with the bot.")
            await ctx.send("You've already registered with Wumbo")
        else:
            log.error("Encountered an error registering the user")
            await ctx.send("Hmm... I couldn't register you. Try again later.")
    



client.run(TOKEN)
