import discord
import random
from discord.ext import commands
from utils import *

class Actions():
    # Replies for the !poke command (we need A LOT more)
    poke_replies = ['STOP TOUCHING ME!', 'LEAVE ME ALONE', 'can I go home now?',
               'It\'s dark in here..', 'AAAAAAAAAAAAH', 'NO', '*giggles*',
               '*moans*', ';)', ':(', 'h-hello?', '*pokes back*', 'D: not there!',
               'A bit lower...', 'WHAT DO YOU WANT?!', 'bleep', 'Well hello there ;)',
               '*blush* not now! everybody is watching..', '*falls over*', '*winks*',
               'N-nani']
    hug_replies = ['*hugs {0}*', '*hugs {0}*', '*hugs {0}*', '*hugs {0}*',
                   '*licks {0}*', '*pounces {0}*', '*jumps on {0}*',
                   '*glomps {0}*', '*falls on {0}*']
    slap_replies = ['*slaps {0} around a bit with a large, girthy trout*', '*slaps {0} with a meaty sausage*']               

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Poke DiscoBot, yay!')
    async def poke(self):
        """Poke DiscoBot, yay!"""
        await self.bot.say(random.choice(self.poke_replies))

    @commands.command()
    async def slap(self, member : discord.Member):
        """<member>: Be careful with this one."""
        await self.bot.say("*slaps {0} around a bit with a large, girthy trout*".format(member))

    #@commands.command()
    #async def slap(self, member : discord.Member):
    #     """<member>: Be careful with this one."""
    #    await self.bot.say(random.choice(self.slap_replies).format(member))    

    @commands.command()
    async def spray(self, member : discord.Member):
        """<member>: Be careful with this one."""
        await self.bot.say("*sprays {0} with the fire hose*".format(member))    

    @commands.command()
    async def hug(self, member : discord.Member):
        """<member>: Show some love!"""
        await self.bot.say(random.choice(self.hug_replies).format(member))

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
