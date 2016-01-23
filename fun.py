import discord
import random
from discord.ext import commands
from utils import *

class FunCommands():
    # Replies for the !poke command (we need A LOT more)
    replies = ['STOP TOUCHING ME!', 'LEAVE ME ALONE', 'can I go home now?',
               'It\'s dark in here..', 'AAAAAAAAAAAAH', 'NO', '*giggles*',
               '*moans*', ';)', ':(', 'h-hello?', '*pokes back*', 'D: not there!',
               'A bit lower...', 'WHAT DO YOU WANT?!', 'bleep', 'Well hello there ;)',
               '*blush* not now! everybody is watching..', '*falls over*', '*winks*',
               'N-nani']

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Poke DiscoBot, yay!')
    async def poke(self):
        """Poke DiscoBot, yay!"""
        await self.bot.say(random.choice(self.replies))

    @commands.command()
    async def slap(self, member : discord.Member):
        """<member>: Be careful with this one."""
        await self.bot.say("*slaps {0} around a bit with a large, girthy trout*".format(member))

    @commands.command(pass_context=True)
    async def lapdance(self, ctx):
        """Request a lapdance."""
        if ctx.message.server:
            if is_admin(ctx.message.author):
                await self.bot.say('*gives {0} a sexy lapdance*'\
                                    .format(ctx.message.author))
            else:
                await self.bot.say('NO!')
        else:
            await self.bot.say('I don\'t give private lapdances, you freak!')
