import discord
from redbot.core import commands
from redbot.core.config import Config


class ReactionLog(commands.Cog):
    """
    A reaction tracker cog.
    """

    def __init__(self, bot) -> None:
        self.bot = bot
        self.config = Config.get_conf(
            self,
            identifier=694835810347909161,
            force_registration=True,
        )
        default_guild = {
            "enabled": False,
            "channel": None,
            "reaction_add_enabled": "",
            "reaction_remove_enabled": "",
        }
        self.config.register_guild(**default_guild)

    @commands.group(name="reactionlogset", aliases=["rlogset"])
    @commands.admin()
    @commands.guild_only()
    async def reactionlogset(self, ctx):
        """
        Reaction Log settings.
        """
        
    @reactionlogset.command(name="enable")
    async def reactionlogset_enable(self, ctx):
        """
        Enable the reaction log feature.
        """
        await self.config.guild(ctx.guild).enabled.set(True)
        await ctx.send("Reaction logging has been enabled for this guild.")

    @reactionlogset.command(name="disable")
    async def reactionlogset_disable(self, ctx):
        """
        Disable the reaction log feature.
        """
        await self.config.guild(ctx.guild).enabled.set(False)
        await ctx.send("Reaction logging  members has been disabled for this guild.")

    @reactionlogset.command(name="channel")
    async def reactionlogset_channel(self, ctx, channel: discord.TextChannel):
        """
        Set the reaction log channel.
        """
        if ctx.channel.permissions_for(channel.guild.me).send_messages is True:
            await self.config.guild(ctx.guild).channel.set(channel.id)
            await ctx.send(f"The reaction log channel has been set to {channel.mention}")
        else:
            await ctx.send(
                "I can't send messages in that channel. Please give me the necessary permissions and try again.",
            )

    @reactionlogset.command(name="reactionadd", aliases=["ra"])
    async def reactionlogset_reactionadd(self, ctx, enable_or_disable: bool):
        """
        Enable/disable logs for reactions added.
        """
        async with ctx.typing():
            await self.config.guild(ctx.guild).reaction_add_enabled.set(enable_or_disable)
        if enable_or_disable:
            await ctx.send("Reactions logs for reactions added has been enabled.")
        else:
            await ctx.send("Reactions logs for reactions added has been disabled.")

    @reactionlogset.command(name="reactionremove", aliases=["rr"])
    async def reactionlogset_reactionremove(self, ctx, enable_or_disable: bool):
        """
        Enable/disable logs for reactions removed.
        """
        async with ctx.typing():
            await self.config.guild(ctx.guild).reaction_remove_enabled.set(enable_or_disable)
        if enable_or_disable:
            await ctx.send("Reactions logs for reactions removed has been enabled.")
        else:
            await ctx.send("Reactions logs for reactions removed has been disabled.")

    @reactionlogset.command(name="settings", aliases=["showsettings"])
    async def reactionlogset_settings(self, ctx):
        """
        Check your reactionlog settings.
        """
        enabled = await self.config.guild(ctx.guild).enabled()
        channel = await self.config.guild(ctx.guild).channel()
        channel_mention = f"<#{channel}>" if channel else "Not Set"
        reaction_add = await self.config.guild(ctx.guild).reaction_add_enabled()
        reaction_remove = await self.config.guild(ctx.guild).reaction_remove_enabled()
        e = discord.Embed(title="Reaction Log Settings", color=await ctx.embed_color())
        e.add_field(name="Enabled", value=enabled, inline=True)
        e.add_field(name="Channel", value=channel_mention, inline=True)
        e.add_field(name="Log On Reaction Add", value=reaction_add, inline=True)
        e.add_field(name="Log On Reaction Remove", value=reaction_remove, inline=True)
        e.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.static_replace(format="png")) 
        await ctx.send(embed=e)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, member: discord.Member):
        logs_channel = await self.config.guild(member.guild).channel()
        logs = self.bot.get_channel(logs_channel)
        if await self.config.guild(member.guild).reaction_add_enabled() & await self.config.guild(member.guild).enabled():
            embed = discord.Embed(
                title=f"{member} added a reaction.",
                color=discord.Color.green(),
            )
            embed.set_footer(text=f"{member} ({member.id})", icon_url=member.display_avatar.url)
            if isinstance(reaction.emoji, (discord.Emoji, discord.PartialEmoji)):
                embed.set_thumbnail(url=reaction.emoji.url)
            embed.add_field(
                name="Reaction:",
                value=f"{reaction}",
                inline=False,
            )
            embed.add_field(
                name="Message Link:",
                value=f"[Click here]({reaction.message.jump_url})",
                inline=False,
            )
            await logs.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction: discord.Reaction, member: discord.Member):
        logs_channel = await self.config.guild(member.guild).channel()
        logs = self.bot.get_channel(logs_channel)
        if await self.config.guild(member.guild).reaction_remove_enabled() & await self.config.guild(member.guild).enabled():
            embed = discord.Embed(
                title=f"{member} removed a reaction.",
                color=discord.Color.red(),
            )
            embed.set_footer(text=f"{member} ({member.id})", icon_url=member.display_avatar.url)
            if isinstance(reaction.emoji, (discord.Emoji, discord.PartialEmoji)):
                embed.set_thumbnail(url=reaction.emoji.url)
            embed.add_field(
                name="Reaction:",
                value=f"{reaction}",
                inline=False,
            )
            embed.add_field(
                name="Message Link:",
                value=f"[Click here]({reaction.message.jump_url})",
                inline=False,
            )
            await logs.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_clear(self, message: discord.Message, reaction: discord.Reaction):
        logs_channel = await self.config.guild(message.guild).channel()
        logs = self.bot.get_channel(logs_channel)
        if await self.config.guild(message.guild).reaction_remove_enabled() & await self.config.guild(message.guild).enabled():
            emojis = []
            for i in reaction:
                emojis.append(i.emoji)
                reactions = ", ".join(map(str, emojis))
            embed = discord.Embed(
                title="Multiple reactions were removed.",
                color=discord.Color.red(),
            )
            if isinstance(reaction.emoji, (discord.Emoji, discord.PartialEmoji)):
                embed.set_thumbnail(url=reaction.emoji.url)
            embed.add_field(
                name="Reactions:",
                value=f"{str(reactions).strip('[]')}",
                inline=False,
            )
            embed.add_field(
                name="Message Link:",
                value=f"[Click here]({message.jump_url})",
                inline=False,
            )
            await logs.send(embed=embed)
