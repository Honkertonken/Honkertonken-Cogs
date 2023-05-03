# most of the code for this cog was taken from the original pressf cog made by aikaterna.
# this is just a fork of same and has been modified for my use
# original source code for aikaterna's cog is available at https://github.com/aikaterna/aikaterna-cogs/tree/v3/pressf

import asyncio

import contextlib
import discord
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.utils.common_filters import filter_mass_mentions


class PressF(commands.Cog):
    """
    Pay some respects.
    """

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=694835810347909161, force_registration=True)
        default_guild = {
            "emoji": "🇫",
        }
        self.config.register_guild(**default_guild)

    async def set_guild_emoji(self, guild: discord.Guild, emoji):
        return await self.config.guild(guild).emoji.set(str(emoji))

    async def get_guild_emoji(self, guild: discord.Guild):
        return await self.config.guild(guild).emoji()

    @commands.command(name="pressf")
    @commands.bot_has_permissions()
    async def pressf(self, ctx, user: discord.Member):
        """
        Pay respects by pressing F.
        """
        emoji = await self.get_guild_emoji(ctx.guild)
        name = user.display_name
        class Pressf(discord.ui.View):
            @discord.ui.button(emoji="👍")
            async def Pressf(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.channel.send(f"**{interaction.user.display_name}** has paid their respects.")
                
        await ctx.send(f"Everyone, let's pay respects to **{filter_mass_mentions(name)}**! Press {emoji} to pay respects.", view=Pressf(timeout=60))
        
        #word = "person has" if amount == 1 else "people have"
        #await ctx.send(f"**{amount}** {word} paid respects to **{filter_mass_mentions(answer)}**.")

    @commands.group(name="pressfset", aliases=["pfset"], invoke_without_command=True)
    @commands.admin_or_permissions(administrator=True)
    async def pressfset(self, ctx):
        """
        Customize the pressf command.
        """
        await ctx.send_help("pressfset")

    @pressfset.command(name="emoji", usage="<emoji>")
    @commands.admin_or_permissions(administrator=True)
    async def pressfset_emoji(self, ctx, emoji: discord.Emoji):
        """
        Customize the pressf command.

        reaction emoji The bot must have access to the emoji to be used.

        """
        await self.set_guild_emoji(ctx.guild, emoji)
        await ctx.reply(f"The new pressf emoji has been set to {emoji}")
