#!/usr/bin/env python3

# ./argv_demo.py sys.argv[1] sys.argv[2] ... sys.argv[N]
# ./argv_demo.py Andrey Vorobev ... 24

# sys.argv[0] — имя скрипта argv_demo.py
# sys.argv[1] — первый аргумент
# sys.argv[2] — второй аргумент
# sys.argv[N] — N аргумент

import sys

print(f"Скрипт: {sys.argv[0]}")

name = sys.argv[1] if len(sys.argv) > 1 else "мир"
print(f"Привет, {name}!")
