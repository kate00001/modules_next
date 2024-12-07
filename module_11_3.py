from pprint import pprint
import math


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = []
    methods = []

    for item in dir(obj):
        value = getattr(obj, item)
        if callable(value):
            if not item.startswith("__"):
                methods.append(item)
        else:
            if not item.startswith("__"):
                attributes.append(item)

    obj_module = getattr(obj, "__module__", "built-in")

    info = {
        "Что интроспектируем:": obj,
        "Тип объекта:": obj_type,
        "Аттрибуты:": attributes,
        "Методы:": methods,
        "Модуль:": obj_module
    }

    return info


my_age = introspection_info(124)
pprint(my_age)

my_name = introspection_info("Екатерина")
pprint(my_name)

info = introspection_info(math.sqrt)
pprint(info) #Хотела проверить другой модуль

