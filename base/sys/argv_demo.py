#!/usr/bin/env python3

# ./argv_demo.py prod devops 53222 

# sys.argv[0] - (имя скрипта)
# sys.argv[1] - первый аргумент (сервер) 
# sys.argv[2] - второй аргумент (пользователь)
# sys.argv[3] - третий аргумент (порт)
# sys.argv[N] - N-й аргумент

import sys

if len(sys.argv) < 3:
    print(f"Использование: {sys.argv[0]} <сервер> | <пользователь> | <порт>")
    sys.exit(1)

server = sys.argv[1]
username = sys.argv[2]
port = sys.argv[3]

print(f"Скрипт: {sys.argv[0]}")
print(f"Подключение к серверу: {server}")
print(f"Пользователь: {username}")
print(f"Порт: {port}")