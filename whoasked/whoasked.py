import asyncio

import discord
from redbot.core import commands


def get_replied_message(ctx: commands.Context) -> discord.Message:
    """Returns the message that the user is replying to, or None."""
    if hasattr(ctx.message, "reference") and ctx.message.reference is not None:
        return ctx.message.reference.resolved

class WhoAsked(commands.Cog):
    """
    When you just have to ask who the hell asked?
    """

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    @commands.command()
    async def whoasked(self, ctx: commands.Context, *, message_id: str = None):
        """
        Who asked?
        """
        message = get_replied_message(ctx) or ctx.message

        if message_id:
            try:
                message = await ctx.channel.fetch_message(int(message_id))
            except (discord.NotFound, ValueError):
                await ctx.send("Invalid message ID.")
                return

        text = "Now playing:\nWho Asked (Feat. Nobody Did)\n"
        for i in range(6):
            content = f"{text}{'─'*i}⚪{'─'*(5-i)}\n◄◄⠀▐▐⠀►► {i*53//10:02d}:{i*53%10:02d} / 4:42⠀───○ 🔊"
            message = await message.reply(content)
            await asyncio.sleep(1)
            await message.edit(content)
