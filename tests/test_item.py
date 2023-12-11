import csv
import os

import pytest

from src.item import Item


@pytest.fixture
def test_data():
    item_1 = Item("Смартфон", 10000, 5)
    item_2 = Item("Ноутбук", 25000, 3)
    item_1.pay_rate = 0.8
    item_2.pay_rate = 0.95
    return item_1, item_2


def test_calculate_total_price(test_data):
    assert test_data[0].calculate_total_price() == 50000
    assert test_data[1].calculate_total_price() == 75000


def test_apply_discount(test_data):
    test_data[0].apply_discount()
    assert test_data[0].price == 8000

    test_data[1].apply_discount()
    assert test_data[1].price == 23750


def test_item_name_setter(test_data):
    test_data[0].name = "Смартфон1234"
    assert test_data[0].name == "Смартфон12"

    test_data[1].name = "Ноут"
    assert test_data[1].name == "Ноут"


def test_string_to_number():
    assert Item.string_to_number("14.89") == 14
    assert Item.string_to_number("6") == 6


def test_instantiate_from_csv():
    test_csv_data = [["name", "price", "quantity"], ["item_1", 15.6, 3], ["item_2", 14.5, 3], ["item_3", 8.0, 4]]
    with open("test_file.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(test_csv_data)

    Item.instantiate_from_csv("test_file.csv")
    assert len(Item.all) == 3

    assert Item.all[0].name == "item_1"
    assert Item.all[0].price == 15.6
    assert Item.all[0].quantity == 3

    os.remove("test_file.csv")
