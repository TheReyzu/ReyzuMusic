#
# Copyright (C) 2022-2023 by Reyzuuu@Github, < https://github.com/Reyzuuu >.
#
# This file is part of < https://github.com/Reyzuuu/ReyzuMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Reyzuuu/ReyzuMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

import config
from strings import get_command
from ReyzuMusic import app
from ReyzuMusic.misc import SUDOERS
from ReyzuMusic.utils.database import add_off, add_on
from ReyzuMusic.utils.decorators.language import language

# Commands
VIDEOMODE_COMMAND = get_command("VIDEOMODE_COMMAND")


@app.on_message(filters.command(VIDEOMODE_COMMAND) & SUDOERS)
@language
async def videoloaymode(client, message: Message, _):
    usage = _["vidmode_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "download":
        await add_on(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_2"])
    elif state == "m3u8":
        await add_off(config.YTDOWNLOADER)
        await message.reply_text(_["vidmode_3"])
    else:
        await message.reply_text(usage)