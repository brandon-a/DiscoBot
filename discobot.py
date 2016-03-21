import random
import datetime
import json
import discord
from discord.ext import commands
import general
import regions
import actions

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
    pm = 'Welcome to {0}!\ntype \'!help\' to see how I work.\nTo set your region type !regions in any channel on the server.\nTo gain access to the #over-18 channel, type !set18 in any channel on the server.\nIf you have any questions, use the !ask command or PM one of the admins.'.format(member.server)
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
    if minutes == 1:
        return '{0} days, {1} hours and {2} minute'.format(days, hours, minutes)
    else:
        return '{0} days, {1} hours and {2} minutes'.format(days, hours, minutes)

def setup(bot, config):
    if 'general' in config['modules']:
        bot.add_cog(general.GeneralCommands(bot, config['general']))
    if 'regions' in config['modules']:
        bot.add_cog(regions.RegionCommands(bot, config['regions']))
    if 'actions' in config['modules']:
        bot.add_cog(actions.Actions(bot))

setup(bot, config)
bot.run(config['credentials']['email'], config['credentials']['password'])
