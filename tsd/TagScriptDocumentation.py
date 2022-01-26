import discord
from redbot.core import commands


class TagScriptDocumentation(commands.Cog):
    """
    A simple in discord documentation for Phenom4n4n's tags cog.
    https://github.com/phenom4n4n/phen-cogs
    """

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="tsd",
        aliases=["tagscriptdocumentation", "tagscriptdocs"],
        invoke_without_command=True,
        autohelp=False,
    )
    async def tsd(self, ctx):
        """
        Tag Script Documentation
        """
        await ctx.send(
            "That doesn't look like a valid block use `[p]tsd list` to see a list of all tagscript blocks."
        )

    @tsd.command(name="args", aliases=["arg"])
    async def args(self, ctx):
        """
        Tag Script Args Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#args-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/6tdrc2D.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="uses", aliases=["use"])
    async def uses(self, ctx):
        """
        Tag Script Uses Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#uses-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/NggRXeb.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="author")
    async def author(self, ctx):
        """
        Tag Script Author Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#author-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/vtvF4U3.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="target")
    async def target(self, ctx):
        """
        Tag Script Target Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#target-block}",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/9Kx44NL.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="channel")
    async def channel(self, ctx):
        """
        Tag Script Channel Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#channel-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/xX6vGOH.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="server")
    async def server(self, ctx):
        """
        Tag Script Server Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/default_variables.html#server-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/2Oj8A49.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="require")
    async def require(self, ctx):
        """
        Tag Script Require Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#require-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/FOPupFX.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="blacklist", aliases=["bl"])
    async def blacklist(self, ctx):
        """
        Tag Script Blacklist Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#blacklist-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/y88vo3I.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="cooldown", aliases=["cd"])
    async def cooldown(self, ctx):
        """
        Tag Script Cooldown Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#cooldown-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/PYTpqIT.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="embed")
    async def embed(self, ctx):
        """
        Tag Script Embed Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#embed-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/OYYY02h.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="redirect")
    async def redirect(self, ctx):
        """
        Tag Script Redirect Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#redirect-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/y168a4z.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="delete", aliases=["del"])
    async def delete(self, ctx):
        """
        Tag Script Delete Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#delete-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/GrF7Q0l.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="react", aliases=["reactu"])
    async def react(self, ctx):
        """
        Tag Script React(u) Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#react-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/kvtFLVg.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="command", aliases=["cmd"])
    async def command(self, ctx):
        """
        Tag Script Command Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#command-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/i4VlWod.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="override")
    async def override(self, ctx):
        """
        Tag Script Override Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/parsing_blocks.html#override-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/eukhyED.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="assignment", aliases=["var", "let"])
    async def assignment(self, ctx):
        """
        Tag Script Assignment Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#assignment-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/xnD2WrL.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="random", aliases=["rand"])
    async def random(self, ctx):
        """
        Tag Script Random Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#random-block}",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/ATFCFee.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="math")
    async def math(self, ctx):
        """
        Tag Script Math Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#math-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/iXa3wUu.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="range")
    async def range(self, ctx):
        """
        Tag Script Range Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#range-block}",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/UIriMjH.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="if")
    async def _if(self, ctx):
        """
        Tag Script If Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#if-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/I1ApnQZ.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="break")
    async def _break(self, ctx):
        """
        Tag Script Break Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#break-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/qt89NtC.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="all")
    async def all(self, ctx):
        """
        Tag Script All Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#all-block}",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/A39SCc0.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="any")
    async def any(self, ctx):
        """
        Tag Script Any Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#any-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/x0rlNv9.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="fiftyfifty", aliases=["5050"])
    async def fiftyfifty(self, ctx):
        """
        Tag Script Fiftyfifty Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#fifty-fifty-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/LdjKymz.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="stop")
    async def stop(self, ctx):
        """
        Tag Script Stop Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#stop-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/81y8q99.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="replace")
    async def replace(self, ctx):
        """
        Tag Script Replace Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#replace-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/wnXXpEf.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="urlencode")
    async def urlencode(self, ctx):
        """
        Tag Script Urlencode Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#urlencode-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/jYwLzXa.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="strftime", aliases=["strf"])
    async def strftime(self, ctx):
        """
        Tag Script Strftime Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#strftime-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/K8jObGF.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="substring")
    async def subtring(self, ctx):
        """
        Tag Script Substring Block.
        """
        e = discord.Embed(
            title="Tags Documentation",
            url="https://phen-cogs.readthedocs.io/en/latest/tags/tse_blocks.html#substring-block",
            type="image",
        )
        e.set_image(url="https://i.imgur.com/fQce8aa.png")
        await ctx.reply(embed=e, mention_author=False)

    @tsd.command(name="list", aliases=["view"])
    async def list(self, ctx):
        """
        All Tag Script Blocks.
        """
        e = discord.Embed(title="List of all Tagscript blocks.")
        e.add_field(
            name="⠀",
            value="\n1. Args \n 2. Uses \n 3. Author \n 4. Target \n 5. Channel \n 6. Server \n 7. Require \n 8. Blacklist \n 9. Cooldown \n 10. Embed \n 11. Redirect \n 12. Delete\n 13. React(u) \n 14. Command \n 15. Override \n 16. Assignment \n 17. Random \n 18. Math \n 19. Range \n 20. If \n 21. Break \n 22. All \n 23. Any \n 24. Fifty-fifty \n 25. Stop \n 26. Replace \n 27. URLEncode \n 28. Strftime \n 29. SubString",
            inline=False,
        )
        e.set_footer(
            text="Note: The subcommands and block names are case sensitive (all are in lower case)."
        )

        await ctx.reply(embed=e, mention_author=False)
