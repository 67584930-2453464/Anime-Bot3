from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "7929209064:AAGxPEAYeo-AXKQ3oJbTOR-AMjC6VMReJpw"
CHANNEL_ID = "@Anime_lar_New"
OWNER_ID = 6627829267  # <-- O'zingizning Telegram ID'ingiz

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# === PHOTO file_id olish uchun ===
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo_id(message: types.Message):
    await message.reply(f"🖼 Rasm file_id:\n<code>{message.photo[-1].file_id}</code>", parse_mode="HTML")


# === POST yuborish komandasi ===
@dp.message_handler(commands=["sendpost"])
async def send_post(message: types.Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("⛔ Sizda ruxsat yo‘q.")
        return

    # Rasm file_id
    photo_file_id = "AgACAgIAAxkBAAMfaP9cDP2hotW9Saz2-2geOZMXyPQAAo3MMRu22kBLLucE295OF4EBAAMCAAN4AAM2BA"

    # Post caption
    caption = (
        "*Qo‘shni Farishta*\n\n"
        "╭──────────────\n"
        "├‣ Holati: Tugallangan\n"
        "├‣ Sifat: 720p\n"
        "├‣ Janr: Romantika, Komediya\n"
        "├‣ Kanal: @Anime_lar_New\n"
        "├‣ Qism: 12\n"
        "╰──────────────\n\n"
        "👇 Pastdagi tugmani bosing 👇"
    )

    # Tugma
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="▶️ Tomosha qilish",
            url="https://t.me/New_Anime_lar_Bot?start=qoshni_farishta"
        )
    )

    # Postni kanalga yuborish
    await bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=photo_file_id,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=keyboard
    )

    await message.reply("✅ Xabar *rasm bilan* kanalga yuborildi.", parse_mode="Markdown")


# === Botni ishga tushurish ===
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


# python "D:/anime_Bot/Tomosha-qilish.py"