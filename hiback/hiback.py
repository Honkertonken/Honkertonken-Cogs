import re

import discord
from redbot.core import commands

search = re.compile(
    (r"(?<![a-z])i'?m ([^\.\?\!,\n\r]+)"),
    flags=re.I,
)


class HiBack(commands.Cog):
    """Replies to "I'm X" with "Hi, X"."""

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        return

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, message):
        """Handle on_message."""

        if (
            not isinstance(message.channel, discord.TextChannel)
            or message.type != discord.MessageType.default
            or message.author.id == self.bot.user.id
            or message.author.bot
            or message.clean_content is None
        ):

            return
        content = message.clean_content
        if search.search(content):
            try:
                back = search.search(content).group(1)
                await message.reply(
                    f"Hi {back}",
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, roles=False, users=False
                    ),
                )
            except (
                discord.HTTPException,
                discord.Forbidden,
            ):
                pass
