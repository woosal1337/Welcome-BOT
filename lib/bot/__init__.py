from discord.ext.commands import Bot as BotBase
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from datetime import datetime
from discord.ext.commands import CommandNotFound
from lib.bot.welcome import welcomeXD

PREFIX = "+"
OWNER_IDS = [618038532665114624]


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("BOT has been CONNECTED!")

    async def on_disconnect(self):
        print("BOT has been DISCONNECTED!")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong!")

        else:
            channel = self.get_channel(757016278060761178)
            await channel.send("Dude your code freaking sucks, and error occured right here!")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(746850984701198437)
            print("BOT is ready!")

            channel = self.get_channel(757016278060761178)


            welcomeXD("WOOSAL")
            #time.sleep(5)
            # await channel.send(file=File(f"./lib/bot/Output/{i}.png"))



async def on_message(self, message):
    pass


bot = Bot()
