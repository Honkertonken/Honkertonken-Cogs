from jokes.jokes import Jokes

__red_end_user_data_statement__ = "This cog does not store any end user data."


def setup(bot):
    bot.add_cog(Jokes(bot))
