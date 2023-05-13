import contextlib
import re

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

search = re.compile(
    r"(i[',\s]*a?m|i.m)[.,\s]*\s*(.*)",
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
            "bot": False,
            "ping": True,
            "blacklisted_users": [],
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
        await ctx.send("Hi back has been enabled for this guild.")

    @hibackset.command(name="disable")
    async def hibackset_disable(self, ctx):
        """
        Disable the hi back feature.
        """
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("Hi back has been disabled for this guild.")

    @hibackset.command(name="dad")
    async def hibackset_dad(self, ctx, true_or_false: bool):
        """
        Add a `im dad` to the hi back messages.
        """
        if true_or_false:
            if not await self.config.guild(ctx.guild).bot():
                await self.config.guild(ctx.guild).dad.set(true_or_false)
                await ctx.send("`Im dad` shall now be added to hi back messages.")
            else:
                await ctx.send("Please disable the `hiback bot` option first.")
        else:
            await self.config.guild(ctx.guild).dad.set(true_or_false)
            await ctx.send("`Im dad` shall not be added to hi back messages.")

    @hibackset.command(name="bot")
    async def hibackset_bot(self, ctx, true_or_false: bool):
        """
        Add a `im {bot_name}` to the hi back messages.
        """
        if true_or_false:
            if not await self.config.guild(ctx.guild).dad():
                await self.config.guild(ctx.guild).bot.set(true_or_false)
                await ctx.send(
                    f"`Im {ctx.bot.user.display_name}` shall now be added to hi back messages.",
                )
            else:
                await ctx.send("Please disable the `hiback dad` option first.")
        else:
            await self.config.guild(ctx.guild).bot.set(true_or_false)
            await ctx.send(
                f"`Im {ctx.bot.user.display_name}` shall not be added to hi back messages.",
            )

    @hibackset.command(name="ping")
    async def hibackset_ping(self, ctx, true_or_false: bool):
        """
        Ping users on the hi back messages.
        """
        await self.config.guild(ctx.guild).ping.set(true_or_false)
        if true_or_false:
            await ctx.send("Users will be pinged on hi back messages.")
        else:
            await ctx.send("Users will not be pinged on hi back messages.")

    @hibackset.command(name="ignore", aliases=["blacklist", "bl"])
    async def hibackset_ignore(self, ctx, users: commands.Greedy[discord.User] = None):
        """
        Ignore a user from the hi back messages.
        """
        if users:
            async with self.config.guild(ctx.guild).blacklisted_users() as blacklisted_users:
                for user in users:
                    if user.id not in blacklisted_users:
                        blacklisted_users.append(user.id)
            ids = len(list(users))
            await ctx.send(
                f"Successfully added {ids} "
                f"{'user' if ids == 1 else 'users'} "
                f"to the ignore list.",
            )
            return
        await ctx.send("`Users` is a required argument.")
        return

    @hibackset.command(name="unignore", aliases=["unblacklist", "unbl"])
    async def hibackset_unignore(self, ctx, users: commands.Greedy[discord.User] = None):
        """
        Unignore a user from the hi back messages.
        """
        if users:
            async with self.config.guild(ctx.guild).blacklisted_users() as blacklisted_users:
                for user in users:
                    if user.id in blacklisted_users:
                        blacklisted_users.remove(user.id)
            ids = len(list(users))
            await ctx.send(
                f"Successfully removed {ids} "
                f"{'user' if ids == 1 else 'users'} "
                f"from the ignore list.",
            )
            return
        await ctx.send("`Users` is a required argument.")
        return

    @hibackset.command(name="restrict")
    async def hibackset_restrict(self, ctx, restrict: str = None):
        """
        Restrict the hiback feature, supports blocklist and allowlist.
        """
        with contextlib.suppress(Exception):
            restrict = restrict.lower()
        if restrict not in ["allowlist", "blocklist", None]:
            await ctx.send(
                "Invalid option. Pick one of `allowlist`, `blocklist` or pass no argument to disable the hi back restrict feature.",
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
                f"Please choose a restriction mode using `{sorted_prefixes[0]}hibackset restrict`.",
            )
            return
        if channels:
            async with self.config.guild(ctx.guild).restricted_channels() as restricted_channels:
                for channel in channels:
                    if channel.id not in restricted_channels:
                        restricted_channels.append(channel.id)

            ids = len(list(channels))
            return await ctx.send(
                f"Successfully added {ids} " f"{'channel.' if ids == 1 else 'channels.'} ",
            )
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
                f"Please choose a restriction mode using `{sorted_prefixes[0]}hibackset restrict`.",
            )
            return
        if channels:
            async with self.config.guild(ctx.guild).restricted_channels() as restricted_channels:
                for channel in channels:
                    if channel.id in restricted_channels:
                        restricted_channels.remove(channel.id)
            ids = len(list(channels))
            return await ctx.send(
                f"Successfully removed {ids} " f"{'channel.' if ids == 1 else 'channels.'} ",
            )
        await ctx.send("`Channels` is a required argument.")
        return

    @hibackset.command(name="clean")
    async def hibackset_clean(self, ctx):
        """
        Clean deleted channels from restricted channels list.
        """
        clean = []
        restricted_channels = await self.config.guild(ctx.guild).restricted_channels()
        for i, channel in enumerate(restricted_channels):
            exists = ctx.guild.get_channel(channel)
            if not exists:
                clean.append(i)

        for i in reversed(clean):
            del restricted_channels[i]

        await self.config.guild(ctx.guild).restricted_channels.set(restricted_channels)
        return await ctx.send(
            "Deleted channels have been removed from the restricted channels list.",
        )

    @hibackset.command(name="settings", aliases=["showsettings"])
    async def hibackset_settings(self, ctx):
        """
        Check your hi back settings.
        """
        enabled = await self.config.guild(ctx.guild).enabled()
        ping = await self.config.guild(ctx.guild).ping()
        dad = await self.config.guild(ctx.guild).dad()
        bot = await self.config.guild(ctx.guild).bot()
        restricted = await self.config.guild(ctx.guild).restricted()
        restricted_channels = await self.config.guild(ctx.guild).restricted_channels()
        blacklisted_users = await self.config.guild(ctx.guild).blacklisted_users()
        channels = ""
        users = ""
        for channel in restricted_channels:
            channel_name = f"<#{channel}>"
            channels += f"{channel_name} "

        for user in blacklisted_users:
            user_name = f"<@{user}>"
            users += f"{user_name} "

        e = discord.Embed(title="Hi Back Settings", color=await ctx.embed_color())
        e.add_field(name="Enabled", value=enabled)
        e.add_field(name="Dad", value=dad)
        e.add_field(name="Bot", value=bot)
        e.add_field(name="Ping", value=ping)
        e.add_field(name="Restriction Mode", value=restricted)
        e.add_field(name="Restricted Channels", value=channels or "None")
        e.add_field(name="Blacklisted Users", value=users or "None")
        e.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_as(format="png"))
        await ctx.send(embed=e)

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
            or message.author.id in await self.config.guild(message.guild).blacklisted_users()
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
        dad = ", im dad" if await self.config.guild(message.guild).dad() else ""
        bot = (
            f", im {self.bot.user.display_name}"
            if await self.config.guild(message.guild).bot()
            else ""
        )
        ping = await self.config.guild(message.guild).ping()
        if search.search(content):
            try:
                back = search.search(content).group(2)
                await message.reply(
                    f"Hi {back}{dad}{bot}",
                    allowed_mentions=discord.AllowedMentions(
                        everyone=False,
                        roles=False,
                        users=False,
                    ),
                    mention_author=ping,
                )
            except (
                discord.HTTPException,
                discord.Forbidden,
            ):
                pass
