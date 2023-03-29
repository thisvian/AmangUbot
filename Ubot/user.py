
from ast import parse
from pyrogram import (
    Client,
    __version__,
    enums
)
from .logging import LOGGER
from config import *


class User1(Client):
    def __init__(self):
        super().__init__(
            name="bot1",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION1,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION1
        else None
        self.LOGGER = LOGGER

class User2(Client):
    def __init__(self):
        super().__init__(
            name="bot2",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION2,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION2
        else None
        self.LOGGER = LOGGER

class User3(Client):
    def __init__(self):
        super().__init__(
            name="bot3",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION3,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION3
        else None
        self.LOGGER = LOGGER

class User4(Client):
    def __init__(self):
        super().__init__(
            name="bot4",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION4,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION4
        else None
        self.LOGGER = LOGGER

class User5(Client):
    def __init__(self):
        super().__init__(
            name="bot5",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION5,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION5
        else None
        self.LOGGER = LOGGER

class User6(Client):
    def __init__(self):
        super().__init__(
            name="bot6",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION6,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION6
        else None
        self.LOGGER = LOGGER

class User7(Client):
    def __init__(self):
        super().__init__(
            name="bot7",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION7,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION7
        else None
        self.LOGGER = LOGGER

class User8(Client):
    def __init__(self):
        super().__init__(
            name="bot8",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION8,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION8
        else None
        self.LOGGER = LOGGER

class User9(Client):
    def __init__(self):
        super().__init__(
            name="bot9",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION9,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION9
        else None
        self.LOGGER = LOGGER

class User10(Client):
    def __init__(self):
        super().__init__(
            name="bot10",
            api_hash=API_HASH,
            api_id=API_ID,
            workers=BOT_WORKERS,
            session_string=SESSION10,
            plugins=dict(root="Ubot/modules"),
            in_memory=True,
        )
        if SESSION10
        else None
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = self.me
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")