import asyncio

import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.common_filters import filter_mass_mentions


class PressF(commands.Cog):
    """Pay some respects."""

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    def __init__(self, bot: Red):
        self.bot = bot
        self.channels = {}
        self.config = Config.get_conf(self, identifier=420, force_registration=True)
        default_guild = {
            "emoji": "🇫",
        }
        self.config.register_guild(**default_guild)

    async def set_guild_emoji(self, guild: discord.Guild, emoji):
        return await self.config.guild(guild).emoji.set(str(emoji))

    async def get_guild_emoji(self, guild: discord.Guild):
        return await self.config.guild(guild).emoji()

    @commands.command()
    @commands.bot_has_permissions(add_reactions=True)
    async def pressf(self, ctx, *, user: discord.User = None):
        """Pay respects by pressing F"""
        emoji = await self.get_guild_emoji(ctx.guild)
        if str(ctx.channel.id) in self.channels:
            return await ctx.send(
                "Oops! I'm still paying respects in this channel, you'll have to wait until I'm done."
            )
        if user:
            answer = user.display_name
        else:
            await ctx.send("What do you want to pay respects to?")

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                pressf = await ctx.bot.wait_for("message", timeout=120.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.send("You took too long to reply.")

            answer = pressf.content[:1900]

        message = await ctx.send(
            f"Everyone, let's pay respects to **{filter_mass_mentions(answer)}**! Press {emoji} to pay respects."
        )
        await message.add_reaction(emoji)
        self.channels[str(ctx.channel.id)] = {"msg_id": message.id, "reacted": []}
        await asyncio.sleep(60)
        try:
            await message.delete()
        except (discord.errors.NotFound, discord.errors.Forbidden):
            pass
        amount = len(self.channels[str(ctx.channel.id)]["reacted"])
        word = "person has" if amount == 1 else "people have"
        await ctx.send(f"**{amount}** {word} paid respects to **{filter_mass_mentions(answer)}**.")
        del self.channels[str(ctx.channel.id)]

    @commands.Cog.listener()
    async def on_reaction_add(
        self,
        reaction,
        user,
    ):
        if str(reaction.message.channel.id) not in self.channels:
            return
        if self.channels[str(reaction.message.channel.id)]["msg_id"] != reaction.message.id:
            return
        if user.id == self.bot.user.id:
            return
        if user.id not in self.channels[str(reaction.message.channel.id)][
            "reacted"
        ] and str(reaction.emoji) == await self.get_guild_emoji(
            reaction.message.guild
        ):
            await reaction.message.channel.send(f"**{user.name}** has paid their respects.")
            self.channels[str(reaction.message.channel.id)]["reacted"].append(user.id)

    @commands.group(name="pressfset", aliases=["pfset"], invoke_without_command=True)
    @commands.admin_or_permissions(administrator=True)
    async def pressfset(self, ctx):
        """
        Customize the pressf command.
        """
        await ctx.send_help("pressfset")

    @pressfset.command(name="emoji", usage="<emoji>")
    @commands.admin_or_permissions(administrator=True)
    async def emoji(self, ctx, emoji: discord.Emoji):
        """Customize the pressf command. reaction emoji
        The bot must have access to the emoji to be used.
        """
        await self.set_guild_emoji(ctx.guild, emoji)
        await ctx.reply(f"The new pressf emoji has been set to {emoji}")
