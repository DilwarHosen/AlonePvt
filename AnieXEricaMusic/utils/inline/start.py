from pyrogram.types import InlineKeyboardButton

import config
from AnieXEricaMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖽𝖽 𝖭𝗈𝗍𝗍𝗒𝗒✨",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉📚",
                callback_data="settings_back_helper"
            ),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="𝖠𝖽𝖽 𝖭𝗈𝗍𝗍𝗒𝗒✨",
                url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+",
            )
        ],
        [
            InlineKeyboardButton(
                text="𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="𝖧𝖾𝗅𝗉📚", callback_data="settings_back_helper"
            )
        ],
     ]
    return buttons
