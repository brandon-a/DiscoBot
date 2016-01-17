import discord
from discord.ext import commands
import random

import general
import regions

description = '''I'm DiscoBot, a simple bot for the discord gaymers channel.

Command prefix: !'''
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    await bot.send_message(member.server, 'Welcome {0}!'.format(member))
    await bot.send_message(member, 'Welcome to the gaymers discord! \
                                    type \'!help\' to see how I work. \
                                    If you have any questions, pm the admins!')

def setup(bot):
    bot.add_cog(general.GeneralCommands(bot))
    bot.add_cog(regions.RegionCommands(bot))

setup(bot)
bot.run(email, pw)
