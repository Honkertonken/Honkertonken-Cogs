import discord
from redbot.core import commands
from redbot.core.bot import Red


async def embedify(self, ctx, url, img_link):
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Documentation Link", url=url))
    view.add_item(discord.ui.Button(label="Image Link", url=img_link))
    e = discord.Embed(title="Tags Documentation", type="image", url=url)
    e.set_image(url=img_link)
    await ctx.reply(embed=e, view=view, mention_author=False)


docs_link = "https://phen-cogs.readthedocs.io/en/latest/tags/"


class TagScriptDocumentation(commands.Cog):
    """
    A simple in discord documentation for Phenom4n4n's tags/slash tags cog.

    https://github.com/phenom4n4n/phen-cogs

    """

    async def red_delete_data_for_user(self, **kwargs):
        """
        Nothing to delete.
        """
        return

    def __init__(self, bot: Red):
        self.bot = bot

    @commands.group(
        name="tsd",
        aliases=["tagscriptdocumentation", "tagscriptdocs"],
        invoke_without_command=True,
        autohelp=False,
    )
    async def tsd(self, ctx):
        """
        Tag Script Documentation.
        """
        prefixes = await self.bot.get_prefix(ctx.message.channel)
        if f"<@!{self.bot.user.id}> " in prefixes:
            prefixes.remove(f"<@!{self.bot.user.id}> ")
        sorted_prefixes = sorted(prefixes, key=len)
        await ctx.send(
            f"That doesn't look like a valid tag script block. Use `{sorted_prefixes[0]}tsd list` to see a list of all tagscript blocks.",
        )

    @tsd.command(name="args", aliases=["arg"])
    async def tsd_args(self, ctx):
        """
        Tag Script Args Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#args-block",
            "https://i.imgur.com/6tdrc2D.png",
        )

    @tsd.command(name="uses", aliases=["use"])
    async def tsd_uses(self, ctx):
        """
        Tag Script Uses Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#uses-block",
            "https://i.imgur.com/NggRXeb.png",
        )

    @tsd.command(name="author")
    async def tsd_author(self, ctx):
        """
        Tag Script Author Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#author-block",
            "https://i.imgur.com/vtvF4U3.png",
        )

    @tsd.command(name="target")
    async def tsd_target(self, ctx):
        """
        Tag Script Target Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#target-block",
            "https://i.imgur.com/9Kx44NL.png",
        )

    @tsd.command(name="channel")
    async def tsd_channel(self, ctx):
        """
        Tag Script Channel Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#channel-block",
            "https://i.imgur.com/xX6vGOH.png",
        )

    @tsd.command(name="server")
    async def tsd_server(self, ctx):
        """
        Tag Script Server Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}default_variables.html#server-block",
            "https://i.imgur.com/2Oj8A49.png",
        )

    @tsd.command(name="require")
    async def tsd_require(self, ctx):
        """
        Tag Script Require Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#require-block",
            "https://i.imgur.com/FOPupFX.png",
        )

    @tsd.command(name="blacklist", aliases=["bl"])
    async def tsd_blacklist(self, ctx):
        """
        Tag Script Blacklist Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#blacklist-block",
            "https://i.imgur.com/y88vo3I.png",
        )

    @tsd.command(name="cooldown", aliases=["cd"])
    async def tsd_cooldown(self, ctx):
        """
        Tag Script Cooldown Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#cooldown-block",
            "https://i.imgur.com/PYTpqIT.png",
        )

    @tsd.command(name="embed")
    async def tsd_embed(self, ctx):
        """
        Tag Script Embed Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#embed-block",
            "https://i.imgur.com/OYYY02h.png",
        )

    @tsd.command(name="redirect")
    async def tsd_redirect(self, ctx):
        """
        Tag Script Redirect Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#redirect-block",
            "https://i.imgur.com/y168a4z.png",
        )

    @tsd.command(name="delete", aliases=["del"])
    async def tsd_delete(self, ctx):
        """
        Tag Script Delete Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#delete-block",
            "https://i.imgur.com/GrF7Q0l.png",
        )

    @tsd.command(name="react", aliases=["reactu"])
    async def tsd_react(self, ctx):
        """
        Tag Script React(u) Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#react-block",
            "https://i.imgur.com/kvtFLVg.png",
        )

    @tsd.command(name="command", aliases=["cmd"])
    async def tsd_command(self, ctx):
        """
        Tag Script Command Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#command-block",
            "https://i.imgur.com/i4VlWod.png",
        )

    @tsd.command(name="override")
    async def tsd_override(self, ctx):
        """
        Tag Script Override Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}parsing_blocks.html#override-block",
            "https://i.imgur.com/eukhyED.png",
        )

    @tsd.command(name="assignment", aliases=["var", "let"])
    async def tsd_assignment(self, ctx):
        """
        Tag Script Assignment Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#assignment-block",
            "https://i.imgur.com/xnD2WrL.png",
        )

    @tsd.command(name="random", aliases=["rand"])
    async def tsd_random(self, ctx):
        """
        Tag Script Random Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#random-block",
            "https://i.imgur.com/ATFCFee.png",
        )

    @tsd.command(name="math")
    async def tsd_math(self, ctx):
        """
        Tag Script Math Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#math-block",
            "https://i.imgur.com/iXa3wUu.png",
        )

    @tsd.command(name="range")
    async def tsd_range(self, ctx):
        """
        Tag Script Range Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#range-block",
            "https://i.imgur.com/UIriMjH.png",
        )

    @tsd.command(name="if")
    async def tsd_if(self, ctx):
        """
        Tag Script If Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#if-block",
            "https://i.imgur.com/I1ApnQZ.png",
        )

    @tsd.command(name="break")
    async def tsd_break(self, ctx):
        """
        Tag Script Break Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#break-block",
            "https://i.imgur.com/qt89NtC.png",
        )

    @tsd.command(name="all")
    async def tsd_all(self, ctx):
        """
        Tag Script All Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#all-block",
            "https://i.imgur.com/A39SCc0.png",
        )

    @tsd.command(name="any")
    async def tsd_any(self, ctx):
        """
        Tag Script Any Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#any-block",
            "https://i.imgur.com/x0rlNv9.png",
        )

    @tsd.command(name="fiftyfifty", aliases=["5050"])
    async def tsd_fiftyfifty(self, ctx):
        """
        Tag Script Fiftyfifty Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#fifty-fifty-block",
            "https://i.imgur.com/LdjKymz.png",
        )

    @tsd.command(name="stop")
    async def tsd_stop(self, ctx):
        """
        Tag Script Stop Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#stop-block",
            "https://i.imgur.com/81y8q99.png",
        )

    @tsd.command(name="replace")
    async def tsd_replace(self, ctx):
        """
        Tag Script Replace Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#replace-block",
            "https://i.imgur.com/wnXXpEf.png",
        )

    @tsd.command(name="urlencode")
    async def tsd_urlencode(self, ctx):
        """
        Tag Script Urlencode Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#urlencode-block",
            "https://i.imgur.com/jYwLzXa.png",
        )

    @tsd.command(name="strftime", aliases=["strf"])
    async def tsd_strftime(self, ctx):
        """
        Tag Script Strftime Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#strftime-block",
            "https://i.imgur.com/K8jObGF.png",
        )

    @tsd.command(name="substring")
    async def tsd_subtring(self, ctx):
        """
        Tag Script Substring Block.
        """
        await embedify(
            self,
            ctx,
            f"{docs_link}tse_blocks.html#substring-block",
            "https://i.imgur.com/fQce8aa.png",
        )

    @tsd.command(name="list", aliases=["view"])
    async def tsd_list(self, ctx):
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
            text="Note: The subcommands and block names are case sensitive (all are in lower case).",
        )

        await ctx.reply(embed=e, mention_author=False)
