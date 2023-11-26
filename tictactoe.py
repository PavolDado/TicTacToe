width = height = 3
number_of_signs = 3
playground = [['_' for x in range(width)] for y in range(height)]
player_signs = ['X', 'O']


def add_move(playground, player_sign):
    success = True
    while success:
        line = input('Enter line: ')
        row = input('Enter column: ')

        if line.lower() != 'q' and row.lower() != 'q':
            if line.isdigit() and row.isdigit():
                line = int(line)
                row = int(row)
                if line < 3 and row < 3:
                    if playground[line][row] == '_':
                        playground[line][row] = player_sign
                        success = False
                        return True
                    else:
                        print('This cell is occupied!')
                else:
                    print('Coordinates are out of range')
            else:
                print('Coordinates must be numbers')
        else:
            print('Game canceled by player')
            success = False
            return False


def print_playground(playground):
    for i in range(len(playground)):
        line = f'Line: {i} '
        for x in range(len(playground[i])):
            line += f'| {playground[i][x]} '
        print(f'{line}|')
    print('-' * 21, '\nColumns:  0   1   2')
    print()


def check_win(playground, width, height, player_sign, number_of_signs=3):
    tmp_array_h, tmp_array_v, tmp_array_dd, tmp_array_du = [], [], [], []
    tmp_array_all = []
    tmp_win_line = player_sign * number_of_signs
    continue_game = True
    tmp_empty = 0

    for y in range(height):
        for x in range(width):
            tmp_array_v.append(playground[x][y])
            tmp_array_h.append(playground[y][x])
        tmp_array_dd.append(playground[y][y])
        tmp_array_du.append(playground[y][height - y - 1])
        tmp_array_all.append(tmp_array_v)
        tmp_array_all.append(tmp_array_h)
        tmp_array_h, tmp_array_v = [], []
    tmp_array_all.append(tmp_array_dd)
    tmp_array_all.append(tmp_array_du)

    for a in tmp_array_all:
        if '_' in a:
            tmp_empty += 1

        if tmp_win_line in ''.join(a):
            continue_game = False
            print(f'Player {player_signs[tmp_counter % 2]} wins!')
            print_playground(playground)
    if tmp_empty == 0 and continue_game:
        print('No winner found')
        continue_game = False
    return continue_game


game_continue = True
tmp_counter = 0
while game_continue:
    print_playground(playground)
    if game_continue:
        game_continue = add_move(playground, player_signs[tmp_counter % 2])
        if game_continue:
            game_continue = check_win(playground, width, height,
                                      player_signs[tmp_counter % 2])

    tmp_counter += 1
