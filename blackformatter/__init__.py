from blackformatter.blackformat import Black

__red_end_user_data_statement__ = "This cog does not store any end user data."


def setup(bot):
    await bot.add_cog(Black(bot))
