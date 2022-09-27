import re

import aiohttp
import discord
from redbot.core import commands
from redbot.core.utils.common_filters import URL_RE

from .rickrolldb import rickrolls_links, rickrolls_list


class AntiRickRoll(commands.Cog):
    """
    Auto detect rickrolls and notify users about it.
    """

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())

    @commands.Cog.listener()
    async def on_message_without_command(self, message):
        content = message.clean_content
        if (
            not isinstance(message.channel, discord.TextChannel)
            or message.type != discord.MessageType.default
            or message.author.id == self.bot.user.id
            or message.author.bot
            or message.clean_content is None
            or not URL_RE.search(content)
        ):
            return
        match = any(word in content for word in rickrolls_links)
        if match:
            await message.reply("Warning : This is mostly a rickroll.")
        elif link := re.findall(r"(https?://[^\s]+)", content):
            async with self.session.get(str(link[0])) as resp:
                match = any(word in str(resp) for word in rickrolls_links or rickrolls_list)
                if match:
                    await message.reply("Warning : This is mostly a rickroll.")
