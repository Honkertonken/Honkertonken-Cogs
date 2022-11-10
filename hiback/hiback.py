import contextlib
import re

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

search = re.compile(
    (r"(?<![a-z])i'?m ([^\.\?\!,\n\r]+)"),
    flags=re.I,
)


class HiBack(commands.Cog):
    """
    Replies to "I'm X" with "Hi, X".
    """

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=694835810347909161,
            force_registration=True,
        )
        default_guild = {
            "enabled": True,
            "dad": False,
            "ping": True,
            "blacklisted_ids": [],
            "restricted": None,
            "restricted_channels": [],
        }
        self.config.register_guild(**default_guild)

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    @commands.group()
    @commands.guild_only()
    @commands.admin_or_permissions()
    async def hibackset(self, ctx):
        """
        HiBack settings.
        """

    @hibackset.command(name="enable")
    async def hibackset_enable(self, ctx):
        """
        Enable the hi back feature.
        """
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("Auto hi back has been enabled for this guild.")

    @hibackset.command(name="disable")
    async def hibackset_disable(self, ctx):
        """
        Disable the hi back feature.
        """
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("Auto hi back has been disabled for this guild.")

    @hibackset.command(name="dad")
    async def hibackset_dad(self, ctx, true_or_false: bool):
        """
        Add a "im dad" to the hi back messages.
        """
        await self.config.guild(ctx.guild).dad.set(true_or_false)
        if true_or_false:
            await ctx.send('"Im dad" shall now be added to auto hi back messages.')
        else:
            await ctx.send('"Im dad" shall not be added to auto hi back messages.')

    @hibackset.command(name="ping")
    async def hibackset_ping(self, ctx, true_or_false: bool):
        """
        Ping users on the hi back messages.
        """
        await self.config.guild(ctx.guild).ping.set(true_or_false)
        if true_or_false:
            await ctx.send("Users will now be pinged on auto hi back messages.")
        else:
            await ctx.send("Users will not be pinged on auto hi back messages.")

    @hibackset.command(name="ignore", aliases=["blacklist", "bl"])
    async def hibackset_ignore(self, ctx, user: discord.Member):
        """
        Ignore a user from the auto hi back messages.
        """
        ids = await self.config.guild(ctx.guild).blacklisted_ids()
        ids.append(user.id)
        await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will be exempted from auto hi back messages.")

    @hibackset.command(name="unignore", aliases=["unblacklist", "unbl"])
    async def hibackset_unignore(self, ctx, user: discord.Member):
        """
        Remove a user from getting exempted by auto hi back messages.
        """
        ids = await self.config.guild(ctx.guild).blacklisted_ids()
        ids.remove(user.id)
        await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will not be exempted from auto hi back messages.")

    @hibackset.command(name="restrict")
    async def hibackset_restrict(self, ctx, restrict: str = None):
        """
        Restrict the hiback feature, supports blocklist and allowlist.
        """
        with contextlib.suppress(Exception):
            restrict = restrict.lower()
        if restrict not in ["allowlist", "blocklist", None]:
            await ctx.send(
                "Invalid option. Pick one of `allowlist`, `blocklist` or pass no argument to disable the hi back restrict feature."
            )
            return
        await self.config.guild(ctx.guild).restricted.set(restrict)
        if restrict:
            await ctx.send(f"Hiback restrict mode has been set to `{restrict}`.")
        else:
            await ctx.send("Hiback restrict mode has been disabled.")

    @hibackset.command(name="add")
    async def hibackset_add(self, ctx, channels: commands.Greedy[discord.TextChannel] = None):
        """
        Add channels to the hiback blocklist/allowlist.
        """
        prefixes = await self.bot.get_prefix(ctx.message.channel)
        if f"<@!{self.bot.user.id}> " in prefixes:
            prefixes.remove(f"<@!{self.bot.user.id}> ")
        sorted_prefixes = sorted(prefixes, key=len)
        if not await self.config.guild(ctx.guild).restricted():
            await ctx.send(
                f"Please choose a restriction mode using `{sorted_prefixes[0]}hibackset restrict`."
            )
            return
        if channels:
            async with self.config.guild(ctx.guild).restricted_channels() as restricted_channels:
                for channel in channels:
                    if channel.id not in restricted_channels:
                        restricted_channels.append(channel.id)

            ids = len(list(channels))
            return await ctx.send(
                f"Successfully added {ids} " f"{'channel.' if ids == 1 else 'channels.'} "
            )
        else:
            await ctx.send("`Channels` is a required argument.")
            return

    @hibackset.command(name="remove")
    async def hibackset_remove(self, ctx, channels: commands.Greedy[discord.TextChannel] = None):
        """
        Remove channels from the hiback blocklist/allowlist.
        """
        prefixes = await self.bot.get_prefix(ctx.message.channel)
        if f"<@!{self.bot.user.id}> " in prefixes:
            prefixes.remove(f"<@!{self.bot.user.id}> ")
        sorted_prefixes = sorted(prefixes, key=len)
        if not await self.config.guild(ctx.guild).restricted():
            await ctx.send(
                f"Please choose a restriction mode using `{sorted_prefixes[0]}hibackset restrict`."
            )
            return
        if channels:
            async with self.config.guild(ctx.guild).restricted_channels() as restricted_channels:
                for channel in channels:
                    if channel.id in restricted_channels:
                        restricted_channels.remove(channel.id)

            ids = len(list(channels))
            return await ctx.send(
                f"Successfully removed {ids} " f"{'channel.' if ids == 1 else 'channels.'} "
            )
        else:
            await ctx.send("`Channels` is a required argument.")
            return

    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_without_command(self, message: discord.Message):
        """
        Handle on_message.
        """
        if (
            not isinstance(message.channel, discord.TextChannel)
            or message.type != discord.MessageType.default
            or message.author.id == self.bot.user.id
            or message.author.bot
            or message.clean_content is None
            or message.author.id in await self.config.guild(message.guild).blacklisted_ids()
            or not await self.config.guild(message.guild).enabled()
        ):
            return

        if (
            await self.config.guild(message.guild).restricted() == "allowlist"
            and message.channel.id
            not in await self.config.guild(message.guild).restricted_channels()
        ):

            return

        if (
            await self.config.guild(message.guild).restricted() == "blocklist"
            and message.channel.id in await self.config.guild(message.guild).restricted_channels()
        ):

            return

        content = message.clean_content
        dad = ", im dad" if await self.config.guild(message.guild).dad() else " "
        ping = await self.config.guild(message.guild).ping()
        if search.search(content):
            try:
                back = search.search(content).group(1)
                await message.reply(
                    f"Hi {back}{dad}",
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False, roles=False, users=False
                    ),
                    mention_author=ping,
                )
            except (
                discord.HTTPException,
                discord.Forbidden,
            ):
                pass
