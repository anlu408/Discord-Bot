import discord
from discord.ext import commands

#Sets the commands set in discord chat to start with a . i.e. .help
client = commands.Bot(command_prefix = '.')

@client.event
#When the bot is ready with info from discord it is put into a ready state
async def on_ready():
    print('Bot is ready.')

@client.event
#When a new member joins the server their entrance is announced.
async def on_member_join(member):
    print(f'{member} has joined the server.')
#In the quotations include your bot token via the Python Dev Portal
client.run('')
