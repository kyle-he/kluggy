from datetime import datetime
from helpers.time import strfdelta
from typing import Union

import discord
from discord.ext import commands

UWU_KIDS = (
    287025331465093120,
    344299314262048769
)


class Moderation(commands.Cog):
    """For basic bot operation."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in UWU_KIDS:
            await message.delete()


def setup(bot):
    bot.add_cog(Moderation(bot))
