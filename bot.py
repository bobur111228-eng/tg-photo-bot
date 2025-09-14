import logging
from aiogram import Bot, Dispatcher, executor, types
import os

API_TOKEN = os.getenv("BOT_TOKEN")  # токен берём из переменных окружения

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=["photo"])
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    file_url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file_info.file_path}"

    await message.reply(
        f"✅ Фото успешно загружено!\n"
        f"🔗 Ссылка: {file_url}\n\n"
        f"📸 Фото хранится на серверах Telegram"
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
