import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

# инициализация логгера 
logger = logging.getLogger(__name__)


# конфигурация и запуск бота
async def main():
    # конфигурация логгирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s ' /
               '[%(asctime)s] - %(name)s - %(message)s'
        )

    #вывод в консоль информации о старте бота
    logger.info("Starting bot")

    #Загружаем информацию из Config
    config: Config = load_config()

    # Инициализируем бота и диспетчер
    bot: Bot = Bot(
        token=config.tg_bot.token,
        parse_mode='HTML'
        )
    
    dp: Dispatcher = Dispatcher()

    #Регистрируем необходимые роутеры
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    # Пропус апдейтов и старт поллинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main":
    asyncio.run(main())