import discord
from discord.utils import get
from redbot.core import commands
from redbot.core.bot import Red


class Sdm(commands.Cog):
    """
    A simple dm cog, directly sends raw text to the specific user.
    """

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def sdm(self, ctx, user: discord.User, *, message: str):
        """
        Directly dm raw text to someone.
        """
        destination = get(self.bot.get_all_members(), id=user.id)
        if not destination:
            return await ctx.send(
                "Invalid ID or user not found. You can only send messages to people I share a server with."
            )
        await destination.send(message)
        await ctx.send(f"Sent message to {destination}.")
