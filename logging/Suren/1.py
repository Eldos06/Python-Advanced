# ❌ Плохой подход — print

def process_payment(amount, user_id):  # usage
    print(f"Processing payment for user {user_id}")  # ❌ Нет временной метки
    print(f"Amount: {amount}")  # ❌ Нет уровня важности
    try:
        # ... операции с платежом
        raise Exception("Payment failed")  # Искусственно вызываем ошибку
        print("Payment successful")  # ❌ Нельзя отключить в production
    except Exception as e:
        print(f"Error: {e}")  # ❌ Нет stacktrace


process_payment(amount=1, user_id=1)

# ✅ Правильный подход — logging

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def process_payment_logged(amount, user_id):
    logger.info("Processing payment for user %s", user_id)
    logger.info("Amount: %s", amount)
    try:
        raise Exception("Payment failed")  # Искусственно вызываем ошибку
        logger.info("Payment successful")
    except Exception as e:
        logger.exception("Error occurred")  # Покажет traceback


process_payment_logged(amount=1, user_id=1)
