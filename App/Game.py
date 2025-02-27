from colorama import init, Fore

init()

# Игровое поле (список строк)
board = [" " for _ in range(9)]  

# Функция для отрисовки поля
def draw_board():
    print(f"{Fore.YELLOW}"
          f"  {board[0]} | {board[1]} | {board[2]}\n"
          f" -----------\n"
          f"  {board[3]} | {board[4]} | {board[5]}\n"
          f" -----------\n"
          f"  {board[6]} | {board[7]} | {board[8]}{Fore.RESET}\n")

# Проверка победителя
def check_winner():
    win_combos = [(0,1,2), (3,4,5), (6,7,8),  # Горизонтали
                  (0,3,6), (1,4,7), (2,5,8),  # Вертикали
                  (0,4,8), (2,4,6)]           # Диагонали
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]  # Возвращаем "X" или "O"
    return None

# Ввод хода
def make_move(player):
    while True:
        try:
            move = int(input(f"{Fore.RESET} Введите номер клетки (1-9) для {player}: ")) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = player
                break
            else:
                print(f"{Fore.RED} Клетка занята или номер некорректный!{Fore.RESET}")
        except ValueError:
            print(f"{Fore.RED} Введите число от 1 до 9!{Fore.RESET}")

# Основной игровой цикл
print(f" {Fore.RED} Player 1 (X) {Fore.RESET} vs {Fore.BLUE} Player 2 (O)")
draw_board()

for turn in range(9):  # Макс. 9 ходов
    current_player = "X" if turn % 2 == 0 else "O"
    make_move(current_player)
    draw_board()

    winner = check_winner()
    if winner:
        print(f"{Fore.GREEN} Победил {winner}!{Fore.RESET}")
        break
else:
    print(f"{Fore.CYAN} Ничья!{Fore.RESET}")



# from colorama import*
# # import asyncio

# init()

# print(f" {Fore.RED}           1) Player 1 (X) {Fore.RESET} vs {Fore.BLUE} 2) Player 2 (O)")

# player_list = {"1", "2"}

# while True:
#     user_input = input(f"{Fore.RESET}Vidite variant: ")
#     if user_input in player_list:
#         print("Complit input")
#         break
#     else:
        # print("Еблан шоли?")

# print(f"{Fore.YELLOW}  "
#                 "                        1 | 2 | 3\n  "
#                 "                       -----------\n " 
#                 "                         4 | 5 | 6\n  " 
#                 "                       -----------\n " 
#                 "                         7 | 8 | 9  ")



