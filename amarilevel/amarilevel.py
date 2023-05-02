import discord
from amari import AmariClient, InvalidToken, NotFound
from redbot.core import commands
from redbot.core.bot import Red


class AmariLevel(commands.Cog):
    """
    View your amari rank.
    """

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.guild_only()
    @commands.command(name="amari")
    async def amari(self, ctx, *member: discord.Member):
        """
        View your amari rank.
        """
        token = (await self.bot.get_shared_api_tokens("amari")).get("auth")
        if token:
            if not member:
                member = ctx.author
            if member.bot:
                return await ctx.send("Bots dont have any amari xp.")
            if ctx.guild.get_member(339254240012664832):
                bot_info = await self.bot.application_info()
                amari = AmariClient(token)
                try:
                    lb = await amari.fetch_full_leaderboard(ctx.guild.id)
                    user = lb.get_user(member.id)
                    e = discord.Embed(
                        title=f"{member.name}'s Amari Rank",
                        type="rich",
                        color=await ctx.embed_color(),
                        description=f"**Rank : {user.position+1}\nLevel : {user.level}\nXp : {user.exp}\n Weekly Xp : {user.weeklyexp}**",
                    )
                    e.set_author(
                        name=f"{member.display_name}",
                        icon_url=f"{member.display_avatar.url}",
                    )
                    e.set_footer(text=f"{ctx.guild.name}", icon_url=f"{ctx.guild.icon}")
                    await ctx.send(embed=e)
                except NotFound:
                    await ctx.send(f"{member} has no amari data in {ctx.guild}.")
                except InvalidToken:
                    await ctx.send(
                        f"The Amari token is invalid, please report this to {bot_info.owner}.",
                    )
                await amari.close()
            else:
                await ctx.send(f"You dont have Amaribot in {ctx.guild.name}.")
        else:
            await ctx.send("Please set an amari api token first.")
