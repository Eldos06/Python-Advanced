from datetime import datetime, timedelta


def calculate_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть от 0 до 100%")
    return price * (1 - discount / 100)

def truncate_text(text: str, max_length: int) -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email.split("@")[-1]

def is_admin(user_roles: list[str]) -> bool:
    return "admin" in [role.lower() for role in user_roles]

def safe_divide(a: float, b: float, default=0.0) -> float:
    if b == 0:
        return default
    return a / b

def rub_to_usd(rub_amount: float, rate: float) -> float:
    if rub_amount < 0 or rate <= 0:
        raise ValueError("Некорректные данные")
    return round(rub_amount / rate, 2)

def check_nickname(nickname: str) -> bool:
    bad_words = ["admin", "root", "pizda", "gavno"]
    return not any(word in nickname.lower() for word in bad_words)


# Средние задачи (Middle)
class Cart:
    def __init__(self):
        self.items = {}  # Словарь вида {"название_товара": общая_стоимость}

    def add_item(self, name: str, price: float, quantity: int = 1):
        if price <= 0 or quantity <= 0:
            raise ValueError("Некорректная цена или количество")
        self.items[name] = self.items.get(name, 0) + (price * quantity)

    def get_total(self) -> float:
        return sum(self.items.values())

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, token: str, username: str, duration_sec: int) -> None:
        expire_at = datetime.now() + timedelta(seconds=duration_sec)
        self.sessions[token] = {"username": username, "expires": expire_at}

    def is_active(self, token: str) -> bool:
        if token not in self.sessions:
            return False
        return self.sessions[token]["expires"] > datetime.now()


def parse_user_balance(json_data: dict) -> dict:
    user_info = json_data.get("response", {}).get("user", {})
    if "id" not in user_info or "balance" not in user_info:
        raise KeyError("Missing required fields")
    return {"user_id": user_info["id"], "balance": float(user_info["balance"])}

def get_page_items(items: list, page: int, page_size: int) -> list:
    if page <= 0 or page_size <= 0:
        return []
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end]
