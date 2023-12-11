import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Геттер для получения приватного атрибута name
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Сеттер для приватного атрибута name. Проверяет длину имени и сокращает до 10 символов.
        """
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        cls.all.clear()
        with open(path, encoding="windows-1251") as file:
            csv_dict = csv.DictReader(file)
            for row in csv_dict:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(text: str) -> int:
        return int(float(text))
