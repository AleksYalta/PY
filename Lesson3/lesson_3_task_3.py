from Address import Address
from Mailing import Mailing

to_address = Address("298600", "Ялта", "Красноармейская", "48", "54")
from_address = Address("854794", "Симферополь", "Киевская", "54", "77")

mailing = Mailing(to_address, from_address, 350, "5454564874521")

print(mailing.get_info())
