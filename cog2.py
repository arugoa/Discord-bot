import discord
from discord.ext import commands, tasks
import random
from random import choice
from itertools import cycle

class Basic_Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'WAZZAA!')

    
    #This is repeat phrase command
    @commands.command()
    async def repeat(self, ctx, *, phrase):
        await ctx.send(f'{phrase}')

    @repeat.error
    async def repeat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the message to send.')


    #This is an 8ball command with yes/no answers to qns
    @commands.command(aliases = ['8ball'])
    async def _8ball(self, ctx, *, question):
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

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specify the question to answer.')


    
def setup(client):
    client.add_cog(Basic_Commands(client))
