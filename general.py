import discord
import random
from discord.ext import commands
from utils import *

class GeneralCommands():
    """
    General commands for DiscoBot.
    """

    def __init__(self, bot, config):
        self.bot = bot
        self.ask_loc = [config['ask_server'], config['ask_channel']]

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

    @commands.command(description='Ask the admins', pass_context=True)
    async def ask(self, ctx, *question):
        """<question>: Ask the admins, by PM to DiscoBot."""
        question = ' '.join(question)
        if len(question) < 3:
            return
        author = ctx.message.author
        q_channel = get_channel(self.bot, self.ask_loc[0], self.ask_loc[1])
        if q_channel:
            print('q')
            await self.bot.send_message(q_channel,
                                    "{0}: {1}".format(author, question))

    @commands.command(description='A short DiscoBot description.')
    async def who(self):
        """More info on DiscoBot"""
        msg = '''Hi I'm Discobot, a Discord bot made with discord.py!
        For more info about me, visit https://github.com/Superbanaan/DiscoBot
        '''
        await self.bot.say(msg)
