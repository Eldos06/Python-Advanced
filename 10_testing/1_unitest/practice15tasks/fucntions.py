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
