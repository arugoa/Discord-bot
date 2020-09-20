import discord
from discord.ext import commands, tasks
import random
from random import choice
from itertools import cycle


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Events   
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        change_status.start()
    '''

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')
    

def setup(client):
    client.add_cog(Example(client))
