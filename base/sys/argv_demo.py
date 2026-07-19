#!/usr/bin/env python3

# sys.argv[0] — имя скрипта
# sys.argv[1] — первый аргумент
# sys.argv[2] — второй аргумент
# sys.argv[N] — N аргумент

import sys

print(f"Скрипт: {sys.argv[0]}")

name = sys.argv[1] if len(sys.argv) > 1 else "мир"
print(f"Привет, {name}!")
