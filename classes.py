from random import randint, sample
from time import sleep


class Player:   
    def __init__(self, name) -> None:
        self.name = name
        self.card = None
        self.am_i_win = False
        self.am_i_loose = False

    def __repr__(self) -> str:
        return f'Player {self.name}'
    
    def make_a_move(self, number):
        is_number_in_card = self.card.is_number_in_card(number)
        print('Зачеркнуть выпавший номер? y/n')

        while True:
            answer = input()
            try:
                if answer.lower() != 'y' or answer.lower() != 'n':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Введен некорректный символ, попробуйте ещё раз')
                continue

        if is_number_in_card:  # True
            if answer.lower() == 'y':  # True
                self.card.cross_number_in_card(number)

                if self.card.is_all_numbers_cross():
                    self.am_i_win = True

                print(f'Игрок {self.name} зачеркнул номер {number}')
            else:  # False
                self.am_i_loose = True
        else: # False
            if answer.lower() == 'y':  # True
                self.am_i_loose = True
            else:  # False
                print(f'Игрок {self.name} пропустил ход')
 

class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)

    def make_a_move(self, number):
        is_number_in_card = self.card.is_number_in_card(number)

        if is_number_in_card:
            self.card.cross_number_in_card(number)

            if self.card.is_all_numbers_cross():
                self.am_i_win = True

            print(f'Игрок {self.name} зачеркнул номер {number}')
        else:
            print(f'Игрок {self.name} пропустил ход')


class Card:

    def __init__(self, numbers: [], owner_name: str) -> None:
        self._all_nums = numbers
        
        self._owner_name = owner_name

        self._sorted_nums = []
        self._rand_indexes = []

        self._sorted_nums.append(sorted(self._all_nums[0:5]))
        self._sorted_nums.append(sorted(self._all_nums[5:10]))
        self._sorted_nums.append(sorted(self._all_nums[10:]))

        for _ in range(3):
            self._rand_indexes.append(sorted(sample(range(1, 10), 5)))

        self._nums_as_string_array = self._get_string_repr_of_nums(self._sorted_nums, self._rand_indexes)

    def _get_string_repr_of_nums(self, nums, indexes) -> list:
        card_str = []

        for i in range(len(nums)):
            nums_ptr = 0
            indx_ptr = 0
            string = []
            for j in range(1, 10):
                if nums_ptr > 4 and indx_ptr > 4:
                    string.append(' ' * 3)
                else:
                    val = indexes[i][indx_ptr]
                    if val == j:
                        string.append(f'{nums[i][nums_ptr]:>3}')
                        nums_ptr += 1
                        indx_ptr += 1
                    else:
                        string.append(' ' * 3)
            card_str.append(string)
        return card_str

    def draw(self) -> None:

        card_header = f'{"Карточка игрока " + self._owner_name:-^27}' \
            if len(f'{"Карточка игрока " + self._owner_name}') < 27 \
            else f'{"Карточка игрока " + self._owner_name}'
        
        print('\n' + card_header)

        for item in self._nums_as_string_array:
            print(*item, sep='')

        print('-' * 27)
    
    def cross_number_in_card(self, number: int) -> None:
        position = None
        for i in range(3):
            for j in range(5):
                if self._sorted_nums[i][j] == number:
                    position = i, j
                    break

        index = self._rand_indexes[position[0]][position[1]]

        self._nums_as_string_array[position[0]][index - 1] = ' - '

        del self._all_nums[0]

    def is_number_in_card(self, number: int) -> bool:
        return True if number in self._all_nums else False

    def is_all_numbers_cross(self) -> bool:
        return True if len(self._all_nums) == 0 else False


class SequenceMaker:
    def __init__(self):
        self._all_nums = []

        for i in range(1, 91):
            self._all_nums.append(i)

    def get_nums(self) -> []:
        num_list = []       
        for _ in range(15):
            length = len(self._all_nums)
            num_list.append(self._all_nums.pop(randint(0, length - 1)))

        return num_list


class Bag:
    def __init__(self) -> None:
        self._numbers = []
        self._remains = 0

        for i in range(1, 91):
            self._numbers.append(i)

        self._remains = len(self._numbers)

    def _delete_number_from_bag(self, index: int) -> None:
        del self._numbers[index]

    def _get_number(self) -> int:
        index = randint(0, len(self._numbers) - 1)
        number_by_index = self._numbers[index]
        self._delete_number_from_bag(index)
        return number_by_index

    @property
    def number(self) -> int:
        return self._get_number()
    
    @property
    def remains(self) -> int:
        return len(self._numbers)


class Game:
    def __init__(self, *players) -> None:
        self._players = players
        self.bag = Bag()

    def start(self):
        maker = SequenceMaker()
        player1 = self._players[0]
        player2 = self._players[1]

        player1.card = Card(maker.get_nums(), player1.name)
        player2.card = Card(maker.get_nums(), player2.name)

        player1.card.draw()
        player2.card.draw()

        while True:
            
            if self.bag.remains == 0:
                print('Бочёнков в мешке не осталось. Ничья.')
                break

            print(f'\nХод игрока {player1.name}')

            number = self.bag.number

            print(f'Бочёнок № {number}, бочёнков в мешке: {self.bag.remains}')

            player1.card.draw()
            player2.card.draw()

            player1.make_a_move(number)

            if player1.am_i_win:
                print(f'Игрок {player1.name} победил!')
                break

            if player1.am_i_loose:
                print(f'Игрок {player2.name} победил!')
                break

            if isinstance(player1, ComputerPlayer) and isinstance(player2, ComputerPlayer):
                sleep(2)

            print(f'\nХод игрока {player2.name}')

            number = self.bag.number
            
            print(f'Бочёнок № {number}, бочёнков в мешке: {self.bag.remains}')

            player1.card.draw()
            player2.card.draw()

            player2.make_a_move(number)

            if player2.am_i_win:
                print(f'Игрок {player2.name} победил!')
                break

            if player2.am_i_loose:
                print(f'Игрок {player1.name} победил!')
                break

            if isinstance(player1, ComputerPlayer) and isinstance(player2, ComputerPlayer):
                sleep(2)
