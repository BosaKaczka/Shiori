# import random

import discord
from discord import app_commands
from discord.ext import commands


class XO(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        possible_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rows = 3
        columns = 3

        def print_game_board():
            for x in range(rows):
                print("\n+---+---+---+")
                print("|", end="")
                for y in range(columns):
                    print("", game_board[x][y], end=" |")
            print("\n+---+---+---+")

        def modify_array(num, turn):
            num -= 1
            match num:
                case 0:
                    game_board[0][0] = turn
                case 1:
                    game_board[0][1] = turn
                case 2:
                    game_board[0][2] = turn
                case 3:
                    game_board[1][0] = turn
                case 4:
                    game_board[1][1] = turn
                case 5:
                    game_board[1][2] = turn
                case 6:
                    game_board[2][0] = turn
                case 7:
                    game_board[2][1] = turn
                case 8:
                    game_board[2][2] = turn

        def check_for_winner(board):
            # Check rows
            for row in board:
                if all(cell == 'X' for cell in row) or all(cell == 'O' for cell in row):
                    return True

            # Check columns
            for col in range(3):
                if all(row[col] == 'X' for row in board) or all(row[col] == 'O' for row in board):
                    return True

            # Check diagonals
            if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
                return True
            if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
                return True

            return False

        play = True
        turn = 'X'
        turn_counter = 0

        while play:
            print_game_board()

            if turn_counter % 2 == 0:
                number_picked = int(input("\nChoose a number [1-9]: "))
                if number_picked in possible_numbers:
                    modify_array(number_picked, turn)
                    possible_numbers.remove(number_picked)
                    turn_counter += 1
                else:
                    print("\nInvalid input. Please choose an available number.")
            else:
                # cpu_choice = random.choice(possible_numbers)
                # print("\nCpu choice:", cpu_choice)
                # modify_array(cpu_choice, turn)
                # possible_numbers.remove(cpu_choice)
                # turn_counter += 1
                number_picked = int(input("\nChoose a number [1-9]: "))
                if number_picked in possible_numbers:
                    modify_array(number_picked, turn)
                    possible_numbers.remove(number_picked)
                    turn_counter += 1
                else:
                    print("\nInvalid input. Please choose an available number.")

            if turn_counter >= 5 and check_for_winner(game_board):
                print_game_board()
                print(f"\nPlayer {turn} wins!")
                play = False
            elif turn_counter == 9:
                print_game_board()
                print("\nIt's a draw!")
                play = False

            turn = 'X' if turn == 'O' else 'O'


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(XO(bot))
