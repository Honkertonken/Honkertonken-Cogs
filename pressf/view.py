import discord
from redbot.core import commands


class PressFButton(discord.ui.Button):
    def __init__(self, emoji):
        super().__init__(emoji=emoji)

    async def callback(self, interaction: discord.Interaction):
        self.view.paid_users.append(interaction.user.id)
        self.label = len(self.view.paid_users)
        await self.view.message.edit(view=self.view)
        await interaction.response.send_message(
            f"**{interaction.user.name}** has paid their respects..",
        )


class PressFView(discord.ui.View):
    def __init__(self, timeout: 60):
        super().__init__(timeout=timeout)
        self.ctx: commands.context
        self.message: discord.Message
        self.member: discord.Member
        self.paid_users = []

    async def start(self, ctx: commands.context, member: discord.Member):
        msg = await ctx.send(
            content=f"Everyone, let's pay our respects to **{member}**!",
            view=self,
        )
        self.message = msg
        self.ctx = ctx
        self.member = member

    async def interaction_check(self, interaction: discord.Interaction):
        if interaction.user.id in self.paid_users:
            await interaction.response.send_message(
                content="You have already paid your respects!",
                ephemeral=True,
            )
            return False
        return True

    async def on_timeout(self):
        for x in self.children:
            x.disabled = True
        self.stop()
        await self.message.edit(view=self)
        if len(self.paid_users) == 0:
            return await self.ctx.channel.send(
                content=f"No one has paid respects to **{self.member}**.",
                allowed_mentions=discord.AllowedMentions.none(),
            )
        plural = "s" if len(self.paid_users) != 1 else ""
        await self.ctx.channel.send(
            content=f"**{len(self.paid_users)}** user{plural} has paid their respects to **{self.member}**.",
            allowed_mentions=discord.AllowedMentions.none(),
        )
