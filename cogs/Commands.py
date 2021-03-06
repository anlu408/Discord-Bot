import Discord
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, client):
        self.client = client

#Events
#Function decorator within a Cog
@commands.cog.listener()
# Self must be the first argument that every function in the class takes.
async def on_ready(self):
    print('Bot is Online')

@commands.cog.listener()
#When the bot is ready with info from discord it is put into a ready state
async def on_ready(self):
    print('Bot is ready.')

@commands.cog.listener()
#When a new member joins the server their entrance is announced.
async def on_member_join(member):
    print(f'{member} has joined the server.')

@commands.cog.listener()
#When a member leaves or is kicked from the server their exit is announced.
async def on_member_remove(member):
    print(f'{member} has left the server')

#Commands
@commands.command()
#Context is passed automatically. Command prints user's ping in Discord.
async def ping(self,ctx):
    await ctx.send(f' Your ping is {round(client.latency * 1000) ms'})

@commands.command()
#The command clears the amount of messages specified when used Default = 5.
async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@commands.command()
#The command kicks a user from the discord channel
async def kick(self, ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)

@commands.command()
#The command bans the user from the discord
async def ban(self, ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason )

@commands.command()
#The command unbans the user from Discord
async def unban(self, ctx, *, member): #Use member here is some names contain spaces
#Creates a named tuple containing user object and reason of ban.
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if(user.name, user.discriminator) == (memmber_name, member_discriminator):
            await ctx.guild.unban(user)
            return=

def setup(client):
    client.add.cog(Example(client))
