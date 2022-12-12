import asyncio

import discord
from redbot.core import commands


def reply(ctx):
    if hasattr(ctx.message, "reference") and ctx.message.reference is not None:
        msg = ctx.message.reference.resolved
        if isinstance(msg, discord.Message):
            return msg


class WhoAsked(commands.Cog):
    """
    When you just have to ask who the hell asked?
    """

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    @commands.command()
    async def whoasked(self, ctx, *, reply_or_message_id: str = None):
        """
        Who Asked?
        """
        if reply_or_message_id:
            try:
                message_id = ctx.channel.get_partial_message(reply_or_message_id)
                m = await message_id.reply(
                    "Now playing:\nWho Asked (Feat. Nobody Did)\n⚪──────────────\n◄◄⠀▐▐⠀►► 0:00 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n───⚪───────────\n◄◄⠀▐▐⠀►► 1:34 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────⚪────────\n◄◄⠀▐▐⠀►► 2:21 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n─────────⚪─────\n◄◄⠀▐▐⠀►► 3:08 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n────────────⚪──\n◄◄⠀▐▐⠀►► 3:55 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────────────⚪\n◄◄⠀▐▐⠀►► 4:42 / 4:42⠀───○ 🔊"
                )
            except discord.HTTPException:
                await ctx.send("Invalid message id.")

        else:
            try:
                message_id = ctx.message.reference.resolved
                m = await message_id.reply(
                    "Now playing:\nWho Asked (Feat. Nobody Did)\n⚪──────────────\n◄◄⠀▐▐⠀►► 0:00 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n───⚪───────────\n◄◄⠀▐▐⠀►► 1:34 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────⚪────────\n◄◄⠀▐▐⠀►► 2:21 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n─────────⚪─────\n◄◄⠀▐▐⠀►► 3:08 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n────────────⚪──\n◄◄⠀▐▐⠀►► 3:55 / 4:42⠀───○ 🔊"
                )
                await asyncio.sleep(1)
                await m.edit(
                    content="Now playing:\nWho Asked (Feat. Nobody Did)\n──────────────⚪\n◄◄⠀▐▐⠀►► 4:42 / 4:42⠀───○ 🔊"
                )

            except discord.HTTPException:
                await ctx.send("Invalid Reply.")
