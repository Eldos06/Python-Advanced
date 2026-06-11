import logging
from aiohttp import web
from app import app
from core.config import CACHE_DIR, configure_logging

log = logging.getLogger(__name__)


def main() -> None:
    # Перед стартом создаем физическую папку кэша на диске, если её ещё нет
    CACHE_DIR.mkdir(exist_ok=True)

    # Включаем систему логирования
    configure_logging()

    # Запускаем наш веб-сервер на локальном компьютере на порту 8081
    # Сервер будет активен по адресу http://localhost:8081
    web.run_app(app, port=8081)


# Проверка: если файл запущен напрямую (а не импортирован куда-то), выполняем функцию main
if __name__ == '__main__':
    main()