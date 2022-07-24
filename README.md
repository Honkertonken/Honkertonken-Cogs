# Honkertonken-Cogs V3

[![Red-DiscordBot](https://img.shields.io/badge/Red--DiscordBot-V3-red.svg)](https://github.com/Cog-Creators/Red-DiscordBot)
[![Discord.py](https://img.shields.io/badge/Discord.py-rewrite-blue.svg)](https://github.com/Rapptz/discord.py/tree/rewrite)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Honkertonken/Cogs-V3.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Honkertonken/Cogs-V3/context:python)
[![CodeFactor](https://www.codefactor.io/repository/github/honkertonken/honkertonken-cogs/badge)](https://www.codefactor.io/repository/github/honkertonken/honkertonken-cogs)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Honkertonken/Cogs-V3/master.svg)](https://results.pre-commit.ci/latest/github/Honkertonken/Cogs-V3/master)
[![Black](https://img.shields.io/badge/Black-Passing-blue)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Autoflake](https://img.shields.io/badge/Autoflake-Passing-green)](https://github.com/myint/autoflake)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/Honkertonken/Honkertonken-Cogs/?ref=repository-badge)
[![Maintainability](https://api.codeclimate.com/v1/badges/e3da6add933361e1f23b/maintainability)](https://codeclimate.com/github/Honkertonken/Honkertonken-Cogs/maintainability)

**Disclaimer: This is an unapproved repo, meaning no one has formally reviewed this repo yet and any loss of data in your bot isn't my fault (Any loss of data is highly unlikely as I use these cogs for my bot.)**

Various fun and utility cogs for Red-DiscordBot V3.
Discord User: Honkertonken#9221(694835810347909161).

# Installation

To add cogs from this repo to your instance, do these steps:

```ini
- [p]load downloader
- [p]repo add Honkertonken-Cogs https://github.com/Honkertonken/Honkertonken-Cogs
- [p]cog install Honkertonken-Cogs <cog name>
- [p]load <cog name>

Note: [p] here refers to your prefix.
```

# About Cogs

| Cog            | Description                                                                     | Authors                 |
| -------------- | ------------------------------------------------------------------------------- | ----------------------- |
| Whoasked       | Who the hell asked? This cog/ command was inspired by KableKompany#0001.        | Honkertonken            |
| Pp             | Detect the length of someones (or your) pp. Note: 100% accurate.                | Honkertonken            |
| Pressf         | A fork of Aikaterna's pressf cog with support for custom emojis.| Aikaterna, Honkertonken |
| Sdm            | A dm to directly send raw text to the specified user, supports id and mentions. | Honkertonken            |
| Tsd            | In discord docs for Phenom4n4n's Tags/Slashtags cog.                            | Honkertonken            |
| ButtonInvite   | A highly customizable invite cog with buttons! Does not use any extra lib.      | Honkertonken            |
| BlackFormatter | Format your code with black. Supports attachments, replies & code blocks.       | Honkertonken            |
| IsortFormatter | Format your code with isort. Supports attachments, replies & code blocks.       | Honkertonken            |
| ReactionLog    | A simple reaction logger cog.                                                   | Honkertonken            |
| AmariLevel     | View your amari rank. Note: Requires you have to have a api key.                 | Honkertonken            |
| Jokes          | Get some jokes from the joke. api.                                               | Honkertonken            |
| AutoKick       | AutoKick users on join. A neat alternative to banning them.                     | Honkertonken            |
| HiBack         | Replies to "I'm X" with "Hi, X".                                                | Honkertonken            |
| AntiRickRoll | Sick and tired of getting rickrolled? This cog tries its best to avoid that. | Honkertonken |

# Contributing

- This can be done by `pip install -U black isort autoflake docformatter`
- Then run the below commands to auto format your code

```py
black .
isort . --profile black
autoflake . --in-place --remove-unused-variables --remove-all-unused-imports --recursive --remove-init-module-imports
docformatter . --in-place --recursive --blank --pre-summary-newline --make-summary-multi-line
```

# Contact

If you encounter bugs or just want to contact to me you can always shoot me a dm at Honkertonken#9221 (694835810347909161) or ping me in the `#support_othercogs` channel. . For feature requests, issues, bugs, or suggestions open a PR/issue on this repo.
