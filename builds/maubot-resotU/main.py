from time import time
import aiohttp
import asyncio
from bs4 import BeautifulSoup

from mautrix.types import TextMessageEventContent, MessageType, Format, RelatesTo, RelationType, MediaMessageEventContent
from maubot import Plugin, MessageEvent
from maubot.handlers import command

async def extract_picture_url(url, base_url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      if response.status != 200:
        return "Error: Unable to access the page."

      content = await response.read()
      soup = BeautifulSoup(content, 'html.parser')

      images = soup.find_all('img')

      for img in images:
        src = img.get('src')
        if src and src.startswith(base_url):
          if src.startswith('//'):
            return f"https:{src}"
          else:
            return src

      return "No image found"

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

class UCLouvainRestoUBot(Plugin):
  # Highly inspired by https://github.com/maubot/echo
  @command.new("ping", help="Ping")
  async def ping_handler(self, evt: MessageEvent, message: str = "") -> None:
    print('PING')
    diff = int(time() * 1000) - evt.timestamp
    
    content = TextMessageEventContent(
      msgtype=MessageType.NOTICE, format=Format.HTML,
      body=f"{evt.sender}: Pong! (ping took {diff} ms to arrive)",
      formatted_body=f"<a href='https://matrix.to/#/{evt.sender}'>{evt.sender}</a>: Pong! "
      f"(<a href='https://matrix.to/#/{evt.room_id}/{evt.event_id}'>ping</a> "
      f"took {diff} ms to arrive)",
      relates_to=RelatesTo(
          rel_type=RelationType("xyz.maubot.pong"),
          event_id=evt.event_id,
      ))

    await evt.respond(content)


  @command.new("menu", help="Menu")
  async def menu_handler(self, evt: MessageEvent, message: str = "") -> None:
    data = await download_image(
      await extract_picture_url(
        "https://uclouvain.be/fr/decouvrir/resto-u/le-galilee-self.html",
        "//cdn.uclouvain.be/groups/cms-editors-resto-u/menu"
      )
    )
    url = await self.client.upload_media(data, mime_type="application/json")

    content = MediaMessageEventContent(
      msgtype=MessageType.IMAGE,
      url=url,
      relates_to=RelatesTo(
          rel_type=RelationType("xyz.maubot.menu"),
          event_id=evt.event_id,
      ))

    await evt.respond(content)
