#!/usr/bin/env python3

# ./argv_demo.py Andrey 25
# sys.argv[0] — имя скрипта
# sys.argv[1] — первый аргумент
# sys.argv[N] — N-й аргумент

import sys

if len(sys.argv) < 2:
    print(f"Использование: {sys.argv[0]} <имя> [возраст]")
    sys.exit(1)

name = sys.argv[1]
age = sys.argv[2] if len(sys.argv) > 2 else "не указан"

print(f"Скрипт: {sys.argv[0]}")
print(f"Имя: {name}")
print(f"Возраст: {age}")