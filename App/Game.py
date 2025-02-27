from colorama import*
# import asyncio

init()

print(f" {Fore.RED}           1) Player 1 (X) {Fore.RESET} vs {Fore.BLUE} 2) Player 2 (O)")

player_list = {"1", "2"}

while True:
    user_input = input(f"{Fore.RESET}Vidite variant: ")
    if user_input in player_list:
        print("Complit input")
        break
    else:
        print("Еблан шоли?")

# print(f"{Fore.YELLOW}  "
#                 "                        1 | 2 | 3\n  "
#                 "                       -----------\n " 
#                 "                         4 | 5 | 6\n  " 
#                 "                       -----------\n " 
#                 "                         7 | 8 | 9  ")


