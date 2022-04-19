import random

import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import pagify


class Pp(commands.Cog):
    """pp"""

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    @commands.command()
    async def pp(self, ctx, *users: discord.Member):
        """
        Detects user's pp length This is 100% accurate.

        Enter multiple users for an accurate comparison!

        """
        if not users:
            users = {ctx.author}

        lengths = {}
        state = random.getstate()
        owner_id = str(ctx.bot.owner_ids)
        bot_owner = int(owner_id.strip("{}"))

        for user in users:
            random.seed(str(user.id))

            if user.id in (ctx.bot.user.id, bot_owner):
                length = 35
            else:
                length = random.randint(0, 30)

            lengths[user] = f'8{"=" * length}D'

        random.setstate(state)
        lengths = sorted(lengths.items(), key=lambda x: x[1])

        msg = "".join(
            "**{}'s size:**\n{}\n".format(user.display_name, length) for user, length in lengths
        )

        for page in pagify(msg):
            await ctx.send(page)
