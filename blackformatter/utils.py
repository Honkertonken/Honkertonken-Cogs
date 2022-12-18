from typing import Optional

import discord
from redbot.core import commands
from redbot.core.utils.chat_formatting import box, text_to_file

from .errors import AttachmentInvalid, AttachmentPermsError, NoData


# thanks vexed
def cleanup(py: str) -> str:
    """
    Remove codeblocks, if present.
    """
    if py.startswith("```") and py.endswith("```"):

        py = py.strip("```py")
        return py.strip("```")

    return py.strip("`") if py.startswith("`") and py.endswith("`") else py


async def get_data(ctx: commands.Context, data: Optional[str]) -> str:
    if data is not None:
        return cleanup(data)

    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]

    elif ctx.message.reference:
        if ctx.message.reference.cached_message.attachments:
            attachment = ctx.message.reference.cached_message.attachments[0]

        else:
            content = ctx.message.reference.cached_message.content
            substrings = content.split("```")
            if len(substrings) == 3:
                return cleanup(substrings[1].lstrip("py").lstrip("py"))

            await ctx.send_help()
            raise NoData
    else:
        await ctx.send_help()
        raise NoData

    filename = attachment.filename
    if not (filename.endswith(".py") or filename.endswith(".txt")):
        await ctx.send("The file attached must be `.txt` or `.py`,")
        raise AttachmentInvalid

    try:
        att_bytes = await attachment.read()
        if not isinstance(att_bytes, bytes):
            await ctx.send("Something's wrong with that attachment.")
            raise AttachmentInvalid
        return att_bytes.decode()
    except discord.HTTPException:
        await ctx.send("I can't access that attachment.")
        raise AttachmentPermsError


async def send_output(ctx: commands.Context, text: str) -> None:
    """
    Send output as a codeblock or file, depending on file limits.

    Handles no attachment perm.

    """

    if (len(text)) < 1980 and text.count("\n") < 20:
        await ctx.send(box(text, lang="py"))
    else:
        if ctx.guild and not ctx.channel.permissions_for(ctx.me).attach_files:
            return await ctx.send(
                "The output is big and I don't have permission to attach files. "
                "You could try again in my DMs."
            )

        file = text_to_file(text, "black.py")
        await ctx.send("The output is big, so I've attached it as a file.", file=file)
