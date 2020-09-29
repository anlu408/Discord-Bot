import discord
import os
from discord.ext import commands

#Sets the commands set in discord chat to start with a . i.e. .help
client = commands.Bot(command_prefix = '.')

"""
The lines of code below import any other Python file found in Cogs.
At the moment it just includes the basic bot.py along with the
Commands.py that includes the commands available to our bot.
"""

#Allows user to load and unload referenced .py files
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.load_extension(f'cogs.{extension}')

for filewname in os.listdr('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]})

#In the quotations include your bot token via the Python Dev Portal
client.run('')
