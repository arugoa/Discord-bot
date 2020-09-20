
import discord
import os
from discord.ext import commands, tasks
import random
from random import choice
from itertools import cycle


client = commands.Bot(command_prefix = '.')
status = cycle(['.help', 'Just bored', 'Learning new things', 'Hacking into the computer'])
def is_it_me(ctx):
    return ctx.author.id == 691288932486348863


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permissions to run this command.')

        
@client.event
async def on_ready():
    print('Bot is ready')
    change_status.start()


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))


@client.command()
@commands.check(is_it_me)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



client.run('NzM2NTI4MTczNDE1NTMwNTQ5.XxwHUA.oHgL0-NxMKGdGAGkVZAZfKWrBu0')






# these commands are in loaded files

'''
#These are events that will only be shown in the IDE

@client.event
async def on_ready():
    print("Bot is ready")



@client.event
async def on_ready():
    print("Bot is ready")
    change_status.start()


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(next(status)))




@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')


#These are executable commands


#This is ping command which replies to .ping

@client.command()
async def ping(ctx):
    await ctx.send(f'WAZZAA! {round(client.latency * 1000)}ms')

#This is repeat phrase command

@client.command()
async def repeat(ctx, *, phrase):
    await ctx.send(f'{phrase}')


#This is clear chat command

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)


#This is an 8ball command with yes/no answers to qns

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

'''



'''
#This is the kick command

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)


#This is the ban command

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


#This is the unban command

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return



@client.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify the number of messages to delete.')
'''




