from time import time
import aiohttp
import asyncio

from mautrix.types import TextMessageEventContent, MessageType, Format, RelatesTo, RelationType, MediaMessageEventContent
from maubot import Plugin, MessageEvent
from maubot.handlers import command

async def download_image(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

class UCLouvainRestoUBot(Plugin):
  # Highly inspired by https://github.com/maubot/echo
  @command.new("ping", help="Ping")
  async def ping_handler(self, evt: MessageEvent, message: str = "") -> None:
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
    data = await download_image("https://cdn.uclouvain.be/groups/cms-editors-resto-u/menu_51063_Restaurants_Universitaires_UCLouvain__Le_Sablon_-_Le_Galilee_-__LPzNYH61112.jpeg")
    url = await self.client.upload_media(data, mime_type="application/json")

    content = MediaMessageEventContent(
      msgtype=MessageType.IMAGE,
      url=url,
      relates_to=RelatesTo(
          rel_type=RelationType("xyz.maubot.menu"),
          event_id=evt.event_id,
      ))

    await evt.respond(content)
