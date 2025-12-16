from Address import Address
from Mailing import Mailing

to_address = Address("125009", "Москва", "Тверская", "6", "20")
from_address = Address("190000", "Санкт-Петербург",
                       "Невский проспект", "15", "8")

mailing = Mailing(to_address, from_address, 750, "RU987654321CN")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, "
    f"{mailing.from_address.town}, {mailing.from_address.street}, "
    f"{mailing.from_address.house} - {mailing.from_address.flat} "
    f"в {mailing.to_address.index}, {mailing.to_address.town}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.flat}. Стоимость {mailing.cost} рублей."
)
