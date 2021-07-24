from datetime import datetime
from helpers.time import strfdelta
from typing import Union

import discord
from discord.ext import commands

UWU_KIDS = (
    280186658723463170,
    344299314262048769,
    361387744775110666,
    485641940826849292,
)


class Moderation(commands.Cog):
    """For basic bot operation."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id in UWU_KIDS and (
            message.content.count("w") >= len(message.content) / 2
            or "uw" in message.content
        ):
            await message.delete()
            await message.channel.send(f"<@!{message.author.id}> watch the w's!")


def setup(bot):
    bot.add_cog(Moderation(bot))
