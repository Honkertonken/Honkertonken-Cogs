from isortformatter.isortformat import Isort

__red_end_user_data_statement__ = "This cog does not store any end user data."


async def setup(bot):
    await bot.add_cog(Isort(bot))
