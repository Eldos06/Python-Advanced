import random
choice = random.choice(["OK", "FAIL", "INVALID"])
import time
import functools

class WeatherDataError(Exception):
    pass

def retry(max_retries=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except WeatherDataError as e:
                    print(f"Attempt #{attempt} failed: {e}")
                    if attempt == max_retries:
                        print("ВСЁ, НАХУЙ, Я В ЛЕС, ВЫРАЩИВАТЬ КЛУБНИКУ")
                        raise
                    time.sleep(1)
        return wrapper
    return decorator





detals = {
    'max_retries' : 3
}


@retry(max_retries=detals['max_retries'])
def get_weather():
    suka = random.choice(["OK", "FAIL", "INVALID"])
    if suka == "FAIL":
        raise WeatherDataError("API failed")
    if suka == "INVALID":
        raise WeatherDataError("Invalid data")
    if suka == "OK":
        return "Cloudy"
    

try:
    result = get_weather()
    print("ЕБАТЬ, РАБОТАЕТ, МАТЬ ЕГО ТАК!", result)
except WeatherDataError as e:
    print("Пиздец:", e)

    



        

