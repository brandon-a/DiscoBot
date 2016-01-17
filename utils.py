import discord

"""
Some miscellaneous util functions for DiscoBot
"""

def get_channel(bot, server_name, channel_name):
    server = discord.utils.get(bot.servers, name=server_name)
    try:
        return discord.utils.get(server.channels, name=channel_name)
    except Exception:
        return None

def is_admin(member):
    if discord.utils.get(member.roles, name='Admin'):
        return True
    else:
        return False
