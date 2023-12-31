from classes import Player, ComputerPlayer, Game

player1 = None
player2 = None

promt = f'{"Игра в лото":-^70}\n'\
        'В каком режиме хотите сыграть? Введите цифру желаемого варианта:\n\n'\
        '1. Человек против компьютера\n'\
        '2. Человек против человека\n'\
        '3. Компьютер против компьютера\n\n' + f"{'-' * 70}"

print(promt)

while True:
    variant = int(input())

    if variant not in range(1, 4):
        print('Введен некорректный символ, попробуйте ещё раз')
        continue
    else:
        break

match variant:
    case 1:
        player1 = Player(name='Игрок')
        player2 = ComputerPlayer(name='Компьютер')
    case 2:
        player1 = Player(name='Игрок1')
        player2 = Player(name='Игрок2')
    case 3:
        player1 = ComputerPlayer(name='Компьютер1')
        player2 = ComputerPlayer(name='Компьютер2')

game = Game(player1, player2)
game.start()
