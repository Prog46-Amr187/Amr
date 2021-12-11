from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Yukki import BOT_USERNAME


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الاعدادات", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الاعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 المساعده", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الاعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📡 قناه التحديثات", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 الاعدادات", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📡 قناه التحديثات", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨 المساعده", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ اضفني في مجموعتك",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ اضفني في مجموعتك",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨 المساعده", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ اضفني في مجموعتك",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📡 قناه التحديثات", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 قائمه اوامر المساعده", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ اضفني في مجموعتك",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📡 قناه التحديثات", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨 المساعده", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **هذا هو {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 جودة الصوت", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 حجم الصوت", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 المستخدين المعتمدين", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 لوحة القيادة", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ أغلاق", callback_data="close"),
            InlineKeyboardButton(text="🔙 عوده للخلف", callback_data="okaybhai"),
        ],
    ]
    return f"🔧 اعدادات بوت  **{MUSIC_BOT_NAME} .**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 إعادة تعيين حجم الصوت 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 خفض الصوت", callback_data="LV"),
            InlineKeyboardButton(text="🔉 صوت متوسط", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 رفع الصوت", callback_data="HV"),
            InlineKeyboardButton(text="🔈 تضخيم", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 حجم مخصص 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 عوده للخلف", callback_data="settingm")],
    ]
    return f"🔧 اعدادات بوت  **{MUSIC_BOT_NAME} .**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 حجم مخصص 🔼", callback_data="AV")],
    ]
    return f"🔧 اعدادات بوت  **{MUSIC_BOT_NAME} .**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 الجميع", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 الادمن",  callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 قائمه المستخدين المعتمدين", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 عوده للخلف", callback_data="settingm")],
    ]
    return f"🔧 اعدادات بوت  **{MUSIC_BOT_NAME} .**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 عوده للخلف", callback_data="settingm")],
    ]
    return f"🔧 اعدادات بوت  **{MUSIC_BOT_NAME} .**", buttons
