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

@client.event
#When a member leaves or is kicked from the server their exit is announced.
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
#Context is passed automatically. Command prints user's ping in Discord.
async def ping(ctx):
    await ctx.send(f' Your ping is {round(client.latency * 1000) ms'})

@client.command()
#The command clears the amount of messages specified when used Default = 5.
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
#The command kicks a user from the discord channel
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@client.command()
#The command bans the user from the discord
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason )

@client.command()
#The command unbans the user from Discord
async def unban(ctx, *, member): #Use member here is some names contain spaces

#Creates a named tuple containing user object and reason of ban.
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (memmber_name, member_discriminator):
            await ctx.guild.unban(user)
            return

#In the quotations include your bot token via the Python Dev Portal
client.run('')
