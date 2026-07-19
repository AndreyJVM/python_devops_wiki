#!/usr/bin/env python3

# sys.exit(1) - Ошибка!
# sys.exit(0) - Успех!

import sys

if len(sys.argv) < 2:
    print("Нужно передать имя сервера")
    sys.exit(1)

server = sys.argv[1]
print(f"Деплой на {server}")
sys.exit(0)