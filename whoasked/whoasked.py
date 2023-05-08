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
    async def whoasked(self, ctx: commands.Context, *, message_id: int = None):
        """
        Who asked?
        """
        message = get_replied_message(ctx) or ctx.message
        if message_id:
            try:
                message = await ctx.channel.fetch_message(message_id)
            except (discord.NotFound, ValueError):
                await ctx.send("Invalid message ID.")
                return
        m = await message.reply(
            "Now playing:\nWho Asked (Feat. Nobody Did)\n⚪──────────────\n◄◄⠀▐▐⠀►► 0:00 / 4:42⠀───○ 🔊",
        )
        await asyncio.sleep(1)
        await m.edit(
            content="Now playing:\nWho Asked (Feat. Nobody Did)\n───⚪───────────\n◄◄⠀▐▐⠀►► 1:34 / 4:42⠀───○ 🔊",
        )
        await asyncio.sleep(1)
        await m.edit(
            content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────⚪────────\n◄◄⠀▐▐⠀►► 2:21 / 4:42⠀───○ 🔊",
        )
        await asyncio.sleep(1)
        await m.edit(
            content="Now playing:\nWho Asked (Feat. Nobody Did)\n─────────⚪─────\n◄◄⠀▐▐⠀►► 3:08 / 4:42⠀───○ 🔊",
        )
        await asyncio.sleep(1)
        await m.edit(
            content="Now playing:\nWho Asked (Feat. Nobody Did)\n────────────⚪──\n◄◄⠀▐▐⠀►► 3:55 / 4:42⠀───○ 🔊",
        )
        await asyncio.sleep(1)
        await m.edit(
            content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────────────⚪\n◄◄⠀▐▐⠀►► 4:42 / 4:42⠀───○ 🔊",
        )
