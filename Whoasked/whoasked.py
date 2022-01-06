import asyncio

import discord
from redbot.core import commands


class WhoAsked(commands.Cog):
    """When you just have to ask who the hell asked?"""

    @commands.command()
    async def whoasked(self, ctx, message: discord.PartialMessage):
        """Who Asked?"""
        try:
            m = await message.reply(
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
            await ctx.send("Incorrect/Invalid Message Id.")
