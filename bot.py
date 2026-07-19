import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database.database import create_tables


# ------------------------
# User Handlers
# ------------------------

from handlers.start import router as start_router
from handlers.help import router as help_router
from handlers.card import router as card_router
from handlers.profile import router as profile_router
from handlers.roll import router as roll_router
from handlers.inventory import router as inventory_router
from handlers.daily import router as daily_router
from handlers.chi import router as chi_router

from handlers.store import router as store_router
from handlers.market import router as market_router
from handlers.sell import router as sell_router
from handlers.my_market import router as my_market_router
from handlers.collections import router as collections_router
from handlers.double import router as double_router

from handlers.flex import router as flex_router
from handlers.burn import router as burn_router



# ------------------------
# Admin Handlers
# ------------------------

from handlers.card_admin import router as card_admin_router
from handlers.collection_admin import router as collection_admin_router



bot = Bot(
    token=BOT_TOKEN
)


dp = Dispatcher()



# ------------------------
# User Commands
# ------------------------

dp.include_router(start_router)
dp.include_router(help_router)
dp.include_router(profile_router)
dp.include_router(card_router)
dp.include_router(roll_router)
dp.include_router(inventory_router)
dp.include_router(daily_router)
dp.include_router(chi_router)

dp.include_router(store_router)
dp.include_router(market_router)
dp.include_router(sell_router)
dp.include_router(my_market_router)

dp.include_router(collections_router)
dp.include_router(double_router)

dp.include_router(flex_router)
dp.include_router(burn_router)



# ------------------------
# Admin Commands
# ------------------------

dp.include_router(card_admin_router)
dp.include_router(collection_admin_router)



async def main():

    create_tables()

    await dp.start_polling(bot)



if __name__ == "__main__":

    asyncio.run(main())