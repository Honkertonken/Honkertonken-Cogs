import re

import discord
from redbot.core import commands
from redbot.core.config import Config

search = re.compile(
    (r"(?<![a-z])i'?m ([^\.\?\!,\n\r]+)"),
    flags=re.I,
)


class HiBack(commands.Cog):
    """
    Replies to "I'm X" with "Hi, X".
    """

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=694835810347909161,
            force_registration=True,
        )
        default_guild = {
            "enabled": True,
            "dad": False,
            "blacklisted_ids": [],
        }
        self.config.register_guild(**default_guild)

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    @commands.group()
    @commands.admin_or_permissions()
    @commands.guild_only()
    async def hibackset(self, ctx):
        """
        HiBack settings.
        """

    @hibackset.command()
    async def enable(self, ctx, enable_or_disable: bool):
        """
        Enable/disable the hi back feature.
        """
        async with ctx.typing():
            await self.config.guild(ctx.guild).enabled.set(enable_or_disable)
        if enable_or_disable:
            await ctx.send("Auto Hi Back has been enabled for this guild.")
        else:
            await ctx.send("Auto Hi back has been disabled for this guild.")

    @hibackset.command()
    async def dad(self, ctx, enable_or_disable: bool):
        """
        Add a "im dad" to the hi back message.
        """
        async with ctx.typing():
            await self.config.guild(ctx.guild).dad.set(enable_or_disable)
        if enable_or_disable:
            await ctx.send('"Im dad" shall now be added to auto hi back messages.')
        else:
            await ctx.send('"Im dad" shall not be added to auto hi back messages.')

    @hibackset.command(aliases=["blacklist", "bl"])
    async def add(self, ctx, user: discord.User):
        """
        Add a user to get exempted by auto hi back messages.
        """
        async with ctx.typing():
            ids = await self.config.guild(ctx.guild).blacklisted_ids()
            ids.append(user.id)
            await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will be exempted from auto hi back messages.")

    @hibackset.command(aliases=["unblacklist", "unbl"])
    async def remove(self, ctx, user: discord.User):
        """
        Remove a user from getting exempted by auto hi back messages.
        """
        async with ctx.typing():
            ids = await self.config.guild(ctx.guild).blacklisted_ids()
            ids.remove(user.id)
            await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will not be exempted from auto hi back messages.")

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, message):
        """
        Handle on_message.
        """
        if not await self.config.guild(message.guild).enabled():
            return
        if (
            not isinstance(message.channel, discord.TextChannel)
            or message.type != discord.MessageType.default
            or message.author.id == self.bot.user.id
            or message.author.bot
            or message.clean_content is None
            or message.author.id in await self.config.guild(message.guild).blacklisted_ids()
        ):
            return
        content = message.clean_content
        dad = ", im dad" if await self.config.guild(message.guild).dad() else " "
        if search.search(content):
            try:
                back = search.search(content).group(1)
                await message.reply(
                    f"Hi {back}{dad}",
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, roles=False, users=False
                    ),
                )
            except (
                discord.HTTPException,
                discord.Forbidden,
            ):
                pass
