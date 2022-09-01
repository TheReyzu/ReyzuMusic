#
# Copyright (C) 2022-2023 by Reyzuuu@Github, < https://github.com/Reyzuuu >.
#
# This file is part of < https://github.com/Reyzuuu/ReyzuMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Reyzuuu/ReyzuMusic/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\nHERE IS YOUR STRING SESSION, COPY IT, DON'T SHARE!!\n")
    print(f"\n{ss}\n")


asyncio.run(main())
