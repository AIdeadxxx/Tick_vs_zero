from colorama import init, Fore
from TickTacBot import TicTacBot
from tqdm import tqdm
from rich.console import Console
from rich.progress import SpinnerColumn, Progress
import time

init()

bot = None
human_player = "X"

# Поле
board = [" "] * 9

# Выигрышные комбинации
wins = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# Доступные цвета
colors = {
    "1": Fore.RED,
    "2": Fore.BLUE,
    "3": Fore.YELLOW,
    "4": Fore.GREEN,
    "5": Fore.MAGENTA,
    "6": Fore.CYAN,
    "7": Fore.WHITE,
}

# def choose_game_mode():
#     while True:
#         chois = input("1 - Игрок против игрока, 2 - Игрок против бота?: ")
#         if chois == "1" or chois == "2":
#             return chois
#         print(f"{Fore.RED} ERORR! {Fore.RESET} Введите 1 (друг) или 2 (бот). ")

# def choose_bot_difficulty():
#     while True:
#         difficulty = input("Выберите сложность бота: Easy (1), Normal (Coming soon...), Hard (Coming soon...): ")
#         if difficulty == "1":
#             return difficulty
#         print(f"{Fore.RED} ERORR! {Fore.RESET} Введите 1 (Easy). ")

# game_mode = choose_game_mode()
# bot_difficulty = None

# if game_mode == "2":
#     bot_difficulty = choose_bot_difficulty()
for i in tqdm(range(50), desc="Loading", unit="iterations"):
    time.sleep(0.05)  # Имитация загрузки
print("Загрузка игры завершена!")

drinks = 3
counter = 0

while counter < drinks:
    mode = input("1 - Игрок против игрока, 2 - Игрок против бота?: ")
    if mode == "2":
        bot = TicTacBot("O")
        print(f"{Fore.GREEN} Вы будте против бота. Бот будет играть за 'O'. {Fore.RESET}")
        break
    elif mode == "1":
        print(f"{Fore.GREEN}Вы будете играть против другого игрока. Игрок 1 будет играть за 'X', игрок 2 за 'O'. {Fore.RESET}")
        break
    else:
        print(f"{Fore.RED} ERORR! {Fore.RESET} Введите 1 или 2")
        counter += 1

if counter == 3:
    print(f"{Fore.RED} Скорее всего вам пока рано играть в крестики нолики.")
    exit()

# Выбор цвета
print("Выберите цвет скина:\n1 - Красный\n2 - Синий\n3 - Жёлтый\n4 - Зелёный\n5 - Фиолетовый\n6 - Березовый\n7 - Белый")
color_choice = input("Введите номер цвета: ")
chosen_color = colors.get(color_choice, Fore.RESET)

# Скины для поля
skins = {
    "1": lambda: print(chosen_color +
        "  ╔═══╦═══╦═══╗\n"
        f"  ║ {board[0]} ║ {board[1]} ║ {board[2]} ║  \n"
        "  ╠═══╬═══╬═══╣\n"
        f"  ║ {board[3]} ║ {board[4]} ║ {board[5]} ║ \n"
        "  ╠═══╬═══╬═══╣\n"
        f"  ║ {board[6]} ║ {board[7]} ║ {board[8]} ║ \n"
        "  ╚═══╩═══╩═══╝" + Fore.RESET
    ),
    "2": lambda: print(chosen_color +
        f"  {board[0]} | {board[1]} | {board[2]}\n"
        " ---+---+---\n"
        f"  {board[3]} | {board[4]} | {board[5]}\n"
        " ---+---+---\n"
        f"  {board[6]} | {board[7]} | {board[8]}" + Fore.RESET
    ),
    "3": lambda: print(chosen_color +
        f"🚀━━━🚀━━━🚀\n"
        f"┃ {board[0]} ┃ {board[1]} ┃ {board[2]} ┃ \n"
        f"🚀━━━🚀━━━🚀\n"
        f"┃ {board[3]} ┃ {board[4]} ┃ {board[5]} ┃ \n"
        f"🚀━━━🚀━━━🚀\n"
        f"┃ {board[6]} ┃ {board[7]} ┃ {board[8]} ┃ \n"
        f"🚀━━━🚀━━━🚀\n" + Fore.RESET
    ),
    "4": lambda: print(chosen_color +
        f"░░░░░░░░░░░░░\n"
        f"░ {board[0]} ░ {board[1]} ░ {board[2]} ░ \n"
        f"░░░░░░░░░░░░░\n"
        f"░ {board[3]} ░ {board[4]} ░ {board[5]} ░ \n"
        f"░░░░░░░░░░░░░\n"
        f"░ {board[6]} ░ {board[7]} ░ {board[8]} ░ \n"
        f"░░░░░░░░░░░░░\n" + Fore.RESET
    ),
    "5" : lambda: print(chosen_color +
        f"█▀▀▀█▀▀▀█▀▀▀█\n"
        f"█ {board[0]} █ {board[1]} █ {board[2]} █ \n"
        f"█▄▄▄█▄▄▄█▄▄▄█\n"
        f"█ {board[3]} █ {board[4]} █ {board[5]} █ \n"
        f"█▀▀▀█▀▀▀█▀▀▀█\n"
        f"█ {board[6]} █ {board[7]} █ {board[8]} █ \n"
        f"█▄▄▄█▄▄▄█▄▄▄█\n" + Fore.RESET
    ),
    "0" : lambda: print(chosen_color +
        f"╭─1─┬─2─┬─3─╮\n"
        f"│ {board[0]} │ {board[1]} │ {board[2]} │ \n"
        f"├─4─┼─5─┼─6─┤\n"
        f"│ {board[3]} │ {board[4]} │ {board[5]} │ \n"
        f"├─7─┼─8─┼─9─┤\n"
        f"│ {board[6]} │ {board[7]} │ {board[8]} │ \n"
        f"╰───┴───┴───╯\n" + Fore.RESET
    ),
    "6" : lambda: print(chosen_color +
        f"○───○───○───○\n"
        f"│ {board[0]} │ {board[1]} │ {board[2]} │ \n"
        f"○───○───○───○\n"
        f"│ {board[3]} │ {board[4]} │ {board[5]} │ \n"
        f"○───○───○───○\n"
        f"│ {board[6]} │ {board[7]} │ {board[8]} │ \n"
        f"○───○───○───○\n" + Fore.RESET
    ),
    "7" : lambda: print(chosen_color +
        f"╱╲{board[0]}╱╲{board[1]}╱╲{board[2]}╱╲\n"
        f"╲╱ ╲╱ ╲╱ ╲╱ \n"
        f"╱╲{board[3]}╱╲{board[4]}╱╲{board[5]}╱╲\n"
        f"╲╱ ╲╱ ╲╱ ╲╱ \n"
        f"╱╲{board[6]}╱╲{board[7]}╱╲{board[8]}╱╲\n"
        f"╲╱ ╲╱ ╲╱ ╲╱ \n" + Fore.RESET
    ),
    "8" : lambda: print(chosen_color +
        f"{board[0]}ᛜ{board[1]}ᛝ{board[2]}ᛞ \n"
        f"────────\n"
        f"ᛟ{board[3]}ᛠ{board[4]}ᛡ{board[5]}ᛢ \n"
        f"────────\n"
        f"ᛣ{board[6]}ᛤ{board[7]}ᛥ{board[8]}ᛦ \n" + Fore.RESET
    )
}

for i in tqdm(range(40), desc="Open the skins", unit="iterations"):
    time.sleep(0.02)  # Имитация загрузки
print("Загрузка завершена!")

# Выбор скина
print("Выберите скин:\n0 - Стиль лабиринт(для новачков) \n1 - С рамками\n2 - Классический (по умолчанию)\n3 - Космический\n4 - Стиль пиксель-арт\n5 - Стиль кирпичики\n6 - Стиль пузыри\n7 - Стиль паутина(хард)\n8 - Стиль древние руны(HELL)")
skin_choice = input("Введите номер скина: ")
draw_board = skins.get(skin_choice, skins["2"])  # По умолчанию классический скин



# if game_mode == "2":
#     bot = TicTacBot("O")

# bot = TicTacBot("O")
# human_palyer = "X"

turn = 0

while turn < 9:
    draw_board()
    player = "X" if turn % 2 == 0 else "O"
        
    if bot and player == "O":
        console = Console()

        with Progress(SpinnerColumn(), *Progress.get_default_columns(), console=console) as progress:
            task = progress.add_task("[cyan]Бот думает...", total=100)
            while not progress.finished:
                progress.update(task, advance=7)
                time.sleep(0.1)
        # print(f"{Fore.GREEN}Бот думает...{Fore.RESET}")
        move = bot.make_move(board)
    else:
        try:
            move = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
        except ValueError:
            print(Fore.RED + "Введите число от 1 до 9." + Fore.RESET)
            continue

    if move is None or move < 0 or move > 8 or board[move] != " ": #move is None or
        print(Fore.RED + "Неверный ход." + Fore.RESET)
        continue

    board[move] = player

    # Проверяем победу
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            draw_board()
            print(Fore.GREEN + f"Игрок {player} победил!" + Fore.RESET)
            exit()

    turn += 1

draw_board()
print(Fore.CYAN + "Ничья!" + Fore.RESET)
