PLAYER_SYMBOLS = "-OX"
ROW_INDICES = "ABC"
COLUMN_INDICES = "123"

def print_game_map(gm):
    for row in gm:
        for cell in row:
            print(PLAYER_SYMBOLS[cell], end=" ")
        print()

def is_tie(gm):
    for row in gm:
        for cell in row:
            if cell == 0:
                return False
    return True

def is_completed(gm):
    for row in gm:
        first = row[0]
        if first != 0:
            for cell in row[1:]:
                if cell != first:
                    break
            else:
                return True, first
    for j in range(len(gm[0])):
        first = gm[0][j]
        if first != 0:
            for i in range(1, len(gm)):
                if gm[i][j] != first:
                    break
                else:
                    return True, first
    diag = gm[0][0]
    if diag != 0:
        for i in range(len(gm)):
            if gm[i][i] != diag:
                break
        else:
            return True, diag
    inv_diag = gm[0][len(gm[0]) - 1]
    if inv_diag != 0:
        for i in range(len(gm)):
            if gm[i][len(gm) - i - 1] != inv_diag:
                break
        else:
            return True, inv_diag
    return is_tie(gm), 0

game_map = []
for _ in range(3):
    temp = []
    for _ in range(3):
        temp.append(0)
    game_map.append(temp)



current_player = 1
completed = False
who_won = 0
while not completed:
    print_game_map(game_map)
    player_input = input(f"Игрок №{current_player}, введите позицию в формате А1: ")
    if len(player_input) != 2:
        print("Введено неверное количество символов. Формат ввода: А1")
        continue
    player_row, player_column = player_input

    player_row = ROW_INDICES.find(player_row)
    if player_row == -1:
        print("Неверный номер ряда. Укажите букву А, В, С")
        continue

    player_column = COLUMN_INDICES.find(player_column)
    if player_column == -1:
        print("Неверный номер ряда. Укажите цифру 1, 2, 3")
        continue

    if game_map[player_row][player_column] > 0:
        print("Ячейка уже занята, выберите другую ")
        continue
    game_map[player_row][player_column] = current_player

    completed, who_won = is_completed(game_map)

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1
    else:
        print("Неверный номер игрока")
        exit(1)

print_game_map(game_map)
if who_won != 0:
    print(f"Игрок №{who_won} победил! ")
else:
    print("Ничья! ")