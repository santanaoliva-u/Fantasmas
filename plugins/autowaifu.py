# Waifu Harem Bot <@loli_harem_bot> 792028928
# Copyright (C) 2020 Fastmore Crak
#
# Mi Pagina Web < https://fastmorecrak.github.io/Home/index.html >
# Scrip Creado con licencia abierta
#Fixes by Github/fastmorecrak | Telegram/fastmorecrak
"""
◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
✘ Comandos Disponibles -

💣autowaifu on/off 💣
    .autowaifu
    .autowaifu on
    .autowaifu off
 Basado en Hackear 💉
 las Waifus del bot = @loli_harem_bot
 📜Creado por 💻Fastmore Crak
https://fastmorecrak.github.io/Home/index.html`
◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️◾️
"""
import os
import requests
from asyncio import sleep
from bs4 import BeautifulSoup as bs
from . import *
XX = "A qt waifu appeared!"
@ultroid_cmd(pattern="autowaifu ?(.*)")
async def _(e): 
    args = e.pattern_match.group(1)
    uff = await eor(e,"`Processing...`")
    if args:
        if args == "on":
            udB.set("WAIFU","TRUE")
            return await uff.edit("📁AutoWaifu - ON   - Su Hackeador de Waifu de bot @loli_harem_bot Esta ⚪️Encendido en este grupo amo mio **Fastmore Crak** ")
        if args == "off":
            udB.set("WAIFU","FALSE")
            return await uff.edit("📁AutoWaifu - OFF -Su Hackeador de Waifu de bot @loli_harem_bot Esta ⚫️Apagado en este grupo amo mio **Fastmore Crak** ")

    waifu = udB.get("WAIFU")
    status = "ON" if waifu == "TRUE" else "OFF"
    return await uff.edit(f"AutoWaifu - {status}")

@ultroid_bot.on(events.NewMessage(incoming=True))
async def reverse(event):
    if not event.media:
        return
    if not XX in event.text:
        return
    if not event.sender_id == 792028928:
        return
    if Redis("WAIFU")!="TRUE":
        return
    dl = await autowaifu_bot.download_media(event.media, "resources/")
    file = {"encoded_image": (dl, open(dl, "rb"))}
    grs = requests.post(
        "https://www.google.com/searchbyimage/upload", files=file, allow_redirects=False
    )
    loc = grs.headers.get("Location")
    response = requests.get(
        loc,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        },
    )
    xx = bs(response.text, "html.parser")
    div = xx.find_all("div", {"class": "r5a77d"})[0]
    alls = div.find("a")
    text = alls.text
    send = await autowaifu_bot.send_message(event.chat_id, f"/protecc {text}")
    await sleep(2)
    await send.delete()
    os.remove(dl)
    
HELP.update({f"{__name__.split('.')[1]}": f"{__doc__.format(i=HNDLR)}"})