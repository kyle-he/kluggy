import asyncio
import math
import random
import re
from datetime import datetime, timedelta

import discord
from discord.ext import commands, tasks


class Fun(commands.Cog):
    """Commands for server admins."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def throw(self, ctx, user: discord.User):
        throw_list = [
            "One million Yuji Stans",
            "a klugster",
            "Duvis Dunaway",
            "bob",
            "divorce papers",
            "lots of hate",
            "an angry klug letter",
            "a long and passive aggressive email",
            "the game industry",
            "Amy Hennig",
            "Earth and Beyond",
            "One 500-Word Essay on How You Got Fired",
            "pain",
            "spain without the s",
            "dog poop",
            "a data structures fan fiction",
            "jeffrey bezo's big ship",
            "a decade of pain",
            "a klug jug",
            "a G R E E T I N G",
            "a klug klock"
        ]
        await ctx.send(f"Threw **{random.choice(throw_list)}** at **{user}**")

def setup(bot):
    bot.add_cog(Fun(bot))

