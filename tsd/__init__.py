from .TagScriptDocumentation import TagScriptDocumentation

__red_end_user_data_statement__ = "This cog does not store any end user data."


async def setup(bot):
    bot.add_cog(TagScriptDocumentation(bot))
