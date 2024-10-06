from enum import Enum


class Role(Enum):
    Customer = 1
    Supplier = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name.replace('_', ' ')) for key in cls]
