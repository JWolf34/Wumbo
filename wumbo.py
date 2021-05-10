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

@client.command()
async def subscribe(ctx, gameName):
    games = sql.selectGameWithName(gameName)

    if len(games) == 0:
        await ctx.send("I didn't find any games with that title. Try a different game.")

    elif len(games) == 1:
        isUserSubscribed = sql.isUserSubscribed(games[0], ctx.author.id)

        if isUserSubscribed:
            await ctx.send("You're already subscribed to " + games[0] + ".")
        else:
            sql.insertSubscription(ctx.author.id, games[0])
            await ctx.send("You've subscribed to " + games[0] + "!")
            
    elif len(games) > 1:
        #TODO
        pass



    
sql.selectGameWithName("A")


client.run(TOKEN)
