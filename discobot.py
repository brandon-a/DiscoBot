import discord
from discord.ext import commands
import random
import datetime
import json
import general
import regions
import fun

with open('config.json', 'r') as c_json:
    config = json.load(c_json)

description = '''I'm DiscoBot, a simple discord bot!

Command prefix: {0}'''.format(config['prefix'])
bot = commands.Bot(command_prefix=config['prefix'], description=description)
t0 = datetime.datetime.now()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_member_join(member):
    pm = 'Welcome to the gaymers discord! \n type \'!help\' to see how I work. \n If you have any questions, pm the admins!'
    await bot.send_message(member.server, 'Welcome {0}!'.format(member))
    await bot.send_message(member, pm)

@bot.command()
async def uptime():
    """Check uptime."""
    global t0
    await bot.say(timedelta_str(datetime.datetime.now() - t0))

def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, _ = divmod(r, 60)
    return '{0} days, {1} hours and {2} minutes'.format(days, hours, minutes)

def setup(bot, config):
    if 'general' in config['modules']:
        bot.add_cog(general.GeneralCommands(bot, config['general']))
    if 'regions' in config['modules']:
        bot.add_cog(regions.RegionCommands(bot, config['regions']))
    if 'fun' in config['modules']:
        bot.add_cog(fun.FunCommands(bot))

setup(bot, config)
bot.run(config['credentials']['email'], config['credentials']['password'])
