from Address import Address


class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_info(self):
        return (f"Отправление {self.track} из {self.from_address.get_full_address()} "
                f"в {self.to_address.get_full_address()}. Стоимость {self.cost} рублей.")

# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
