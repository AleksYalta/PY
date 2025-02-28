from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "3250", "+79781111111"),
    Smartphone("Siemens", "a56", "+79782222222"),
    Smartphone("Sony_Ericson", "r52", "+79783333333"),
    Smartphone("Motorolla", "rzv3", "+79784444444"),
    Smartphone("Samsung", "www", "+79785555555")

]

for Smartphone in catalog:
    print(Smartphone.get_info())
