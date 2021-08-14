from .. import loader
from asyncio import sleep
@loader.tds
class SabiMod(loader.Module):
	strings = {"name": "Sabi's"}
	@loader.owner
	async def heartscmd(self, message):
		for _ in range(10):
			for sabi in ['я', 'люблю', 'Саби', 'Я', 'люблю', 'Саби']:
				await message.edit(Sabi)
				await sleep(0.7)