# Месяц — сезон
def month_to_season(month):
    if 12 <= month <= 2:
        return "Зима"
    elif 3 <= month <= 5:
        return "Весна"
    elif 6 <= month <= 8:
        return "Лето"
    elif 9 <= month <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


month = int(input("Введите номер месяца (1-12): "))
print(month_to_season(month))

# def month_to_season(month):
#     if month in [12, 1, 2]:
#         return "Зима"
#     elif month in [3, 4, 5]:
#         return "Весна"
#     elif month in [6, 7, 8]:
#         return "Лето"
#     elif month in [9, 10, 11]:
#         return "Осень"
#     else:
#         return "Неверный номер месяца"
#
# month = int(input("Введите номер месяца (1-12): "))
# print(month_to_season(month))
