import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    url="https://te.legra.ph/file/d27c1f4c3dd09d552a0da.mp4"
                )
            ]
        ]
    )
