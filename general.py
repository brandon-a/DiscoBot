import discord
import random
from discord.ext import commands
from utils import *

class GeneralCommands():
    """
    General commands for DiscoBot.
    """

    # Replies for the !poke command (we need A LOT more)
    replies = ['STOP TOUCHING ME!', 'LEAVE ME ALONE', 'can I go home now?',
               'It\'s dark in here..', 'AAAAAAAAAAAAH', 'NO', '*giggles*',
               '*moans*', ';)', ':(', 'h-hello?', '*pokes back*', 'D: not there!',
               'A bit lower...', 'WHAT DO YOU WANT?!', 'bleep', 'Well hello there ;)',
               '*blush* not now! everybody is watching..', '*falls over*', '*winks*',
               'N-nani']

    def __init__(self, bot):
        self.bot = bot

    @commands.command(description='Roll dice with m sides n times. format: <n>d<m>')
    async def roll(self, dice : str):
        """<n>d<m>: Roll dice with m sides n times."""
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await self.bot.say('Format has to be in <n>d<m>!')
            return

        if rolls > 20 or limit > 1000 or rolls < 1 or limit < 1:
            await self.bot.say("Sorry, can't do that!")
        else:
            result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
            await self.bot.say(result)

    @commands.command(description='Let DiscoBot choose for you!')
    async def choose(self, *choices : str):
        """<c1> <c2> ...: Let DiscoBot choose for you!"""
        await self.bot.say(random.choice(choices))

    @commands.command(description='Check when a member joined.')
    async def joined(self, member : discord.Member):
        """<member>: Check when a member joined."""
        await self.bot.say('{0.name} joined at {1}'.format(member,
                                        member.joined_at.strftime("%Y-%m-%d")))

    @commands.command()
    async def slap(self, member : discord.Member):
        """<member>: Be careful with this one."""
        await self.bot.say("*slaps {0} around a bit with \
                            a large, girthy trout*".format(member))

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

    @commands.command(description='Poke DiscoBot, yay!')
    async def poke(self):
        """Poke DiscoBot, yay!"""
        await self.bot.say(random.choice(self.c))

    @commands.command(description='Ask the admins', pass_context=True)
    async def ask(self, ctx, *question):
        """<question>: Ask the admins, either on the server or by PM to DiscoBot"""
        question = ' '.join(question)
        if len(question) < 3:
            return
        author = ctx.message.author
        q_channel = get_channel(self.bot, 'Gaymers', 'questions')
        if q_channel:
            print('q')
            await self.bot.send_message(q_channel,
                                    "{0}: {1}".format(author, question))
