__all__ = ("app")

import logging
from aiohttp import web
from core.currency_rates_getter import CurrencyRatesGetter
from helpers.request_param_reader import get_currency_and_date_from_request

log = logging.getLogger(__name__)

# Создаем таблицу роутов (маршрутов)
routes = web.RouteTableDef()


# Регистрируем два адреса: без даты и с датой
@routes.get("/rates/{currency}")
@routes.get("/rates/{currency}/{date}")
async def get_currency_rates(request: web.Request) -> web.Response:
    # 1. Считываем и проверяем параметры запроса
    currency, selected_date = await get_currency_and_date_from_request(request)

    # 2. Создаем наш "Мозг" для добычи курсов
    getter = CurrencyRatesGetter(
        currency=currency,
        for_data=selected_date,
    )

    # 3. Получаем данные (из кэша или интернета) в виде байтовой строки JSON
    info_data_bytes = await getter.get_currency_info()

    # 4. Превращаем байты обратно в обычный текст (строку)
    json_text = info_data_bytes.decode("utf-8")

    log.info("Sending response for %r rates on date = %s", currency, selected_date)

    # 5. Возвращаем пользователю в браузер финальный JSON-ответ со статусом 200 OK
    return web.json_response(text=json_text)


# Функция сборки нашего веб-приложения
def create_app() -> web.Application:
    web_app = web.Application()
    # Привязываем наши маршруты (URL-адреса) к серверу
    web_app.add_routes(routes)
    return web_app


# Создаем готовый инстанс приложения
app = create_app()