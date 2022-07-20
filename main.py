import telethon
from telethon import TelegramClient
from telethon import events
APP_ID  = 18922496
API_HASH = "371d1dc33eccaa19bb0814a27bb98f3c"
sedthon = TelegramClient("session", APP_ID, API_HASH)
sedthon.start()

@sedthon.on(events.NewMessage(outgoing=True, pattern=".فحص"))
async def _(event):
	await event.edit("مبروك")

sedthon.run_until_disconnected()
