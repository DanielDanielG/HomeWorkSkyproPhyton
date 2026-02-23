import random

# ======================================
# НАСТРОЙКИ API - ЗАПОЛНИТЕ ИСХОДНЫМИ ДАННЫМИ
# ======================================

BASE_URL = "https://yougile.com"
API_KEY = ""
USER_ID = "6509c5a3-1c86-4071-9136-6a6405270e35"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def get_unique_title():
    """Генерирует уникальное имя для теста"""
    number = random.randint(10000, 99999)
    return f"TestProject_{number}"
