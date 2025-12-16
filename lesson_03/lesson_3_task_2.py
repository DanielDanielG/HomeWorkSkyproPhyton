from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "A10", "+798567895231"),
    Smartphone("Nokia", "3210", "+792165895231"),
    Smartphone("Sony Ericsson", "Xperia", "+795067895231"),
    Smartphone("Samsung", "A10", "+795289895254"),
    Smartphone("Samsung", "A10", "+792167801203")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model} - {phone.subscriber_number}")
