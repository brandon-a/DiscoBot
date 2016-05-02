import discord
from discord.ext import commands

class RegionCommands():
    """
    Region commands for DiscoBot
    """

    def __init__(self, bot, config):
        self.bot = bot
        self.all_regions = config['all_regions']

    @commands.command(description='Display region message.')
    async def regions(self):
        """Display all possible regions."""
        msg = "To set or change your region, type '!setregion <region>' \n"
        msg +='Possible regions: '
        msg += ', '.join(self.all_regions)
        await self.bot.say(msg)

    @commands.command(description='Set your region', pass_context=True)
    async def setregion(self, ctx, *region : str):
        """<region>: Set your region, for more help type'!regions'."""
        if ctx.message.server:
            region = ' '.join(region)
            if region in self.all_regions:
                author = ctx.message.author
                new_roles = [role for role in author.roles \
                             if role.name not in self.all_regions]
                d_role = discord.utils.get(ctx.message.server.roles,
                                           name=region)
                if d_role:
                    new_roles.append(d_role)
                await self.bot.replace_roles(author, *new_roles)
                await self.bot.say('Region set successfully.')
        else:
            await self.bot.say('I cannot set your region here!')
