import os
import random
import time

N = 10  # Размер игрового поля
M = 10

player_symbol = u"\u263A"  # Смайлик для игрока
apple_symbol = u"\u25A0"  # Символ для яблока

player_pos = [N//2, M//2]  # Начальное положение игрока
apples = [[random.randint(0, N-1), random.randint(0, M-1)] for _ in range(5)]  # Произвольное размещение яблок

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана
    for i in range(N):
        for j in range(M):
            if [i, j] == player_pos:
                print(player_symbol, end=' ')
            elif [i, j] in apples:
                print(apple_symbol, end=' ')
            else:
                print(".", end=' ')
        print()

def move_player():
    key = input("Введите WASD для перемещения: ").lower()
    if key == 'w':
        player_pos[0] = max(0, player_pos[0] - 1)
    elif key == 's':
        player_pos[0] = min(N-1, player_pos[0] + 1)
    elif key == 'a':
        player_pos[1] = max(0, player_pos[1] - 1)
    elif key == 'd':
        player_pos[1] = min(M-1, player_pos[1] + 1)

def main():
    score = 0
    while True:
        print_board()
        move_player()
        if player_pos in apples:
            apples.remove(player_pos)
            score += 1
            if len(apples) == 0:
                print("Вы победили!")
                time.sleep(5)  # Задержка в 5 секунду
                break

if __name__ == "__main__":
    main()
