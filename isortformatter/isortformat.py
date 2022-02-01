import isort
from redbot.core import commands

from .utils import *


class Isort(commands.Cog):
    """Run isort on code."""

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def isort(self, ctx, *, data: Optional[str]):
        """
        Format a python file with isort.
        """
        try:
            code = await get_data(ctx, data)
        except NoData:
            return

        try:
            output = isort.code(code)
            await send_output(ctx, output)

        except isort.exceptions.FileSkipped:
            await ctx.send("There was nothing to change in this code.")

        except isort.exceptions.FileSkipped:
            await ctx.send("The code is invalid check your code and try again.")
