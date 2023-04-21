
from function import get_first_id_info, get_second_id_info, get_third_id_info, get_fourth_id_info, get_five_id_info, \
    get_description, get_date, get_to, get_amount_from_list, gettofromlist


def test_get_first_id_info():
    lst = [{'id': 1}, {'id': 2}, {'id': 1}]
    assert get_first_id_info(lst) == [{'id': 1}, {'id': 1}]


def test_get_second_id_info():
    lst = [{'id': 1}, {'id': 2}, {'id': 2}]
    assert get_second_id_info(lst) == [{'id': 2}, {'id': 2}]


def test_get_third_id_info():
    lst = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 3}]
    assert get_third_id_info(lst) == [{'id': 3}, {'id': 3}]


def test_get_fourth_id_info():
    lst = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 4}]
    assert get_fourth_id_info(lst) == [{'id': 4}, {'id': 4}]


def test_get_five_id_info():
    lst = [{'id': 1}, {'id': 2}, {'id': 3}, {'id': 4}, {'id': 5}, {'id': 5}]
    assert get_five_id_info(lst) == [{'id': 5}, {'id': 5}]


def test_get_description():
    data = [{'description': 'Перевод организации'}, {'description': 'Оплата услуг'}, {'description': 'Покупка товаров'}]
    assert get_description(data) == 'Перевод организации'


def test_get_date():
    data = [{'date': '2019-12-07T06:17:14.634890'}, {'date': '2020-01-15T09:25:37.123456'}]
    assert get_date(data) == '07.12.2019'


def test_get_to():
    accounts = [{'to': 'Счет 35158586384610753655'}, {'to': 'Карта 4276123456789012'}]
    assert get_to(accounts) == 'Счет 3655'


def test_get_amount_from_list():
    transactions = [{'operationAmount': {'amount': '48150.39'}}, {'operationAmount': {'amount': '1000'}}]
    assert get_amount_from_list(transactions) == 48150.39


def test_gettofromlist():
    transactions = [{'from': 'Visa Platinum 7000 7979 1234 6361'}, {'from': 'Mastercard 5555 4444 3333 1111'}]
    assert gettofromlist(transactions) == 'Visa Platinum 7000 **** **** 6361 Mastercard 5555 **** **** 1111'