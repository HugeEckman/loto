from pytest import fixture

from classes import Bag, SequenceMaker


@fixture(autouse=True)
def number_from_bag():
    bag = Bag()
    return bag.number


@fixture(autouse=True)
def remain_difference():
    bag = Bag()
    before = bag.remains
    bag.number
    after = bag.remains
    return before, after


@fixture(autouse=True)
def set_of_number():
    maker = SequenceMaker()
    return maker.get_nums()

