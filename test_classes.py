def test_getting_number(number_from_bag):
    print(f'  Number from bag is {number_from_bag}')
    assert 1 <= number_from_bag <= 90


def test_remain_difference(remain_difference):
    print(f' Before: {remain_difference[0]}, after: {remain_difference[1]}')
    assert remain_difference[0] - remain_difference[1] == 1


def test_of_number_amount(set_of_number):
    for item in set_of_number:
        print(f'{item} ', end='')
    assert len(set_of_number) == 15


def test_of_negative_exist(set_of_number):
    has_negative = False
    for item in set_of_number:
        has_negative = True if item < 0 else False
        print(f'{item} ', end='')
    assert has_negative is False


def test_of_list_type(set_of_number):
    assert type(set_of_number) is list
