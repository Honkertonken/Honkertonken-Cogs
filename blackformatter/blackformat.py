from typing import Optional

import black
from redbot.core import commands

from .errors import NoData
from .utils import get_data, send_output


class Black(commands.Cog):
    """Run black on code."""

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @commands.command()
    async def black(self, ctx, *, data: Optional[str]):
        """
        Format your python code with black.
        """
        try:
            code = await get_data(ctx, data)
        except NoData:
            return

        try:
            output = black.format_file_contents(code, fast=True, mode=black.Mode())
            await send_output(ctx, output)

        except black.NothingChanged:
            await ctx.send("There was nothing to change in this code.")

        except black.parsing.InvalidInput:
            await ctx.send("The code is invalid check your code and try again.")
