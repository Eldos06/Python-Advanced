import json
from datetime import date
from aiohttp import web
from core.currency_exists_check import check

# Проверяем, нормальную ли валюту запросил пользователь
async def validate_currency(currency: str) -> str:
    if await check.currency_exists(currency):
        return currency  # Если всё ок, возвращаем её имя

    # Если валюта фейковая — прерываем работу и отдаем клиенту ошибку 404 (Not Found)
    msg = f"Unknown currency: {currency!r}, please try again later"
    raise web.HTTPNotFound(
        body=json.dumps({"message": msg}),
        reason=msg,
        content_type="application/json",
    )

from datetime import date, timedelta

# Метод для обработки даты
def validate_provided_date(provided_date: str | None) -> date:
    # По умолчанию ставим «вчерашний» день, так как за сегодня котировки в бесплатном API еще могут не появиться
    selected_date = date.today() - timedelta(days=1)

    # Если пользователь сам передал конкретную дату в адресе
    if provided_date is not None:
        try:
            # Пытаемся превратить строку типа "2024-03-10" в объект даты
            selected_date = date.fromisoformat(provided_date)
        except ValueError:
            # Если юзер написал ерунду вместо даты — отдаем ошибку 422 (Необрабатываемый объект)
            msg = "Provided date is not a valid date, please use ISO format"
            raise web.HTTPUnprocessableEntity(
                body=json.dumps({"message": msg}),
                reason=msg,
                content_type="application/json",
            )

    return selected_date

# Главная функция, которая собирает всё вместе
async def get_currency_and_date_from_request(
        request: web.Request,
) -> tuple[str, date]:
    # Берем валюту из URL, переводим в нижний регистр и валидируем
    currency: str = await validate_currency(
        request.match_info["currency"].lower(),
    )
    # Берем дату из URL (если она там есть) и валидируем
    selected_date: date = validate_provided_date(
        request.match_info.get("date"),
    )
    return currency, selected_date