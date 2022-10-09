import itertools

from redbot.core import commands
from redbot.core.utils.chat_formatting import humanize_list, text_to_file


class Backup(commands.Cog):
    """
    Some useful commands when backing up your bot.
    """

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self):
        """
        Nothing to delete.
        """
        return

    @commands.command()
    @commands.is_owner()
    async def backup(self, ctx):
        """
        All in one command to list all repo names, links and cogs installed
        from that repo.
        """
        downloader = ctx.bot.get_cog("Downloader")
        all_repos = list(downloader._repo_manager.repos)
        repos_list = [[f"{i.name}", i.url] for i in all_repos]
        cogs = await downloader.installed_cogs()
        for cog, r in itertools.product(cogs, repos_list):
            if cog.repo_name == list(r)[0]:
                r.append(cog.name)
        message = "\n".join(map(humanize_list, repos_list))
        await ctx.send(file=text_to_file(message, "backup.txt"))

    @commands.command()
    @commands.is_owner()
    async def cogslist(self, ctx, repo_name: str):
        """
        List the cogs installed from a specific repo.
        """
        downloader = ctx.bot.get_cog("Downloader")
        cogs = await downloader.installed_cogs()
        cogs_list = [cog.name for cog in cogs if cog.repo_name == repo_name]
        await ctx.send(
            f"Cogs installed from the repo named {repo_name} are : \n{', '.join(cogs_list)} "
        ) if cogs_list else await ctx.send(
            f"No cogs were installed from the repo named {repo_name}. Make sure to check the spelling and case."
        )

    @commands.command()
    @commands.is_owner()
    async def listrepos(self, ctx):
        """
        List all repos and their respective links.
        """
        downloader = ctx.bot.get_cog("Downloader")
        all_repos = list(downloader._repo_manager.repos)
        repos = [f"{repo.name} - {repo.url}" for repo in all_repos]
        repos_list = "\n".join(repos)
        await ctx.send(file=text_to_file(repos_list, "repos.txt"))

    @commands.command()
    @commands.is_owner()
    async def listcogs(self, ctx):
        """
        List all cogs.
        """
        cogs_list = await ctx.bot._cog_mgr.available_modules()
        await ctx.send(file=text_to_file(", ".join(cogs_list), "cogs.txt"))
