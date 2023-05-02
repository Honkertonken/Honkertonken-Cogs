import asyncio
import datetime

import discord
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config
from redbot.core.utils.menus import start_adding_reactions
from redbot.core.utils.predicates import ReactionPredicate


class AutoKick(commands.Cog):
    """
    AutoKick users on join.
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=694835810347909161,
            force_registration=True,
        )
        default_guild = {
            "channel": None,
            "enabled": "False",
            "blacklisted_ids": [],
        }
        self.config.register_guild(**default_guild)

    @commands.group(name="autokickset", aliases=["aks"])
    @commands.bot_has_permissions(kick_members=True)
    @commands.admin_or_permissions(kick_members=True)
    @commands.guild_only()
    async def autokickset(self, ctx):
        """
        Auto Kick settings.
        """

    @autokickset.command(name="channel")
    async def autokickset_channel(self, ctx, channel: discord.TextChannel = None):
        """
        Set the auto kick log channel.

        Leave blank to disable.

        """
        if channel:
            if ctx.channel.permissions_for(channel.guild.me).send_messages is True:
                await self.config.guild(ctx.guild).channel.set(channel.id)
                await ctx.send(f"The auto kick log channel has been set to {channel.mention}")
            else:
                await ctx.send(
                    "I can't send messages in that channel. Please give me the necessary permissions and try again.",
                )
        else:
            await self.config.guild(ctx.guild).channel.clear(None)
            await ctx.send("Auto kick log channel has been cleared.")

    @autokickset.command(name="enable")
    async def autokickset_enable(self, ctx):
        """
        Enable the autokick feature.
        """
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("Auto kicking blacklisted members has been enabled for this guild.")

    @autokickset.command(name="disable")
    async def autokickset_disable(self, ctx):
        """
        Disable the autokick feature.
        """
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("Auto kicking blacklisted members has been disabled for this guild.")

    @autokickset.command(name="add", aliases=["blacklist", "bl"])
    async def autokickset_add(self, ctx, user: discord.User):
        """
        Add a certain user to get auto kicked.
        """
        async with ctx.typing():
            ids = await self.config.guild(ctx.guild).blacklisted_ids()
            ids.append(user.id)
            await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will be auto kicked on join.")

    @autokickset.command(name="remove", aliases=["unblacklist", "unbl"])
    async def autokickset_remove(self, ctx, user: discord.User):
        """
        Remove a certain user from getting auto kicked.
        """
        async with ctx.typing():
            ids = await self.config.guild(ctx.guild).blacklisted_ids()
            ids.remove(user.id)
            await self.config.guild(ctx.guild).blacklisted_ids.set(ids)
        await ctx.send(f"{user} will not be auto kicked on join.")

    @autokickset.command(name="settings", aliases=["showsettings"])
    async def autokickset_settings(self, ctx):
        """
        Check your autokick settings.
        """
        channel = await self.config.guild(ctx.guild).channel()
        channel_mention = f"<#{channel}>" if channel else "Not Set"
        enabled = await self.config.guild(ctx.guild).enabled()
        e = discord.Embed(title="Auto kick Settings", color=await ctx.embed_color())
        e.add_field(name="Channel", value=channel_mention, inline=True)
        e.add_field(name="Enabled", value=enabled, inline=True)
        e.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_as(format="png"))
        await ctx.send(embed=e)

    @autokickset.command(name="clear", aliases=["nuke"], hidden=True)
    async def autokickset_clear(self, ctx):
        """
        Clear the autokick list.
        """
        confirmation_msg = await ctx.send("Are you sure you want to clear the auto kick list. ?")
        pred = ReactionPredicate.yes_or_no(confirmation_msg, ctx.author)
        start_adding_reactions(confirmation_msg, ReactionPredicate.YES_OR_NO_EMOJIS)
        try:
            await self.bot.wait_for("reaction_add", check=pred, timeout=60)
        except asyncio.TimeoutError:
            return await ctx.send("You took too long to respond. Cancelling.")
        if not pred.result:
            return await ctx.send("Alright I will not clear the auto kick list.")
        async with ctx.typing():
            await self.config.guild(ctx.guild).blacklisted_ids.clear()
        await ctx.send("Auto kick list has been cleared.")

    @commands.bot_has_permissions(kick_members=True)
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if await self.config.guild(member.guild).enabled():
            logs_channel = await self.config.guild(member.guild).channel()
            logs = self.bot.get_channel(logs_channel)
            e = discord.Embed(
                title=f"{member} just got auto kicked.",
                color=discord.Color.red(),
            )
            e.set_footer(text=f"{member.guild.name}", icon_url=f"{member.guild.icon}")
            e.set_author(name=f"{member.display_name}", icon_url=f"{member.display_avatar.url}")
            e.timestamp = datetime.datetime.now(datetime.timezone.utc)
            if member.id in await self.config.guild(member.guild).blacklisted_ids():
                try:
                    await member.guild.kick(member, reason="AutoKicked.")
                    await logs.send(embed=e)
                except discord.Forbidden:
                    if logs:
                        await logs.send(
                            f"{member} could not be auto kicked. Please make sure i have necessary permissions and try again.",
                        )
